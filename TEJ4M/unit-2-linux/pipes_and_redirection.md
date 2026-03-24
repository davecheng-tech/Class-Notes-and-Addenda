# Pipes and Redirection

This note covers how Linux commands communicate with each other. It explains:

- Standard streams: where command input and output go
- Redirection: sending output to files instead of the screen
- Pipes: connecting the output of one command to the input of another
- `grep`: searching for patterns in text
- Combining tools to answer questions about your system

<br>

## 1. Standard Streams

Every command you run in the terminal has three connections to the outside world. These are called **standard streams**:

| Stream | Name | Default destination | Description |
|---|---|---|---|
| `stdin` | Standard input | Keyboard | Where the command reads input from |
| `stdout` | Standard output | Terminal screen | Where the command sends its normal output |
| `stderr` | Standard error | Terminal screen | Where the command sends error messages |

When you run `ls`, it reads nothing from stdin, sends the file listing to stdout (which appears on your screen), and sends any errors to stderr (also your screen).

By default, stdout and stderr both appear on the same terminal, so they look the same. But they are separate streams, and Linux lets you redirect each one independently.

Understanding these three streams is the key to everything in this note. Redirection and pipes work by rerouting these streams — sending stdout somewhere other than the screen, or feeding one command's stdout into another command's stdin.

<br>

## 2. Redirection: Commands and Files

Redirection lets you send command output to a file instead of the screen, or read input from a file instead of the keyboard.

### `>` — Write Output to a File (Overwrite)

```bash
ls /etc > filelist.txt
```

This runs `ls /etc` but instead of printing the result to the terminal, it writes it to `filelist.txt`. If the file already exists, it is **overwritten** — the previous contents are gone.

### `>>` — Append Output to a File

```bash
echo "Scan completed" >> log.txt
```

This adds a line to `log.txt` without erasing what was already there. Use `>>` when you want to accumulate data in a file over time.

### `<` — Read Input from a File

```bash
wc -l < /etc/passwd
```

This feeds the contents of `/etc/passwd` into the `wc -l` command as input. The result is the number of lines in the file.

> [!IMPORTANT]
> `>` is destructive. If you accidentally run `> important_file.txt` (redirect nothing into a file), it will erase the file's contents. Be careful with this operator.

### `2>` — Redirect Error Messages

Sometimes you want to discard error messages or send them to a separate file:

```bash
ls /nonexistent 2> errors.txt
```

This sends the error message ("No such file or directory") to `errors.txt` instead of the screen. The `2` refers to stderr (stream number 2).

A common pattern is to discard errors entirely:

```bash
find / -name "*.conf" 2> /dev/null
```

This searches the entire filesystem for `.conf` files and discards any "Permission denied" errors by sending them to `/dev/null` — the black hole from the filesystem hierarchy note.

### Summary of Redirection Operators

| Operator | Effect |
|---|---|
| `>` | Redirect stdout to a file (overwrite) |
| `>>` | Redirect stdout to a file (append) |
| `<` | Redirect stdin from a file |
| `2>` | Redirect stderr to a file |
| `2>/dev/null` | Discard error messages |

<br>

## 3. Pipes: Connecting Commands

A **pipe** (`|`) connects the stdout of one command to the stdin of the next command. This lets you chain tools together, where each tool does one small job and passes the result along.

```bash
ps aux | grep ssh
```

This does two things in sequence:

1. `ps aux` produces a list of all running processes (stdout)
2. `|` sends that output into `grep ssh` (stdin)
3. `grep ssh` filters the list to only show lines containing "ssh"

Without the pipe, you would have to save the output to a file and then search the file — two separate steps. The pipe makes it one.

### Chaining Multiple Pipes

You can chain as many commands as you need:

```bash
ps aux | grep ssh | wc -l
```

This counts how many lines in the process list contain "ssh". Three commands, connected by two pipes, each doing one job.

### Why Pipes Matter

Pipes are the core design philosophy of the Linux command line. Instead of building one giant tool that does everything, Linux provides many small tools that each do one thing well. Pipes are the glue that connects them.

This is sometimes called the **Unix philosophy**: *Write programs that do one thing and do it well. Write programs to work together.*

You have already used pipes several times in this unit:

| Command | What it does |
|---|---|
| `ps aux \| grep ssh` | Find SSH-related processes |
| `ls /usr/bin \| wc -l` | Count programs in /usr/bin |
| `sudo ss -ltnp \| grep :22` | Find what is listening on port 22 |

Each of these combines two simple tools into something more powerful than either one alone.

<br>

## 4. `grep`: Searching for Patterns

`grep` is one of the most important tools to combine with pipes. It searches text for lines that match a pattern and prints only those lines.

### Basic Usage

```bash
grep "error" /var/log/syslog
```

This searches the file `/var/log/syslog` for lines containing the word "error" and prints them.

### Common Flags

| Flag | Effect | Example |
|---|---|---|
| `-i` | Case-insensitive search | `grep -i "error" log.txt` matches "Error", "ERROR", "error" |
| `-n` | Show line numbers | `grep -n "port" /etc/ssh/sshd_config` |
| `-r` | Search recursively in a directory | `grep -r "listen" /etc/nginx/` |
| `-c` | Count matching lines (instead of printing them) | `grep -c "failed" /var/log/auth.log` |
| `-v` | Invert: show lines that do NOT match | `grep -v "^#" /etc/ssh/sshd_config` |

### `grep -v` and Filtering Comments

Configuration files in `/etc` are often full of comment lines (starting with `#`). To see only the active, uncommented lines:

```bash
grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"
```

This chains two `grep -v` commands:
1. Remove lines starting with `#` (comments)
2. Remove blank lines (`^$`)

The result is only the lines that actually configure the service.

