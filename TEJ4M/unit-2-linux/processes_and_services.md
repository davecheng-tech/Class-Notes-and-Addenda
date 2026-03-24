# Processes and Services

This note covers how Linux manages running programs. It explains:

- What a process is
- Viewing processes with `ps` and `top`
- Foreground and background processes
- Stopping processes with signals and `kill`
- Services and `systemctl`
- How processes connect to the networking concepts from Unit 1

<br>

## 1. What Is a Process?

Every running program on a Linux system is a **process**. When you open a terminal, that terminal is a process. When you run `ls`, that is a short-lived process. When Nginx serves a web page, that is a long-running process. Even the desktop environment you are looking at is a collection of processes.

Each process has:

| Property | Description |
|---|---|
| **PID** | Process ID — a unique number assigned by the kernel |
| **Owner** | The user account the process runs as |
| **Parent** | The process that started it (identified by PPID — parent process ID) |
| **State** | Whether the process is running, sleeping, stopped, etc. |
| **Resource usage** | How much CPU and memory it is consuming |

The kernel is responsible for managing all processes: allocating CPU time, managing memory, and ensuring that processes with different owners remain isolated from each other. This connects directly to the permission model from the previous note — a process runs with the permissions of the user account that owns it.

<br>

## 2. Viewing Processes

### `ps` — Snapshot of Processes

The `ps` command prints a snapshot of currently running processes.

**By itself, `ps` only shows processes owned by you in the current terminal session:**

```bash
ps
```

```
    PID TTY          TIME CMD
   1234 pts/0    00:00:00 bash
   1301 pts/0    00:00:00 ps
```

This is not very useful on its own. To see more, use flags:

### `ps aux` — All Processes on the System

```bash
ps aux
```

