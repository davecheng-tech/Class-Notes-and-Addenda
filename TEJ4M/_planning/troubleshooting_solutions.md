# Solution Guide — Troubleshooting Exercise

## Setup Reminder

Run on each machine to set up the environment for this exercise:
```bash
sudo bash setup.sh
```

To reset at end of class:
```bash
sudo bash teardown.sh
```

---
<br>

## Scenario 1 — The Launcher Won't Run

### What Was Broken

| Problem | Location | Description |
|---------|----------|-------------|
| 1 | `/usr/local/bin/launcher` | No execute permission |
| 2 | `/usr/local/bin/launcher` | ARM64 binary — wrong architecture for this x86_64 machine |
| 3 | `/opt/retrogames/launcher` | Correct binary, but also no execute permission and not in PATH |

### Step-by-Step Solution

**Step 1 — Try running it.**
```bash
launcher
```
```
bash: launcher: command not found
```
Not in PATH. Need to find it.

**Step 2 — Find it.**
```bash
find / -name launcher 2>/dev/null
```
```
/usr/local/bin/launcher
/opt/retrogames/launcher
```
Two results. Start with the one in a PATH directory.

**Step 3 — Try running by full path.**
```bash
/usr/local/bin/launcher
```
```
bash: /usr/local/bin/launcher: Permission denied
```
No execute bit.

**Step 4 — Check permissions.**
```bash
ls -l /usr/local/bin/launcher
```
```
-rw-r--r-- 1 root root 120 Mar 30 08:00 /usr/local/bin/launcher
```
No `x` anywhere. Fix it.

**Step 5 — Add execute permission.**
```bash
sudo chmod +x /usr/local/bin/launcher
launcher
```
```
bash: /usr/local/bin/launcher: cannot execute binary file: Exec format error
```
Different error. It's executable, but the machine can't run it.

**Step 6 — Inspect the binary.**
```bash
file /usr/local/bin/launcher
```
```
/usr/local/bin/launcher: ELF 64-bit LSB executable, ARM aarch64
```
ARM binary. Check our machine.

**Step 7 — Check our architecture.**
```bash
lscpu | grep Architecture
```
```
Architecture: x86_64
```
x86_64 ≠ aarch64. This binary cannot run here.

> **Important:** This is exactly the architecture problem from Period 1 — ISAs (or Instruction Set Architectures) are not cross-compatible. A binary compiled for ARM has instructions the x86 CPU doesn't understand. This is also why emulation exists: to bridge this gap in software.

**Step 8 — Try the other launcher.**
```bash
file /opt/retrogames/launcher
```
```
/opt/retrogames/launcher: ELF 64-bit LSB executable, x86-64
```
x86_64 binary — matches this machine. This is the one.

**Step 9 — Fix its permissions and run it.**
```bash
chmod +x /opt/retrogames/launcher
/opt/retrogames/launcher
```
```
RetroGames Launcher v1.0
Architecture: x86_64
System ready. Load a ROM to begin.
```

**Step 10 (Extension) — Add to PATH permanently.**
```bash
export PATH=$PATH:/opt/retrogames
launcher
```

---
<br>

## Scenario 2 — Something Is Wrong With This Machine

### What Was Broken

| Process | Description |
|---------|-------------|
| `retro-monitord` (parent) | Ignores SIGTERM. Monitors child worker and respawns it if killed. |
| `worker.sh` (child) | Runs indefinitely, writes to log. Respawns when killed (until parent is dead). |

### Step-by-Step Solution

**Step 1 — Look for suspicious processes.**
```bash
ps aux
```
Look for unfamiliar names. Should see something like:
```
student   2241  0.0  ...  bash /usr/local/lib/retrogames/monitord.sh
student   2244  0.0  ...  bash /usr/local/lib/retrogames/worker.sh
```

**Step 2 — See the parent-child relationship.**
```bash
ps aux --forest
```
```
student   2241  ...  \_ bash .../monitord.sh
student   2244  ...       \_ bash .../worker.sh
```
The worker is a child of the monitor. This matters.

**Step 3 — Check the log to confirm.**
```bash
grep ERROR /var/log/retro-monitor.log
```
```
2026-03-25 09:12:07 [ERROR] rom directory not found — retrying indefinitely
2026-03-25 09:12:10 [ERROR] rom directory not found — retrying indefinitely
```
Confirmed: this process is malfunctioning and won't stop on its own.

**Step 4 — Try killing the worker.**
```bash
kill 2244
```
Wait a few seconds, then:
```bash
ps aux | grep retro
```
```
student   2241  ...  bash .../monitord.sh
student   2251  ...  bash .../worker.sh   ← new PID — it came back
```
Worker respawned. The parent is keeping it alive.

> **Important:** This is why process trees matter. Killing a child process only works if nothing is watching it. In real sysadmin work, services and daemons almost always have a parent that manages them — this is why `systemctl stop` exists instead of just `kill`.