> [!NOTE]
> The `^` symbol means "start of line" in grep patterns. `^#` matches lines that begin with `#`, and `^$` matches completely empty lines. These are basic **regular expressions** — a pattern language used by many tools. You do not need to master regular expressions for this course, but recognizing `^` (start) and `$` (end) is useful.

### `grep` with Pipes

`grep` is most powerful when combined with pipes. It acts as a filter, reducing a large amount of output to only the lines you care about:

```bash
sudo dmesg | grep -i wifi
```

This searches the kernel message log for anything related to Wi-Fi. Without `grep`, `dmesg` would dump hundreds of lines to the screen. (`dmesg` requires `sudo` on Lubuntu.)

<br>

## 5. Other Useful Tools for Pipes

These commands are designed to work in pipelines. Each one does a small, specific job.

### `wc` — Count Things

| Command | What it counts |
|---|---|
| `wc -l` | Lines |
| `wc -w` | Words |
| `wc -c` | Bytes (characters) |

```bash
cat /etc/passwd | wc -l        # how many user accounts exist?
```

### `sort` — Sort Lines

```bash
du -h /var/log/* 2>/dev/null | sort -h
```

This lists the size of each file in `/var/log/`, then sorts them by human-readable size (smallest to largest). The `2>/dev/null` discards errors from directories you cannot read.

| Flag | Effect |
|---|---|
| (none) | Sort alphabetically |
| `-n` | Sort numerically |
| `-r` | Reverse order |
| `-h` | Sort human-readable sizes (K, M, G) |

### `head` and `tail` — First or Last Lines

```bash
ps aux | head -5          # first 5 lines (includes the header)
cat /var/log/syslog | tail -20    # last 20 lines (most recent log entries)
```

### `uniq` — Remove Consecutive Duplicates

`uniq` removes duplicate adjacent lines. It is almost always used after `sort`:

```bash
cat /var/log/auth.log | grep "Failed" | sort | uniq -c | sort -rn
```

This finds failed login attempts, sorts them, counts duplicates, and sorts by frequency — most common failures first.

### `cut` — Extract Columns

```bash
cat /etc/passwd | cut -d: -f1
```

This extracts just the first field (username) from each line of `/etc/passwd`, using `:` as the delimiter. The password file uses colons to separate fields, and `cut` lets you pull out just the column you need.

<br>

## 6. Putting It All Together

The real power of pipes and redirection comes from combining them. Here are some practical examples that use the skills from this entire unit.

### How many user accounts exist on this system?

```bash
wc -l < /etc/passwd
```

### What services are listening on the network?

```bash
sudo ss -ltnp | grep LISTEN
```

### What are the 5 largest files in /var/log?

```bash
du -h /var/log/* 2>/dev/null | sort -rh | head -5
```

### What processes is my user account running?

```bash
ps aux | grep "^$(whoami)"
```

### Save a system snapshot to a file

```bash
echo "=== Date ===" > snapshot.txt
date >> snapshot.txt
echo "=== Disk ===" >> snapshot.txt
df -h / >> snapshot.txt
echo "=== Memory ===" >> snapshot.txt
free -h >> snapshot.txt
echo "=== Listening Ports ===" >> snapshot.txt
sudo ss -ltnp >> snapshot.txt
```

This builds a file piece by piece using `>>` (append). The first line uses `>` (overwrite) to start fresh.

<br>

## 7. Key Terms

| Term | Definition |
|---|---|
| **stdin** | Standard input — the default input stream (keyboard) |
| **stdout** | Standard output — the default output stream (terminal screen) |
| **stderr** | Standard error — the stream for error messages (also terminal screen by default) |
| **Redirection** | Sending a stream to or from a file instead of its default destination |
| **Pipe (`\|`)** | Connects the stdout of one command to the stdin of the next |
| **grep** | A tool that filters text, printing only lines matching a pattern |
| **Regular expression** | A pattern language for matching text (e.g., `^#` matches lines starting with `#`) |
| **Unix philosophy** | The design principle of small, focused tools that work together through pipes |

<br>

## Exercise: Pipeline Challenges

Solve each challenge using a single command line (one or more commands connected with pipes and/or redirection). Record your command and the output.

### Warm-Up

1. List all files in `/etc` and count how many there are. (Hint: `ls` piped to `wc`.)

2. Display only the last 10 lines of `/var/log/syslog`.

3. Search `/etc/ssh/sshd_config` for lines containing the word "Port" (case-insensitive). Include line numbers in the output.

### Filtering and Searching

4. List all running processes and filter to show only processes owned by `root`. How many are there? (Solve this in two separate commands: one to show them, one to count them.)

5. Display the active (uncommented, non-blank) lines in `/etc/ssh/sshd_config`. How many active configuration lines are there?

6. Search the kernel message log (`sudo dmesg`) for anything related to your storage device. (Hint: your disk is `sda`.)

### Building Pipelines

7. List all user accounts on the system (extract just the usernames from `/etc/passwd`) and sort them alphabetically.

8. Find the 5 largest items in `/var/log/` sorted by size, largest first. (Hint: `du -h` for sizes, `sort -rh` for reverse human-readable sort, `head` for the top 5.)

9. Create a file called `system-info.txt` that contains:
   - The current date and time
   - Your machine's hostname
   - The output of `uname -m`
   - The output of `free -h`

   Use redirection (`>` for the first line, `>>` for the rest) to build the file without a text editor. Then display the file with `cat` to verify.

10. **Challenge:** Find all unique service names currently in the `LISTEN` state. (Hint: start with `sudo ss -ltnp`, pipe through `grep LISTEN`, use `cut` to extract the process name column, then `sort` and `uniq`. There are multiple valid approaches.)
