# Permissions and Ownership

This note covers how Linux controls who can access files and directories. It explains:

- Why Linux is a multi-user operating system
- Users, groups, and service accounts
- Reading permission strings in `ls -l` output
- Changing permissions with `chmod`
- Changing ownership with `chown`
- How `sudo` fits into the permission model

<br>

## 1. Linux Is Multi-User by Design

Linux was built from the start to support multiple users on the same machine. This is not a theoretical feature — it is the foundation of how the entire operating system manages access and security.

Even on your Chromebook, where you are the only person logging in, there are many user accounts on the system. Run this command:

```bash
cat /etc/passwd
```

You will see dozens of entries. Most of them are not human users. They are **service accounts**: accounts that exist so specific programs can run with limited permissions. For example:

| Account | Purpose |
|---|---|
| `root` | The superuser — unrestricted access to everything |
| Your username | Your personal account |
| `www-data` | Runs the Nginx web server |
| `sshd` | Runs the SSH service |
| `nobody` | A minimal-privilege account used by some services |

This design exists for isolation. If the Nginx web server is compromised by an attacker, the damage is limited to what the `www-data` account can access — not the entire system. If every service ran as `root`, a single vulnerability could compromise everything.

The mechanism that enforces this isolation is **file permissions**.

<br>

## 2. Ownership: Users and Groups

Every file and directory on a Linux system has two owners:

1. A **user** (also called the owner)
2. A **group**

You can see this by running `ls -l` on any file:

```bash
ls -l /etc/hostname
```

```
-rw-r--r-- 1 root root 11 Mar 15 10:42 /etc/hostname
```

The two names after the number are the user and group:

```
-rw-r--r-- 1 root root 11 Mar 15 10:42 /etc/hostname
               │    │
               │    └── group: root
               └─────── user: root
```

This file is owned by user `root` and group `root`. Most system configuration files follow this pattern.

Now look at a file in your home directory:

```bash
ls -l ~/Desktop
```

The files there will be owned by your username and your group (which is usually the same as your username on single-user Lubuntu systems).

### What Is a Group?

A group is a collection of user accounts. Groups allow permissions to be shared among multiple users without giving access to everyone.

For example, a group called `students` might include three user accounts. Any file owned by the `students` group can be accessed by all three users according to the group permissions.

On your Chromebook, your user account belongs to several groups. You can see them with:

```bash
groups
```

Or for more detail:

```bash
id
```

This will show your user ID (`uid`), your primary group ID (`gid`), and any additional groups you belong to, such as `sudo` (which is why you are allowed to use the `sudo` command).

<br>

## 3. Reading Permission Strings

When you run `ls -l`, the first column shows the **permission string**:

```
-rwxr-xr-- 1 student student 2048 Mar 20 14:30 myscript.sh
```

The permission string is 10 characters:

```
- r w x r - x r - -
│ └─┬─┘   └─┬─┘   └─┬─┘
│   │       │       └── others (everyone else)
│   │       └────────── group
│   └────────────────── user (owner)
└────────────────────── file type: - (file), d (directory), l (symlink)
```

Each set of three characters represents:

| Character | Meaning |
|---|---|
| `r` | Read — can view the file's contents (or list a directory's contents) |
| `w` | Write — can modify the file (or create/delete files in a directory) |
| `x` | Execute — can run the file as a program (or enter a directory with `cd`) |
| `-` | That permission is not granted |

So `rwxr-xr--` means:

| Who | Permissions | Meaning |
|---|---|---|
| User (owner) | `rwx` | Read, write, and execute |
| Group | `r-x` | Read and execute, but not write |
| Others | `r--` | Read only |

### Directory Permissions

Permissions on directories have slightly different effects than on files:

| Permission | On a file | On a directory |
|---|---|---|
| `r` | Can read file contents | Can list directory contents (`ls`) |
| `w` | Can modify file contents | Can create or delete files inside |
| `x` | Can execute as a program | Can enter the directory (`cd`) |

A common point of confusion: to access a file inside a directory, you need `x` (execute) permission on the directory itself — even if you have read permission on the file. Without `x` on the directory, you cannot traverse into it.

<br>

## 4. Changing Permissions with `chmod`

The `chmod` command changes the permissions on a file or directory. There are two ways to use it: **numeric mode** and **symbolic mode**.

### Numeric Mode

Numeric mode uses a three-digit number where each digit represents permissions for the user, group, and others (in that order). Each digit is the sum of:

| Value | Permission |
|---|---|
| 4 | Read |
| 2 | Write |
| 1 | Execute |
| 0 | None |

Add the values together for each category:

| Number | Permissions | Meaning |
|---|---|---|
| `7` | `rwx` | 4 + 2 + 1 = read, write, execute |
| `6` | `rw-` | 4 + 2 = read, write |
| `5` | `r-x` | 4 + 1 = read, execute |
| `4` | `r--` | 4 = read only |
| `0` | `---` | No permissions |

Examples:

```bash
chmod 755 myscript.sh    # user: rwx, group: r-x, others: r-x
chmod 644 notes.txt      # user: rw-, group: r--, others: r--
chmod 700 private/       # user: rwx, group: ---, others: ---
```

### Symbolic Mode

Symbolic mode uses letters to add or remove specific permissions:

```bash
chmod +x myscript.sh     # add execute for everyone
chmod u+w notes.txt      # add write for the user (owner)
chmod go-w shared.txt    # remove write for group and others
```