**Step 5 — Try killing the parent with SIGTERM.**
```bash
kill 2241
ps aux | grep retro
```
Still running. The monitor is ignoring SIGTERM.

**Step 6 — Use SIGKILL on the parent.**
```bash
kill -9 2241
ps aux | grep retro
```
```
student   2251  ...  bash .../worker.sh
```
Parent is gone, but the worker is now an orphan — still running.

**Step 7 — Kill the orphaned worker.**
```bash
kill -9 2251
```
or by name:
```bash
pkill -9 -f worker.sh
```

**Step 8 — Verify everything is gone.**
```bash
ps aux | grep retro
```
No results (except the grep itself).

---
<br>

## Scenario 3 — The Service Won't Start

### What Was Broken

| # | Problem | Fix |
|---|---------|-----|
| 1 | `/etc/retrogames/retrogames.conf` owned by root, permissions 600 — student cannot read it | `sudo chmod 644 /etc/retrogames/retrogames.conf` |
| 2 | `log_level=DEBG` — typo, not a valid log level | Edit to `DEBUG` or `INFO` |
| 3 | `rom_path=~/roms` — directory does not exist | `mkdir ~/roms` |

### Step-by-Step Solution

**Step 1 — Run verify.sh. Everything fails.**
```bash
./verify.sh
```
```
  [FAIL] Config file is readable by current user  →  Hint: check ownership and permissions with ls -l
  [FAIL] log_level is a valid value (DEBUG / INFO / WARNING / ERROR)
  [FAIL] rom_path directory exists
```
Three failures. Start with the first.

**Step 2 — Try to read the config.**
```bash
cat /etc/retrogames/retrogames.conf
```
```
cat: /etc/retrogames/retrogames.conf: Permission denied
```

**Step 3 — Check why.**
```bash
ls -l /etc/retrogames/retrogames.conf
```
```
-rw------- 1 root root 104 Mar 30 08:00 /etc/retrogames/retrogames.conf
```
Root owns it, permissions `600` — only root can read. Fix it.

**Step 4 — Fix permissions.**
```bash
sudo chmod 644 /etc/retrogames/retrogames.conf
./verify.sh
```
```
  [PASS] Config file is readable by current user
  [FAIL] log_level is a valid value  →  Current value: 'DEBG'
  [FAIL] rom_path directory exists
```
One down.

> **Important:** We could also have used `sudo chown $USER /etc/retrogames/retrogames.conf` — that would transfer ownership instead of opening up permissions. In a real system, which approach you choose matters for security. Here, `chmod 644` is fine.

**Step 5 — Read the config file.**
```bash
cat /etc/retrogames/retrogames.conf
```
```
# RetroGames Configuration
data_dir=/opt/retrogames/data
log_level=DEBG
max_players=4
rom_path=/home/student/roms
```

**Step 6 — Fix the log level.**
```bash
sudo nano /etc/retrogames/retrogames.conf
```
Change `DEBG` → `DEBUG` (or `INFO`). Save and exit.

```bash
./verify.sh
```
```
  [PASS] Config file is readable by current user
  [PASS] log_level is a valid value
  [FAIL] rom_path directory exists  →  Looking for: '/home/student/roms'
```

**Step 7 — Fix the missing directory.**
```bash
ls ~/roms
```
```
ls: cannot access '/home/student/roms': No such file or directory
```
Doesn't exist. Create it.
```bash
mkdir ~/roms
./verify.sh
```
```
  [PASS] Config file is readable by current user
  [PASS] log_level is a valid value
  [PASS] rom_path directory exists (/home/student/roms)

  All 3 checks passed. Configuration is valid.
```

---
<br>

## Common Mistakes

| Scenario | Mistake | Clarification |
|----------|---------|---------------|
| 1 | Running `chmod +x launcher` without the full path, then still getting "not found" | PATH still doesn't include `/opt/retrogames` — must run by full path or add to PATH |
| 1 | Confused by `Exec format error` — thinks it's still a permissions issue | Permissions are fine now; the binary literally speaks a different instruction set |
| 2 | Kill worker, don't check again, declare success | Have them run `ps aux \| grep retro` to verify — parent respawned it |
| 2 | Kill parent with SIGTERM, see nothing happen, assume it worked | Check `ps` — process is still there |
| 2 | Kill parent with SIGKILL, forget about orphaned worker | Worker is still running — check and kill it |
| 3 | Try to edit config without sudo after making it readable | They own read permission but still need sudo/root to write |
| 3 | Create `roms` directory in wrong location | Path in config is absolute — must match exactly |

---
<br>

---
<br>

# Part 2 — Solution Guide (Scenarios 4–6)

## Setup Reminder

Run on each machine to set up exercise 2:
```bash
sudo bash troubleshooting-2/setup.sh
```

