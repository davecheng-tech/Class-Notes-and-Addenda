# Scenario 6 — The Media Server

## Background

A script called `rg-media` is supposed to start the RetroGames media server. It reads a configuration file and reports its status. Someone set it up, but they may have made a few mistakes along the way.

A `verify.sh` script is included in this folder. Run it to see where you stand:

```
./verify.sh
```

## Your Goal

Get `./verify.sh` to report **all checks passed**, then confirm the media server starts:

```
rg-media
```

---

## What You Know

- There are **three things wrong** with the setup.
- The problems involve the script itself, its configuration file, and the configuration file's contents.
- Use `verify.sh` to track your progress after each fix.

---

## Your Job

Investigate. Fix each problem. Run `./verify.sh` after each change.

---

## Hints

These are tools and concepts that may help. They're here if you get stuck — not as a step-by-step guide.

**Reading what a script is looking for:**
```
cat /usr/local/bin/rg-media
```
Scripts are just text files. Reading the script itself tells you exactly what paths and files it expects to find.

**Listing the contents of a directory:**
```
ls /etc/retrogames/
```
If a file isn't where a program expects it, it may exist nearby under a different name.

**Copying a file to a new location or name:**
```
sudo cp /path/to/source /path/to/destination
```

**Creating a directory and any missing parent directories:**
```
sudo mkdir -p /path/to/deeply/nested/directory
```
Without `-p`, `mkdir` fails if any parent directory in the path does not already exist.