The letters are:

| Letter | Meaning |
|---|---|
| `u` | User (owner) |
| `g` | Group |
| `o` | Others |
| `a` | All (same as `ugo`) |

Symbolic mode is useful for quick changes. Numeric mode is more common when setting all permissions at once.

### Common Permission Patterns

| Numeric | String | Typical use |
|---|---|---|
| `755` | `rwxr-xr-x` | Programs and scripts — owner can modify, everyone can run |
| `644` | `rw-r--r--` | Regular files — owner can edit, everyone can read |
| `700` | `rwx------` | Private directories — only the owner has access |
| `600` | `rw-------` | Private files — only the owner can read and write |

<br>

## 5. Changing Ownership with `chown`

The `chown` command changes who owns a file. It requires `sudo` because changing ownership is a privileged operation.

### Change the user owner:

```bash
sudo chown alice report.txt
```

This makes `alice` the owner of `report.txt`.

### Change both user and group:

```bash
sudo chown alice:students report.txt
```

This sets the owner to `alice` and the group to `students`.

### Change ownership recursively (for a directory and everything inside it):

```bash
sudo chown -R alice:students project/
```

> [!WARNING]
> Be careful with `chown -R` on system directories. Changing ownership of files in `/etc` or `/usr` can break system services. Only use it on files and directories you created or manage.

### When Do You Need `chown`?

In Unit 1, some of you encountered situations where a web server could not read files you placed in `/var/www/html`, or where a service could not access its own configuration. These problems are almost always caused by incorrect ownership: the file exists but the service account (e.g., `www-data`) does not own it and cannot read it.

<br>

## 6. How `sudo` Fits In

You have been using `sudo` since Unit 1 without much explanation beyond "it gives you admin permissions." Here is what it actually does.

`sudo` runs a single command as the `root` user. The `root` account has no permission restrictions — it can read, write, and execute any file on the system.

```bash
sudo nano /etc/ssh/sshd_config
```

This opens the SSH configuration file for editing as `root`. Without `sudo`, your regular user account cannot write to files in `/etc` because they are owned by `root` and you are not `root`.

### Why Not Just Log In as root?

If `root` can do anything, why not use it for everything?

Because `root` can also break anything. A typo in a command run as `root` can delete system files, corrupt configurations, or make the machine unbootable. The permission model exists specifically to limit the damage that mistakes or malicious software can cause.

The principle is called **least privilege**: run with the minimum permissions needed for the task. Use `sudo` for the specific commands that require elevated access, then return to your normal account.

> [!NOTE]
> Your user account can use `sudo` because it belongs to the `sudo` group. You can verify this with the `groups` command. Not all user accounts have this privilege — service accounts like `www-data` cannot use `sudo`.

<br>

## 7. Key Terms

| Term | Definition |
|---|---|
| **User (owner)** | The account that owns a file; the first name in `ls -l` output |
| **Group** | A collection of user accounts that share permissions on files |
| **Service account** | A non-human user account created for a specific program to run under |
| **root** | The superuser account with unrestricted access to the entire system |
| **Permission string** | The 10-character string (e.g., `-rwxr-xr--`) that encodes a file's access rules |
| **chmod** | Command to change the permissions on a file or directory |
| **chown** | Command to change the user and/or group owner of a file or directory |
| **sudo** | Runs a single command with root privileges |
| **Least privilege** | The principle that users and programs should operate with only the minimum permissions necessary |

<br>

## Exercise: Permissions Puzzle

In this exercise, you will create a small directory structure and configure its permissions to meet specific requirements. Work on your Lubuntu machine.

### Setup

Run the following commands to create the exercise files:

```bash
mkdir -p ~/permissions-lab/public ~/permissions-lab/private ~/permissions-lab/shared
touch ~/permissions-lab/public/readme.txt
touch ~/permissions-lab/private/secrets.txt
touch ~/permissions-lab/shared/notes.txt
touch ~/permissions-lab/run-me.sh
echo '#!/bin/bash' > ~/permissions-lab/run-me.sh
echo 'echo "Hello from run-me.sh"' >> ~/permissions-lab/run-me.sh
```

### Tasks

For each task, record the command(s) you used and verify the result with `ls -l` or `ls -la`.

1. **Make `run-me.sh` executable.** Try running it first with `./run-me.sh` (from inside the `permissions-lab` directory). What error do you get? Fix it so you can run the script, and run it again.

2. **Make the `private/` directory accessible only to you.** No one else should be able to read, write, or enter it. Verify with `ls -l` that the permissions on the `private` directory show `rwx------`.

3. **Make `readme.txt` readable by everyone but only writable by you.** This is a common pattern for documentation files.

4. **Make the `shared/` directory readable and enterable by everyone, but only writable by you.** What numeric permission does this correspond to?

5. **Check who owns `run-me.sh`.** Now use `sudo chown root:root run-me.sh` to transfer ownership to root. Run `ls -l` to confirm. Can you still run it? Can you still edit it? Try both and explain what you observe.

6. **Take ownership back.** Use `chown` to make yourself the owner of `run-me.sh` again. What happens if you try without `sudo`?

7. **Investigate a system file.** Run `ls -l /etc/shadow`. What are the permissions? Who is the owner? Why do you think this file is so restricted? (Hint: research what `/etc/shadow` stores.)

8. **Clean up.** Remove the entire `permissions-lab` directory and everything inside it with a single command.