To reset at end of class:
```bash
sudo bash troubleshooting-2/teardown.sh
```

Both scripts are independent of the original exercise — safe to run in any order.

---
<br>

## Scenario 4 — The Stats Script Won't Run

### What Was Broken

| Problem | Location | Description |
|---------|----------|-------------|
| 1 | `/usr/local/bin/rg-stats` | No execute permission (chmod 644) |
| 2 | `/var/log/retrogames-stats.log` | chmod 600, owned by root — student cannot read it |

### Step-by-Step Solution

**Step 1 — Try running it.**
```bash
rg-stats
```
```
bash: rg-stats: Permission denied
```
The script is in PATH (it's in `/usr/local/bin/`) but has no execute bit.

**Step 2 — Confirm with ls -l.**
```bash
ls -l /usr/local/bin/rg-stats
```
```
-rw-r--r-- 1 root root 312 Mar 31 08:00 /usr/local/bin/rg-stats
```
`rw-r--r--` — no `x` anywhere. Fix it.

**Step 3 — Add execute permission.**
```bash
sudo chmod +x /usr/local/bin/rg-stats
rg-stats
```
```
ERROR: Cannot read stats log at /var/log/retrogames-stats.log
       Check file permissions.
```
Different error — the script runs now, but can't read the log file.

> **Key teaching point:** A program's own permissions are not the only thing that matters. When a program tries to *read a file*, that file's permissions also apply. This is the same reason a web server needs read access to the files it serves.

**Step 4 — Check the log file's permissions.**
```bash
ls -l /var/log/retrogames-stats.log
```
```
-rw------- 1 root root 310 Mar 31 08:00 /var/log/retrogames-stats.log
```
Root owns it, permissions `600` — no one else can read it. Fix it.

**Step 5 — Fix the log file permissions.**
```bash
sudo chmod 644 /var/log/retrogames-stats.log
rg-stats
```
```
=== RetroGames Session Statistics ===

Recent sessions:
  2026-03-30 14:01:05 [SESSION] player=kanzaki game=galaga score=12400 duration=8m
  2026-03-30 14:09:22 [SESSION] player=morrow game=pacman score=8800 duration=5m
  2026-03-30 14:15:03 [SESSION] player=kanzaki game=centipede score=21600 duration=12m
  2026-03-30 14:27:44 [SESSION] player=wu game=galaga score=9100 duration=6m
  2026-03-30 14:33:59 [SESSION] player=morrow game=centipede score=15200 duration=9m

Total sessions logged: 5
```

---
<br>

## Scenario 5 — The Highscore Server Config

### What Was Broken

| # | Problem | Fix |
|---|---------|-----|
| 1 | `/etc/retrogames/highscores.conf` owned by root, chmod 600 — not readable | `sudo chmod 644 /etc/retrogames/highscores.conf` |
| 2 | `max_entries=one-hundred` — not a number | Edit to a valid integer, e.g. `100` |
| 3 | `data_dir=/opt/retrogames/scores` — directory does not exist | `mkdir -p /opt/retrogames/scores` |

### Step-by-Step Solution

**Step 1 — Run verify.sh. Everything fails.**
```bash
./verify.sh
```
```
  [FAIL] Config file is readable by current user  →  Hint: check ownership and permissions with ls -l
  [FAIL] max_entries is a valid number (e.g. 100)  →  Current value: 'not found'
  [FAIL] data_dir directory exists  →  Looking for: 'not found in config'
```
The cascading failures on Checks 2 and 3 happen because the file can't be read yet — the values aren't missing, they just can't be read. Fix Check 1 first.

**Step 2 — Check the config file's permissions.**
```bash
ls -l /etc/retrogames/highscores.conf
```
```
-rw------- 1 root root 104 Mar 31 08:00 /etc/retrogames/highscores.conf
```
Root owns it, `600`. Fix it.

**Step 3 — Fix permissions.**
```bash
sudo chmod 644 /etc/retrogames/highscores.conf
./verify.sh
```
```
  [PASS] Config file is readable by current user
  [FAIL] max_entries is a valid number (e.g. 100)  →  Current value: 'one-hundred'
  [FAIL] data_dir directory exists  →  Looking for: '/opt/retrogames/scores'
```
One down. Now the real values are visible.

**Step 4 — Read and fix the config.**
```bash
cat /etc/retrogames/highscores.conf
```
```
# RetroGames Highscore Server Configuration
max_entries=one-hundred
data_dir=/opt/retrogames/scores
leaderboard_name=RetroGames Hall of Fame
```
`max_entries=one-hundred` — a string where a number is expected.

```bash
sudo nano /etc/retrogames/highscores.conf
```
Change `one-hundred` → `100`. Save and exit.

```bash
./verify.sh
```
```
  [PASS] Config file is readable by current user
  [PASS] max_entries is a valid number (e.g. 100)
  [FAIL] data_dir directory exists  →  Looking for: '/opt/retrogames/scores'
```

**Step 5 — Create the missing directory.**
```bash
ls /opt/retrogames/scores
```
```
ls: cannot access '/opt/retrogames/scores': No such file or directory
```
Doesn't exist. Create it. Note: `/opt/retrogames/` may also not exist, so use `-p`:
```bash
mkdir -p /opt/retrogames/scores
./verify.sh
```
```
  [PASS] Config file is readable by current user
  [PASS] max_entries is a valid number (e.g. 100)
  [PASS] data_dir directory exists (/opt/retrogames/scores)

  All 3 checks passed. Configuration is valid.
```

---
<br>

## Scenario 6 — The Media Server

### What Was Broken

| # | Problem | Fix |
|---|---------|-----|
| 1 | `/usr/local/bin/rg-media` has no execute permission (chmod 644) | `sudo chmod +x /usr/local/bin/rg-media` |
| 2 | Config placed at `/etc/retrogames/media.conf.bak` — script expects `/etc/retrogames/media.conf` | `sudo cp /etc/retrogames/media.conf.bak /etc/retrogames/media.conf` |
| 3 | `stream_dir=/var/lib/retrogames/streams` — directory does not exist | `sudo mkdir -p /var/lib/retrogames/streams` |

### Step-by-Step Solution

**Step 1 — Run verify.sh.**
```bash
./verify.sh
```
```
  [FAIL] rg-media script is executable  →  Hint: check permissions with ls -l /usr/local/bin/rg-media
  [FAIL] Config file exists and is readable at /etc/retrogames/media.conf  →  Hint: look at what is actually in /etc/retrogames/
  [FAIL] stream_dir directory exists  →  Check config path first: is the config file in the right place?
```

**Step 2 — Fix execute permission.**
```bash
ls -l /usr/local/bin/rg-media
```
```
-rw-r--r-- 1 root root 512 Mar 31 08:00 /usr/local/bin/rg-media
```
```bash
sudo chmod +x /usr/local/bin/rg-media
./verify.sh
```
```
  [PASS] rg-media script is executable
  [FAIL] Config file exists and is readable at /etc/retrogames/media.conf
  [FAIL] stream_dir directory exists  →  Check config path first: is the config file in the right place?
```

**Step 3 — Investigate the config.**
The script expects `/etc/retrogames/media.conf`. Let's see what's actually there:
```bash
ls /etc/retrogames/
```
```
media.conf.bak   retrogames.conf   highscores.conf
```
`media.conf.bak` — the file is there but named incorrectly. Copy it to the expected path:
```bash
sudo cp /etc/retrogames/media.conf.bak /etc/retrogames/media.conf
./verify.sh
```
```
  [PASS] rg-media script is executable
  [PASS] Config file exists and is readable at /etc/retrogames/media.conf
  [FAIL] stream_dir directory exists  →  Looking for: '/var/lib/retrogames/streams'
```

**Step 4 — Read the script to understand what it needs (optional teaching moment).**
```bash
cat /usr/local/bin/rg-media
```
Reading the script shows exactly what path it is looking for in `stream_dir`. This is a key troubleshooting instinct: when a program can't find something, read the program.

**Step 5 — Create the missing directory.**
```bash
sudo mkdir -p /var/lib/retrogames/streams
./verify.sh
```
```
  [PASS] rg-media script is executable
  [PASS] Config file exists and is readable at /etc/retrogames/media.conf
  [PASS] stream_dir directory exists (/var/lib/retrogames/streams)

  All 3 checks passed.
  Now run: rg-media
```

**Step 6 — Run the media server.**
```bash
rg-media
```
```
RetroGames Media Server
Stream directory: /var/lib/retrogames/streams
Max connections:  10
Status: ready
```

---
<br>

## Common Mistakes — Part 2

| Scenario | Mistake | Clarification |
|----------|---------|---------------|
| 4 | Run `bash rg-stats` after seeing "Permission denied" — it works, student thinks they're done | `bash rg-stats` bypasses the execute bit — the problem is still there; always run by name |
| 4 | Fix execute bit, see a new error, think they made it worse | A new error means progress — the first problem is solved, and a second one is now visible |
| 5 | Try to edit config immediately without fixing permissions first | `nano` needs read access to open it — fix permissions first |
| 5 | Use `mkdir /opt/retrogames/scores` without `-p` on a fresh machine | Parent directory may not exist — `-p` handles this |
| 6 | Try to `mv` or `cp` the `.bak` file without `sudo` | `/etc/retrogames/` is root-owned — need sudo to write to it |
| 6 | Copy the file but forget the destination filename | `sudo cp media.conf.bak media.conf.bak` leaves the problem unsolved — destination name matters |