This shows every process from every user. There will be a lot of output. Here is a representative selection from one of our Chromebooks:

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.2  0.3  22932 14084 ?        Ss   10:20   0:02 /sbin/init splash
root         810  0.0  0.1  13684  6908 ?        Ss   10:20   0:00 /usr/libexec/bluetooth/bluetoothd
root         946  0.0  0.4 336504 19132 ?        Ssl  10:20   0:00 /usr/sbin/NetworkManager --no-daemon
syslog       951  0.0  0.1 222508  5804 ?        Ssl  10:20   0:00 /usr/sbin/rsyslogd -n -iNONE
navidro+    1065  0.1  0.9 2102592 37296 ?       Ssl  10:20   0:01 /usr/bin/navidrome
root        2024  0.0  0.2  12016  7992 ?        Ss   10:36   0:00 sshd: /usr/sbin/sshd -D [listener]
sta-tech    2048  0.0  0.1  11384  5228 pts/1    Ss   10:36   0:00 -bash
sta-tech    2121  0.0  0.1  13616  4508 pts/1    R+   10:39   0:00 ps auwx
```

Key columns:

| Column | Meaning |
|---|---|
| `USER` | The account that owns the process |
| `PID` | Process ID |
| `%CPU` | Percentage of CPU being used |
| `%MEM` | Percentage of physical memory being used |
| `STAT` | Process state (`S` = sleeping, `R` = running, `Z` = zombie, `T` = stopped) |
| `COMMAND` | The command that started the process |

Notice the `USER` column. You can see processes running as `root`, `www-data`, and your own username. This is the multi-user model in action — all these processes coexist on the same machine, each with different permissions.

> [!TIP]
> The output of `ps aux` is usually long. You can pipe it to `grep` to search for a specific process. For example, to find all SSH-related processes:
> ```bash
> ps aux | grep ssh
> ```

### `top` — Live Process Monitor

While `ps` shows a snapshot, `top` shows a **live, updating view** of processes sorted by resource usage:

```bash
top
```

The display refreshes automatically. The top section shows system-wide statistics (CPU usage, memory usage, number of processes), and the bottom section lists individual processes.

Useful keys while `top` is running:

| Key | Action |
|---|---|
| `q` | Quit |
| `M` | Sort by memory usage |
| `P` | Sort by CPU usage |
| `k` | Kill a process (prompts for PID) |

`top` is the tool to reach for when a machine feels slow. It immediately shows you which process is consuming the most CPU or memory.

> [!TIP]
> Try running `htop` — it is a more user-friendly alternative to `top` with colour, mouse support, and easier navigation. If it is not installed on your machine, install it with `sudo apt install htop`.

<br>

## 3. Foreground and Background

When you run a command in the terminal, it normally runs in the **foreground**: it takes over the terminal and you cannot type another command until it finishes. Most commands finish quickly, so this is fine.

But some commands run indefinitely. In Unit 1, you ran a Python HTTP server:

```bash
python3 -m http.server 8000
```

This command does not return — it keeps running, serving web pages, and your terminal is locked up. You cannot type anything else until you stop it.

### Ctrl+C — Stop a Foreground Process

Pressing **Ctrl+C** sends an interrupt signal to the foreground process, asking it to stop. This is the most common way to end a long-running command.

### Running a Command in the Background

Adding `&` to the end of a command starts it in the **background**. The process runs, but your terminal is free for other commands:

```bash
python3 -m http.server 8000 &
```

The terminal will print something like:

```
[1] 2456
```

This tells you the process is job number `[1]` with PID `2456`. You can now type other commands while the server continues running.

### `jobs` — List Background Jobs

```bash
jobs
```

Shows all jobs running in the background from this terminal session.

### Moving Processes Between Foreground and Background

| Action | How |
|---|---|
| Stop a foreground process temporarily | **Ctrl+Z** (suspends it, does not kill it) |
| Resume a suspended process in the background | `bg` |
| Bring a background process back to the foreground | `fg` |

A common workflow:

1. Start a long-running command and realize you need the terminal
2. Press **Ctrl+Z** to suspend it
3. Run `bg` to let it continue in the background
4. Do your other work
5. Run `fg` when you want to interact with it again

> [!WARNING]
> A process suspended with Ctrl+Z is **paused**, not running. If you suspend a web server, it stops serving pages until you resume it with `bg` or `fg`. This is different from Ctrl+C, which terminates the process entirely.

<br>

## 4. Signals and `kill`

When you press Ctrl+C, you are sending a **signal** to the process. Signals are the kernel's way of communicating with processes. The `kill` command lets you send signals to any process by its PID.

### Common Signals

| Signal | Number | Sent by | Effect |
|---|---|---|---|
| `SIGINT` | 2 | Ctrl+C | Politely asks the process to stop |
| `SIGTSTP` | 20 | Ctrl+Z | Suspends (pauses) the process |
| `SIGTERM` | 15 | `kill PID` | Politely asks the process to terminate (default) |
| `SIGKILL` | 9 | `kill -9 PID` | Forces the process to terminate immediately |

### Using `kill`

To stop a process, you need its PID. Find it with `ps aux | grep ...` or `top`, then:

```bash
kill 2456          # sends SIGTERM (polite request)
```

If the process does not respond:

```bash
kill -9 2456       # sends SIGKILL (forced termination)
```

> [!IMPORTANT]
> Always try `kill` (SIGTERM) before `kill -9` (SIGKILL). SIGTERM allows the process to clean up (close files, release resources). SIGKILL terminates it instantly with no cleanup, which can leave behind temporary files or corrupt data.

### You Can Only Kill Your Own Processes

The permission model applies to signals too. You can only send signals to processes owned by your user account. To kill a process owned by `root` or another user, you need `sudo`:

```bash
sudo kill 412
```

<br>

## 5. Services and `systemctl`

Some processes are designed to start automatically when the system boots and run continuously in the background. These are called **services** (or **daemons**).

You have already worked with several services in Unit 1:

| Service | What it does |
|---|---|
| `ssh` | Accepts remote login connections |
| `nginx` | Serves web pages |

Services are managed by **systemd**, the system and service manager on Lubuntu. You interact with it using the `systemctl` command.

### Checking Service Status

SSH is the one service guaranteed to be running on every machine in the class. Use it as a starting point:

```bash
systemctl status ssh
```

This shows whether the service is running, its PID, recent log output, and whether it is enabled to start at boot.

**On our Chromebooks:**

```
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; disabled; preset: enabled)
     Active: active (running) since Tue 2026-03-24 10:36:35 EDT; 2min 47s ago
TriggeredBy: ● ssh.socket
   Main PID: 2024 (sshd)
      Tasks: 1 (limit: 4352)
     Memory: 4.1M
