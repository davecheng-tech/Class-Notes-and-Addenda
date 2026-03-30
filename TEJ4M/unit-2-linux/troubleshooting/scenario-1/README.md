# Scenario 1 — The Launcher Won't Run

## Background

Someone set up a RetroGames launcher on this machine before you arrived. They said it's installed and ready to go.

It is not ready to go.

## Your Goal

Get the launcher running so it prints its startup message.

---

## What You Know

- Running `launcher` in the terminal produces an error (or nothing at all).
- The launcher binary was placed somewhere on this system.
- There may be more than one file called `launcher` — not all of them will work.

---

## Your Job

Figure out what's wrong. Fix it. Get the launcher to run.

You may hit more than one problem in sequence — fix each one and keep going.

---

## Hints

These are tools and concepts you may not have seen before. They're here if you get stuck — not as a recipe to follow.

**Finding a file anywhere on the system:**
```bash
find / -name filename 2>/dev/null
```
The `2>/dev/null` suppresses permission-denied errors so you can read the results.
Common locations for installed software: `/usr/local/bin`, `/opt`.

**The `file` command:**
When a program fails with an unfamiliar error, `file` tells you what kind of file it actually is — its format and target architecture:
```bash
file /path/to/somefile
```
An executable built for one CPU architecture cannot run on another.

**Checking your machine's architecture:**
```bash
lscpu | grep Architecture
```

**Running a file that isn't in your PATH:**
```bash
/full/path/to/file
```
