# Teacher Solution Guide — Troubleshooting Exercise

**Course:** TEJ4M | **Unit:** 2 — Linux | **Period:** 6

Use this to take up each scenario after students have worked through them.
Project and walk through the commands live in the terminal.

---

## Setup Reminder

Run on each student machine before class (or have students run it themselves):
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

> **Teaching moment:** This is exactly the architecture problem from Period 1 — ISAs are not cross-compatible. A binary compiled for ARM has instructions the x86 CPU doesn't understand. This is also why emulation exists: to bridge this gap in software.

**Step 8 — Try the other launcher.**
```bash
file /opt/retrogames/launcher
```
```
/opt/retrogames/launcher: Bourne-Again shell script, ASCII text executable
```
Shell script — architecture-independent. This is the one.

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

> **Teaching moment:** This is why process trees matter. Killing a child process only works if nothing is watching it. In real sysadmin work, services and daemons almost always have a parent that manages them — this is why `systemctl stop` exists instead of just `kill`.

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
bash verify.sh
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
bash verify.sh
```
```
  [PASS] Config file is readable by current user
  [FAIL] log_level is a valid value  →  Current value: 'DEBG'
  [FAIL] rom_path directory exists
```
One down.

> **Teaching moment:** We could also have used `sudo chown $USER /etc/retrogames/retrogames.conf` — that would transfer ownership instead of opening up permissions. In a real system, which approach you choose matters for security. Here, `chmod 644` is fine.

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
bash verify.sh
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
bash verify.sh
```
```
  [PASS] Config file is readable by current user
  [PASS] log_level is a valid value
  [PASS] rom_path directory exists (/home/student/roms)

  All 3 checks passed. Configuration is valid.
```

---
<br>

## Common Student Mistakes to Watch For

| Scenario | Mistake | Clarification |
|----------|---------|---------------|
| 1 | Running `chmod +x launcher` without the full path, then still getting "not found" | PATH still doesn't include `/opt/retrogames` — must run by full path or add to PATH |
| 1 | Confused by `Exec format error` — thinks it's still a permissions issue | Permissions are fine now; the binary literally speaks a different instruction set |
| 2 | Kill worker, don't check again, declare success | Have them run `ps aux \| grep retro` to verify — parent respawned it |
| 2 | Kill parent with SIGTERM, see nothing happen, assume it worked | Check `ps` — process is still there |
| 2 | Kill parent with SIGKILL, forget about orphaned worker | Worker is still running — check and kill it |
| 3 | Try to edit config without sudo after making it readable | They own read permission but still need sudo/root to write |
| 3 | Create `roms` directory in wrong location | Path in config is absolute — must match exactly |
