# Terminal Reference

This document is a quick reference for UNIX command-line tools covered in the terminal tutorial. It applies to both Linux (Lubuntu) and macOS.

---

## Navigation

| Command | What it does |
|---------|-------------|
| `pwd` | Print working directory — shows where you are |
| `ls` | List files and folders in the current directory |
| `ls -l` | Long listing — shows permissions, size, date |
| `ls -a` | Show hidden files (names starting with `.`) |
| `ls -la` | Long listing including hidden files |
| `cd foldername` | Change into a folder |
| `cd ..` | Go up one level |
| `cd ~` | Go to your home directory |
| `cd /` | Go to the root of the filesystem |

A **path** describes a location in the filesystem:
- `/home/student/Documents` — absolute path (starts from root `/`)
- `Documents/notes` — relative path (starts from where you are)

---

## Files and Directories

| Command | What it does |
|---------|-------------|
| `mkdir foldername` | Create a new folder |
| `touch filename` | Create an empty file (or update its timestamp) |
| `cp source destination` | Copy a file |
| `cp -r source destination` | Copy a folder and its contents |
| `mv source destination` | Move or rename a file or folder |
| `rm filename` | Delete a file |
| `rm -r foldername` | Delete a folder and its contents |

`rm` is permanent — there is no recycle bin.

---

## Viewing File Contents

| Command | What it does |
|---------|-------------|
| `cat filename` | Print the entire file to the terminal |
| `less filename` | View a file one screen at a time (press `q` to quit) |
| `head filename` | Show the first 10 lines |
| `head -n 5 filename` | Show the first 5 lines |
| `tail filename` | Show the last 10 lines |
| `tail -n 5 filename` | Show the last 5 lines |

---

## Searching

### grep — Search file contents

```
grep "pattern" filename
```

| Flag | Effect |
|------|--------|
| `-i` | Case-insensitive search |
| `-r` | Search recursively inside a folder |
| `-n` | Show line numbers |

Example: `grep -rn "error" logs/` finds the word "error" in all files inside `logs/`, with line numbers.

### find — Search for files by name

```
find where -name "pattern"
```

Example: `find . -name "*.txt"` finds all `.txt` files starting from the current directory.

---

## Piping and Redirection

These operators connect commands together or control where output goes.

| Symbol | Meaning |
|--------|---------|
| `\|` | Pipe — send output of one command as input to another |
| `>` | Redirect output to a file (overwrites) |
| `>>` | Redirect output to a file (appends) |
| `<` | Use a file as input to a command |

Examples:

```bash
ls -l | less              # scroll through a long listing
cat file.txt | grep "hi"  # search within a file
ls > filelist.txt         # save directory listing to a file
echo "new line" >> notes.txt  # append to a file
```

### Useful commands to combine with pipes

| Command | What it does |
|---------|-------------|
| `sort` | Sort lines alphabetically |
| `sort -n` | Sort numerically |
| `sort -r` | Reverse order |
| `wc -l` | Count lines |
| `wc -w` | Count words |
| `uniq` | Remove consecutive duplicate lines (use after `sort`) |

---

## Permissions

Run `ls -l` to see permissions. The permission string looks like this:

```
-rwxr-xr--  1  student  staff  1024  Jan 10  file.sh
```

The first 10 characters break down as:

```
- rwx r-x r--
│ │   │   └── others: read only
│ │   └────── group: read and execute
│ └────────── owner: read, write, execute
└──────────── type: - (file), d (directory), l (symlink)
```

Each group of 3 characters uses `r` (read), `w` (write), `x` (execute), or `-` (no permission).

### chmod — Change permissions

```
chmod permissions filename
```

Numeric mode is most common:

| Number | Permissions |
|--------|-------------|
| `7` | rwx |
| `6` | rw- |
| `5` | r-x |
| `4` | r-- |
| `0` | --- |

Three digits set permissions for owner, group, and others in that order.

Examples:
```bash
chmod 755 script.sh   # owner: rwx, group: r-x, others: r-x
chmod 644 notes.txt   # owner: rw-, group: r--, others: r--
chmod +x script.sh    # add execute permission for everyone
```

---

## Processes

| Command | What it does |
|---------|-------------|
| `ps` | List your running processes |
| `ps aux` | List all processes from all users |
| `top` | Live view of processes and resource usage (press `q` to quit) |
| `kill PID` | Send a termination signal to a process by its ID |
| `kill -9 PID` | Force-kill a process immediately |

The **PID** (Process ID) appears in the first column of `ps` or `top` output.

---

## Getting Help

| Command | What it does |
|---------|-------------|
| `man command` | Open the manual page for a command (press `q` to quit) |
| `command --help` | Print a short usage summary |

Example: `man ls` explains every option available for `ls`.
