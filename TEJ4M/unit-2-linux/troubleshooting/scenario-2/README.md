# Scenario 2 — Something Is Wrong With This Machine

## Background

A classmate complains that this machine has been acting strangely — sluggish, fan running, generally not right. They don't know what's causing it. You sit down to investigate.

## Your Goal

1. Identify the rogue process(es) responsible.
2. Confirm they are the source of the problem using the log file at `/var/log/retro-monitor.log`.
3. Stop them — permanently. They should not come back.

---

## What You Know

- One or more unexpected processes are running.
- There is a log file at `/var/log/retro-monitor.log`.
- Killing a process once may not be enough.

---

## Your Job

Diagnose what's running and why. Then stop it cleanly and verify it's gone.

---

## Hints

**Seeing all running processes:**
```
ps aux
```
Look for process names you don't recognise.

**Seeing parent-child relationships between processes:**
```
ps aux --forest
```
or
```
pstree -p
```
This shows which processes spawned which. If a child keeps coming back, ask yourself: what's the parent doing?

**Searching a log file:**
```
grep "pattern" /var/log/retro-monitor.log
```
Useful patterns to try: `ERROR`, `MONITOR`, `WORKER`.

**Signals:**
`kill <pid>` sends **SIGTERM** — a polite request to stop. Processes can choose to ignore this.

`kill -9 <pid>` sends **SIGKILL** — forced, immediate termination. Cannot be ignored or caught.

**Verifying a process is gone:**
```
ps aux | grep processname
```
