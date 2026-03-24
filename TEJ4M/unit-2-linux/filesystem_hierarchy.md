# Filesystem Hierarchy

This note covers how Linux organizes files and directories. It explains:

- Why a filesystem needs structure
- The root directory and the directory tree
- Key directories and what lives in each one
- The Filesystem Hierarchy Standard (FHS)
- How to explore the filesystem on your own machine

<br>

## 1. Why Structure Matters

Every file on a Linux system has a location. Configuration files, program binaries, user documents, log files, temporary data, and hardware interfaces all exist somewhere in the filesystem. On a running Lubuntu system, there are tens of thousands of files.

Without an organizing principle, finding anything would be impossible. Worse, programs that need to locate configuration files or shared libraries would have no reliable way to do so.

Linux solves this problem with a standardized directory layout. Every major directory has a defined purpose. Once you understand the layout, you can predict where things live on any Linux system — not just your own.

This matters practically. When you edited `/etc/ssh/sshd_config` in Unit 1, you were working in `/etc` because that is where Linux keeps configuration files. That was not an arbitrary choice. It is part of the structure described in this note.

<br>

## 2. The Root Directory

Every file and directory on a Linux system exists inside a single tree that starts at the **root directory**, written as `/`.

There is no equivalent of Windows drive letters (`C:\`, `D:\`). Even if a machine has multiple storage devices, they are all mounted somewhere within the same tree. Everything starts at `/`.

```
/
├── bin
├── boot
├── dev
├── etc
├── home
├── opt
├── proc
├── sbin
├── tmp
├── usr
└── var
```

This is not a complete listing — a real system has additional directories — but these are the ones worth understanding.

**On our Chromebooks:**

```bash
ls /
```

```
bin   dev  home  lib64       media  opt   root  sbin  srv       sys  usr
boot  etc  lib   lost+found  mnt    proc  run   snap  swapfile  tmp  var
```

Some of these directories (like `lib`, `lib64`) exist because our machines run a 64-bit OS. Others (`snap`, `lost+found`, `swapfile`) are system-managed and not something you interact with directly. You do not need to memorize all of them. Focus on the ones described below.

<br>

## 3. Key Directories

### `/home` — User Files

Each user account has a personal directory inside `/home`. Your home directory is `/home/yourname`.

This is where your documents, downloads, configuration files for desktop applications, and personal data live. The `~` shortcut in the terminal always refers to your home directory.

When you run `ls -la ~`, the files starting with `.` (like `.bashrc`, `.config`, `.local`) are hidden configuration files for your user account. Programs store per-user settings here rather than in system-wide locations.

On a multi-user system, each user has their own directory under `/home`, and standard permissions prevent users from reading each other's files.

### `/etc` — System Configuration

`/etc` contains configuration files for the system and for installed services. These are plain text files that control how software behaves.

You have already worked with files in `/etc`:

| File | Service | What you configured |
|---|---|---|
| `/etc/ssh/sshd_config` | SSH | Changed port, disabled root login |
| `/etc/nginx/sites-available/default` | Nginx | Custom web server configuration |
| `/etc/samba/smb.conf` | Samba | File sharing settings |
| `/etc/apt/sources.list` | APT | Software repository locations |

The pattern is consistent: install a service, then configure it by editing a file in `/etc`. This is one of the most important directories to understand as a system administrator.

> [!NOTE]
> The name `/etc` historically stood for "et cetera" — a catch-all. Over time it became the standard location specifically for configuration files. The name stuck.

### `/var` — Variable Data

`/var` holds data that changes during normal system operation. The most important subdirectories are:

| Directory | Contents |
|---|---|
| `/var/log` | System and service log files |
| `/var/cache` | Cached data (e.g., downloaded package files from `apt`) |
| `/var/www` | Default location for web server content (e.g., your Nginx pages) |

When something goes wrong with a service, `/var/log` is often the first place to look. Log files record what happened and when.

### `/usr` — Installed Software

`/usr` contains the majority of installed programs, libraries, and documentation. It is organized into subdirectories:

| Directory | Contents |
|---|---|
| `/usr/bin` | Most user-facing commands and programs |
| `/usr/sbin` | System administration commands |
| `/usr/lib` | Shared libraries used by programs |
| `/usr/share` | Architecture-independent data (docs, icons, fonts) |

When you install software with `apt`, the program files typically end up somewhere under `/usr`.

> [!NOTE]
> On many modern Linux distributions including Lubuntu, `/bin` is actually a **symbolic link** to `/usr/bin`, and `/sbin` is a link to `/usr/sbin`. A symbolic link (or symlink) works like a shortcut — it is a special file that points to another location. When you access `/bin`, the system silently redirects you to `/usr/bin`. Historically these were separate directories, but they have been merged. You may still see them referenced separately in documentation.

### `/tmp` — Temporary Files

`/tmp` is a scratch space. Programs and system services use it for temporary data that does not need to persist. On a running system, `/tmp` is rarely empty — services like Bluetooth, system logging, and other background processes store working files here.

The contents are typically cleared on reboot. Any user can write to `/tmp`, which makes it useful but also a reason to be cautious about what you store there. It is not a permanent location.

### `/boot` — Startup Files

`/boot` contains the files needed to start the operating system: the Linux kernel, the initial RAM disk, and the bootloader configuration.

**On our Chromebooks, `lsblk` shows the disk layout:**

```
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda      8:0    0  14.9G  0 disk
├─sda1   8:1    0   300M  0 part /boot/efi
└─sda2   8:2    0  14.6G  0 part /
```

The EFI boot partition (`sda1`) is separate from the root filesystem (`sda2`). The boot partition contains the bootloader; the root partition (`/`) is where the OS and all your files live.

> [!NOTE]
> `lsblk` may also show several `loop` devices — these are snap packages (like Firefox) mounted as virtual block devices. They are managed by the system and can be ignored.

### `/opt` — Optional Software

`/opt` is for software installed outside of the distribution's package manager. If you download and install a program manually (not through `apt`), `/opt` is a conventional place to put it.

This directory will become more relevant later in this unit when we cover manual software installation.

### `/dev` — Devices

`/dev` contains **device files**: special files that represent hardware components. They are not regular files with stored data — they are interfaces that the kernel provides for programs to communicate with hardware.

For example:

| Device file | Represents |
|---|---|
| `/dev/sda` | The first storage disk |
| `/dev/sda1`, `/dev/sda2` | Partitions on that disk |
| `/dev/null` | A "black hole" — anything written to it is discarded |
| `/dev/zero` | A source of infinite zero bytes |
| `/dev/random` | A source of random data |

You do not normally interact with `/dev` directly, but its existence illustrates an important Linux principle: **everything is a file**. Hardware, processes, and even abstract data sources are accessed through the same filesystem interface.

### `/proc` — Process Information

`/proc` is a **virtual filesystem**. It does not exist on disk. Instead, the kernel generates its contents on the fly to expose information about running processes and system state.

For example:

```bash
cat /proc/cpuinfo
```

This does not read a stored file. The kernel dynamically generates CPU information when you access it. Similarly, `/proc/meminfo` provides live memory statistics, and each running process has a numbered directory (e.g., `/proc/1234/`) containing information about that process.

> [!TIP]
> Commands like `lscpu` and `free` work by reading from `/proc` and formatting the output. When you run `lscpu`, it is parsing `/proc/cpuinfo` for you.

<br>

## 4. The Filesystem Hierarchy Standard

The directory layout described above is not arbitrary. It follows the **Filesystem Hierarchy Standard (FHS)**, a specification that defines where files should be placed on a Linux system.

The FHS exists so that:

- Programs can find configuration files, libraries, and data in predictable locations
- System administrators can navigate any Linux machine with the same mental model
- Package managers like `apt` know where to install files

Not every Linux distribution follows the FHS identically, but the major directories (`/etc`, `/home`, `/usr`, `/var`, `/tmp`, `/dev`, `/proc`) are consistent across virtually all of them. What you learn on Lubuntu applies on Ubuntu Server, Debian, Fedora, and most other distributions.

<br>

## 5. A Map of the Filesystem

The following table summarizes the key directories. Use it as a reference.

| Directory | Purpose | Changes often? | Example contents |
|---|---|---|---|
| `/home` | User personal files | Yes | Documents, downloads, dotfiles |
| `/etc` | System configuration | When you configure something | `sshd_config`, `smb.conf`, `sources.list` |
| `/var` | Variable runtime data | Yes | Logs, caches, web content |
| `/usr` | Installed programs and libraries | When you install software | Binaries, shared libraries, docs |
| `/tmp` | Temporary files | Cleared on reboot | Scratch data |
| `/boot` | Kernel and bootloader | Rarely | `vmlinuz`, `initrd.img` |
| `/opt` | Optional/manual software | When you manually install | Third-party applications |
| `/dev` | Device interfaces | Managed by kernel | `sda`, `null`, `random` |
| `/proc` | Live process/system info | Virtual, always current | `cpuinfo`, `meminfo`, process dirs |

<br>

## 6. Key Terms

| Term | Definition |
|---|---|
| **Root directory** | `/` — the top of the filesystem tree; every file path starts here |
| **FHS** | Filesystem Hierarchy Standard — the specification that defines where files belong on a Linux system |
| **Home directory** | `/home/username` — a user's personal file space; abbreviated `~` |
| **Configuration file** | A text file (typically in `/etc`) that controls how a service or program behaves |
| **Device file** | A special file in `/dev` that provides an interface to a hardware device |
| **Virtual filesystem** | A filesystem like `/proc` that is generated by the kernel in memory, not stored on disk |
| **Mount** | The act of making a storage device accessible at a specific point in the directory tree |
| **Symbolic link (symlink)** | A file that points to another file or directory, similar to a shortcut |

<br>

## Exercise: Filesystem Scavenger Hunt

Answer each question by running a command on your Lubuntu machine. Record the command you used and the answer.

1. What is the full path to your home directory? (Use a command, don't just type it.)

2. List the contents of `/etc/apt/`. What files and directories are in there?

3. Find the log file for the `apt` package manager. It is somewhere under `/var/log/`. What is the full path, and what does the most recent entry say?

4. How many files and directories are in `/usr/bin/`? To count them, you can **pipe** the output of one command into another using the `|` symbol. The command `wc -l` counts lines. Try combining `ls` and `wc -l` with a pipe to get the count.

5. Read the first 5 lines of `/proc/cpuinfo`. What processor model does it report?

6. What does `/dev/null` do? Test it: run `echo "hello" > /dev/null` and then try to read the file with `cat /dev/null`. What happened?

7. Run `ls -la /bin`. What do you notice about this directory? What does the output tell you about the relationship between `/bin` and `/usr/bin`?

8. Find the configuration file for the hostname of your machine. It is a single-line file in `/etc/`. What is the file called, and what does it contain? (The hostname is the name you chose for your computer during the Lubuntu installation.)

9. Look inside `/tmp/` with `ls -la /tmp/`. What is in there? Based on the names, what kinds of programs are using `/tmp` for temporary storage?

10. Run `df -h /`. How much disk space is used and how much is available on the root partition?