```

Key information:

| Field | Meaning |
|---|---|
| `Active: active (running)` | The service is currently running |
| `disabled` / `enabled` | Whether the service starts automatically at boot |
| `Main PID` | The process ID of the service |
| `TriggeredBy` | Some services (like SSH here) are started on-demand by a socket rather than at boot |

You can check the status of any service this way. Try `systemctl status cups` or `systemctl status bluetooth` to see other services on your machine.

### Starting and Stopping Services

The examples below use Nginx as the service. If you do not have Nginx installed, you can follow along with any service you installed in Unit 1.

```bash
sudo systemctl stop nginx       # stop the service
sudo systemctl start nginx      # start the service
sudo systemctl restart nginx    # stop and then start (apply config changes)
```

These require `sudo` because managing system services is a privileged operation.

> [!NOTE]
> SSH on Lubuntu is configured slightly differently from most services — it uses a socket-activated setup, so restarting it requires additional steps (as you saw in Unit 1). Most services, including Nginx, follow the simpler pattern shown above.

### Enabling and Disabling Services at Boot

```bash
sudo systemctl enable nginx     # start automatically when the machine boots
sudo systemctl disable nginx    # do not start at boot (can still be started manually)
```

The distinction matters: `start`/`stop` affect the current session. `enable`/`disable` affect what happens on the next boot.

### The Pattern from Unit 1

In Unit 1, whenever you changed a configuration file, you restarted the service for the changes to take effect:

1. Edit the config file (e.g., `sudo nano /etc/nginx/sites-available/default`)
2. Restart the service (e.g., `sudo systemctl restart nginx`)
3. Verify the service is running (e.g., `systemctl status nginx`)

This is a standard workflow for system administration. Now you know what each step is actually doing: modifying the configuration file that the service reads, then telling systemd to stop and restart the process so it reads the updated file.

<br>

## 6. Process Hierarchy

Every process except the very first one is started by another process. This creates a tree structure.

The root of the tree is **PID 1**, which is the `init` process (on Lubuntu, this is systemd). It is the first process started by the kernel at boot, and every other process descends from it.

You can see the process tree with:

```bash
pstree
```

**Partial output on our Chromebooks (abbreviated):**

```
systemd─┬─ModemManager───3*[{ModemManager}]
        ├─NetworkManager───3*[{NetworkManager}]
        ├─bluetoothd
        ├─cron
        ├─cupsd
        ├─dbus-daemon
        ├─rsyslogd───3*[{rsyslogd}]
        ├─sddm─┬─Xorg───3*[{Xorg}]
        │       └─sddm-helper───lxqt-session─┬─lxqt-panel───5*[{lxqt-panel}]
        │                                     ├─openbox───{openbox}
        │                                     ├─pcmanfm-qt─┬─qterminal─┬─bash
        │                                     │            │           └─3*[{qterminal}]
        │                                     │            └─6*[{pcmanfm-qt}]
        │                                     └─3*[{lxqt-session}]
        ├─snapd───8*[{snapd}]
        ├─sshd───sshd───sshd───bash───pstree
        ├─systemd-journal
        ├─systemd-logind
        └─wpa_supplicant
```

Notice that everything branches from `systemd` at the top. You can trace any process back to PID 1. Look at the SSH line in particular: `sshd───sshd───sshd───bash───pstree` — the SSH daemon spawned a child process for the login session, which started a `bash` shell, which is running the `pstree` command itself.

To see PIDs included, use:

```bash
pstree -p
```

This is why systemd is so important: it is the ancestor of every service and user process on the system. When you use `systemctl` to manage a service, you are communicating with PID 1.

<br>

## 7. Key Terms

| Term | Definition |
|---|---|
| **Process** | A running instance of a program, identified by a PID |
| **PID** | Process ID — a unique number assigned to each process by the kernel |
| **PPID** | Parent Process ID — the PID of the process that started this one |
| **Foreground process** | A process that occupies the terminal; you cannot type until it finishes |
| **Background process** | A process that runs without occupying the terminal |
| **Signal** | A message sent by the kernel to a process (e.g., SIGTERM, SIGKILL) |
| **SIGTERM** | A signal that politely requests a process to terminate |
| **SIGKILL** | A signal that forces a process to terminate immediately |
| **Service (daemon)** | A process designed to run continuously in the background, typically started at boot |
| **systemd** | The system and service manager on Lubuntu; it is PID 1 |
| **systemctl** | The command-line tool for interacting with systemd |

<br>

## Exercise: Process Detective

In this exercise, you will start, find, manage, and stop processes on your Lubuntu machine. Record the commands you use and the output you observe.

### Part A: Observing Processes

1. Run `ps aux` and find the process for your terminal session (look for `bash` in the COMMAND column). What is its PID? What user owns it?

2. Run `ps aux | grep ssh`. Is the SSH service running? What user owns the SSH processes?

3. Run `top` and observe for 10 seconds. What process is currently using the most CPU? The most memory? Press `q` to quit.

### Part B: Managing a Process

4. Start a Python HTTP server on port 9000 in the foreground:
   ```bash
   python3 -m http.server 9000
   ```
   Your terminal is now locked. Press **Ctrl+Z** to suspend the server.

5. Run `jobs`. What does it show? What state is the server in?

6. Run `bg` to resume the server in the background. Confirm it is running by opening a browser on the same machine and visiting `http://127.0.0.1:9000`.

7. Use `ps aux | grep http.server` to find the server's PID. Write it down.

8. Use `kill` with the PID to stop the server. Verify it is gone by running `jobs` again and by trying to reload the page in the browser.

### Part C: Services

9. Check the status of the SSH service:
   ```bash
   systemctl status ssh
   ```
   Is it running? Is it enabled at boot? What is its PID?

10. Now inspect a different service. Install a lightweight web server to experiment with:
    ```bash
    sudo apt install nginx
    ```
    Check its status with `systemctl status nginx`. Is it running? What PID was it assigned?

11. Stop Nginx and check its status again:
    ```bash
    sudo systemctl stop nginx
    systemctl status nginx
    ```
    What changed in the output?

12. Start Nginx again and check its status:
    ```bash
    sudo systemctl start nginx
    systemctl status nginx
    ```
    Is the PID the same as before, or different? Why?

13. Run `pstree -p` and find the Nginx process in the tree. What is its parent process?
