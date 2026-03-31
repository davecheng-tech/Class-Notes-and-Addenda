# Scenario 5 — The Highscore Server Config

## Background

The RetroGames highscore server has a configuration file at `/etc/retrogames/highscores.conf`.

A `verify.sh` script is included in this folder. It checks whether the configuration is valid and reports what passes and what fails. Run it to see where you stand:

```
./verify.sh
```

Right now, everything fails.

## Your Goal

Get `./verify.sh` to report **all checks passed**.

---

## What You Know

- There are **three things wrong** with the setup.
- Not all of the problems are inside the file — some are about the file itself.
- `verify.sh` will tell you how many checks pass after each fix. Use it to track your progress.

---

## Your Job

Find all three problems. Fix them. Run `./verify.sh` after each fix.

---

## Hints

**Reading file metadata (permissions and ownership):**
```
ls -l /path/to/file
```

**Changing file ownership:**
```
sudo chown user:group /path/to/file
```
To give a file back to yourself: `sudo chown $USER:$USER /path/to/file`

**Changing file permissions:**
```
sudo chmod 644 /path/to/file
```
644 = owner can read/write, everyone else can read.

**Reading a config file:**
```
cat /etc/retrogames/highscores.conf
```

**Editing a config file:**
```
sudo nano /etc/retrogames/highscores.conf
```

**Checking whether a directory exists:**
```
ls /path/to/directory
```

**Creating a directory (and any missing parent directories):**
```
mkdir -p /path/to/directory
```
The `-p` flag creates parent directories automatically if they don't exist yet.
