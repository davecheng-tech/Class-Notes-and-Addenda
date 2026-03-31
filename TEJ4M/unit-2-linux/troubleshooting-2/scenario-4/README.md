# Scenario 4 — The Stats Script Won't Run

## Background

A script called `rg-stats` was installed on this machine to display session statistics for the RetroGames system. The previous admin says it's all set up and ready to use.

It is not ready to use.

## Your Goal

Get `rg-stats` to run and print the session stats summary.

---

## What You Know

- Running `rg-stats` in the terminal produces an error.
- The script is at `/usr/local/bin/rg-stats`.
- There may be more than one thing wrong — fix each problem and keep going.

---

## Your Job

Figure out what's wrong. Fix it. Get the stats to print.

You may hit more than one problem in sequence — each time you fix something, try running it again to see what's next.

---

## Hints

These are tools and concepts you may find useful. They're here if you get stuck — not as a recipe to follow.

**Checking a file's permissions and ownership:**
```
ls -l /path/to/file
```
Look at the permission string (e.g. `-rw-r--r--`) and the owner/group columns.

**Adding execute permission to a file:**
```
sudo chmod +x /path/to/file
```

**Changing who can read a file:**
```
sudo chmod 644 /path/to/file
```
644 = owner can read/write, everyone else can read.

**Running a script that is in your PATH:**
```
rg-stats
```
Note: run the script by name — do not call it with `bash rg-stats`. That bypasses the execute permission entirely and defeats the point of this exercise.
