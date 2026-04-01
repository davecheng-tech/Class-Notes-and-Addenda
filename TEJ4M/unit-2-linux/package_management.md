# Package Management

This note covers how software is installed on a Linux system. It explains:

- What a package is
- How `apt` works under the hood
- Repositories, dependencies, and the package cache
- `dpkg`: the layer beneath `apt`
- Manual installation: what to do when there is no package
- How to add software to your PATH

<br>

## 1. What Is a Package?

When you run `sudo apt install nginx`, you are installing a **package**. A package is a bundle that contains:

- The compiled program (binary files)
- Configuration files (usually placed in `/etc`)
- Documentation
- Metadata: the package name, version, description, and a list of **dependencies** (other packages it needs to function)

Packages are the standard way software is distributed on Debian-based Linux systems like Lubuntu and Ubuntu. They are pre-built for your architecture — when you install a package on your x86-64 Chromebook, `apt` downloads the x86-64 version automatically.

> [!NOTE]
> This is the software compatibility concept from the processor architecture note in practice. Packages are compiled for a specific architecture. The `apt` package manager knows your machine's architecture and pulls the correct version.

<br>

## 2. How `apt` Works

You have been using `apt` since Unit 1, but it has been a black box: you type a command, software appears. Here is what actually happens.

### Step 1: The Package List (`apt update`)

Before installing anything, your system needs to know what software is available. This information comes from **repositories** — servers on the Internet that host packages.

Your system's repository list is stored in:

```
/etc/apt/sources.list
```

and in individual files under:

```
/etc/apt/sources.list.d/
```

When you run:

```bash
sudo apt update
```

`apt` contacts every repository in these files and downloads a current index of available packages — names, versions, descriptions, and dependencies. This index is stored locally in `/var/lib/apt/lists/`.

`apt update` does **not** install or upgrade anything. It only refreshes the list of what is available.

### Step 2: Dependency Resolution (`apt install`)

When you run:

```bash
sudo apt install nginx
```

`apt` looks up the `nginx` package in the local index and checks its dependency list. If `nginx` requires libraries or other packages that are not already installed, `apt` adds them to the install plan automatically.

This is **dependency resolution** — one of the most important things `apt` does for you. Without it, you would need to manually identify and install every library a program requires, in the correct order.

You have seen this in action. When you install a package, `apt` often reports something like:

```
The following additional packages will be installed:
  libnginx-mod-http-geoip2 nginx-common nginx-core
```

These are dependencies being resolved automatically.

### Step 3: Download

`apt` downloads the package files (`.deb` files) from the repository servers. Downloaded packages are cached locally in `/var/cache/apt/archives/` so they do not need to be re-downloaded if you reinstall later.

### Step 4: Installation (`dpkg`)

Once downloaded, `apt` hands each `.deb` file to **`dpkg`**, the low-level package installer. `dpkg` extracts the files and places them in the correct locations on the filesystem:

- Binaries go to `/usr/bin/` or `/usr/sbin/`
- Configuration files go to `/etc/`
- Libraries go to `/usr/lib/`
- Documentation goes to `/usr/share/doc/`

### Step 5: Post-Install Configuration

Some packages run setup scripts after installation — creating user accounts, generating initial configuration files, or starting services. This is why some installs ask questions or produce output beyond "done."

### The Complete Picture

```
apt update          →  Download package index from repositories
apt install nginx   →  Resolve dependencies
                    →  Download .deb files from repository
                    →  dpkg extracts and installs files
                    →  Post-install scripts run
```

<br>

## 3. Useful `apt` Commands

You already know the basics. Here is the full set of commands worth knowing:

| Command | What it does |
|---|---|
| `sudo apt update` | Refresh the package index from repositories |
| `sudo apt upgrade` | Upgrade all installed packages to their latest versions |
| `sudo apt install <package>` | Install a package (and its dependencies) |
| `sudo apt remove <package>` | Remove a package (keeps configuration files) |
| `sudo apt purge <package>` | Remove a package AND its configuration files |
| `sudo apt autoremove` | Remove packages that were installed as dependencies but are no longer needed |
| `apt search <keyword>` | Search for packages by name or description |
| `apt show <package>` | Show detailed information about a package |
| `apt list --installed` | List all installed packages |
| `dpkg -L <package>` | List all files installed by a package |

### Tracing an Install

To see exactly what `apt` installed and where the files went, use `dpkg -L`:

```bash
dpkg -L nginx
```

This lists every file that the `nginx` package placed on your system. You will see files in `/usr/sbin/` (the binary), `/etc/nginx/` (configuration), `/usr/share/doc/nginx/` (documentation), and more.

This is a useful diagnostic tool. If you are not sure where a package put its configuration file, `dpkg -L` will tell you.

<br>

## 4. `dpkg`: The Layer Beneath

`apt` is a high-level tool that handles repositories, downloads, and dependency resolution. Underneath, it uses **`dpkg`** to do the actual installation.

You can use `dpkg` directly if you have a `.deb` file:

```bash
sudo dpkg -i some-package.deb
```

The `-i` flag means "install." Unlike `apt`, `dpkg` does **not** resolve dependencies. If the package requires libraries that are not installed, `dpkg` will report errors and leave the package in a broken state.

To fix broken dependencies after a `dpkg` install:

```bash
sudo apt install -f
```

The `-f` flag tells `apt` to fix broken dependencies by downloading and installing whatever is missing.

> [!TIP]
> In practice, you rarely use `dpkg` directly. But understanding that it exists helps explain what `apt` is doing behind the scenes and why `.deb` files are the underlying format.

<br>

## 5. Manual Installation: When There Is No Package

Not all software is available through `apt`. Some programs are distributed as:

- Pre-compiled binaries (a downloadable file you run directly)
- Tarballs (compressed archives, `.tar.gz` or `.tar.xz`)
- Source code that must be compiled

When there is no `apt` package, you install software manually. This requires understanding where files should go and how the system finds programs to run.

### How Linux Finds Commands: the PATH

When you type a command like `ls` or `nginx`, the shell does not search the entire filesystem. It looks in a specific list of directories called the **PATH**.

You can see your PATH with:

```bash
echo $PATH
```

**On our Chromebooks, this looks something like:**

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

The PATH is a colon-separated list of directories. When you type a command, the shell checks each directory from left to right. The first match is the program that runs.

This is why:
- Programs installed by `apt` (which places binaries in `/usr/bin/`) work immediately
- A program you download to your home directory does not work by just typing its name — your home directory is not in the PATH

This is also why some of the troubleshooting scenarios produced `command not found` errors — the binary existed, but it was not in any directory the shell searches.

### Manual Install Strategy

When installing software manually, you have two approaches:

**Option A: Install to a PATH directory.** Place the binary in `/usr/local/bin/`, which is in the PATH and is the conventional location for manually installed software.

**Option B: Run it from where it is.** Use the full path to the binary (e.g., `./btop` or `/home/student/btop/bin/btop`). This works but is inconvenient for programs you run frequently.

<br>

## 6. Guided Walkthrough: Manual Install of `btop`

`btop` is an advanced system monitor — like `top` and `htop`, but with a richer interface. It is available through `apt` on some systems, but we will install it manually to learn the process.

> [!NOTE]
> The point of this exercise is not to install `btop` — you could do that with `apt`. The point is to practice the manual installation workflow: download, extract, understand what you have, place it where it needs to go, and verify.

### Step 1: Download the Release

Visit the btop GitHub releases page to find the latest release. On our x86-64 Chromebooks, we need the `x86_64-linux-musl` version.

Download it from the terminal:

```bash
cd /tmp
wget https://github.com/aristocratos/btop/releases/download/v1.4.6/btop-x86_64-unknown-linux-musl.tbz
```

> [!TIP]
> We download to `/tmp` because it is scratch space. If anything goes wrong, we have not cluttered our home directory.

### Step 2: Extract the Archive

The `.tbz` extension is a compressed tar archive (tar + bzip2). Extract it:

```bash
tar -xjf btop-x86_64-unknown-linux-musl.tbz
```

The flags mean:

| Flag | Meaning |
|---|---|
| `-x` | Extract |
| `-j` | Decompress with bzip2 (for `.tbz` / `.tar.bz2` files) |
| `-f` | The next argument is the filename |

### Step 3: Explore What You Extracted

```bash
ls btop/
```

Look at the contents. There will be a `bin/` directory containing the `btop` binary, and possibly a `README`, themes, or other files.

### Step 4: Test It

Run the binary directly from where it was extracted:

```bash
./btop/bin/btop
```

It should launch the system monitor. Press `q` to quit.

This works, but only because you specified the path (`./btop/bin/btop`). Typing just `btop` would fail because the shell cannot find it in the PATH.

### Step 5: Install to the PATH

Copy the binary to `/usr/local/bin/` so it is available system-wide:

```bash
sudo cp btop/bin/btop /usr/local/bin/
```

Now test:

```bash
btop
```

It should launch without needing a path prefix. The shell found it in `/usr/local/bin/`, which is in your PATH.

### Step 6: Clean Up

Remove the downloaded archive and extracted files from `/tmp`:

```bash
rm -r /tmp/btop /tmp/btop-x86_64-linux-musl.tbz
```

### What Just Happened

You performed the same steps that `apt` does automatically:

| `apt` does this | You did this |
|---|---|
| Downloads from a repository | Downloaded from GitHub with `wget` |
| Extracts the `.deb` archive | Extracted the `.tbz` archive with `tar` |
| Places binaries in the PATH | Copied the binary to `/usr/local/bin/` |
| Resolves dependencies | (btop is statically linked — no dependencies needed) |

The difference is that `apt` handles all of this for you — plus dependency resolution. Manual installation requires you to understand each step.

<br>

## 7. Key Terms

| Term | Definition |
|---|---|
| **Package** | A bundle containing a program, its configuration, documentation, and dependency metadata |
| **Repository** | A server that hosts packages for download |
| **Dependency** | A package that another package requires in order to function |
| **Dependency resolution** | The process of automatically identifying and installing all required dependencies |
| **`apt`** | The high-level package manager for Debian-based systems (handles repos, downloads, dependencies) |
| **`dpkg`** | The low-level package installer that extracts and installs `.deb` files |
| **`.deb`** | The package file format used by Debian-based Linux distributions |
| **PATH** | The list of directories the shell searches when you type a command |
| **`/usr/local/bin`** | The conventional location for manually installed software |
| **Tarball** | A compressed archive (`.tar.gz`, `.tar.xz`, `.tbz`) used to distribute files |
| **Statically linked** | A binary that includes all its dependencies internally, requiring no external libraries |

<br>

## Exercise: Manual Install of `micro`

Now do it yourself. `micro` is a modern, user-friendly terminal text editor — similar to `nano` but with syntax highlighting, mouse support, and more intuitive keybindings.

Install `micro` manually by following the same pattern as the `btop` walkthrough. You will need to figure out some of the details on your own.

### Instructions

1. Go to the micro releases page on GitHub: `https://github.com/micro-editor/micro/releases`

2. Find the latest release. Identify which file is the correct download for our machines. The filename will include `linux64` for x86-64. (Hint: think about your architecture. What does `uname -m` report?)

3. Download it to `/tmp` using `wget`.

4. Extract the archive. The file extension tells you what compression is used:

   | Extension | tar flags |
   |---|---|
   | `.tar.gz` or `.tgz` | `-xzf` |
   | `.tar.bz2` or `.tbz` | `-xjf` |
   | `.tar.xz` | `-xJf` |

   Look at the filename you downloaded. Which flags do you need?

5. Explore the extracted directory. Where is the binary?

6. Run it directly from the extracted location to test it. Open a file, type something, and save. (Hint: `Ctrl+S` to save, `Ctrl+Q` to quit — more intuitive than `nano`.)

7. Install it to `/usr/local/bin/` so it is available system-wide.

8. Verify: type `micro` from any directory. Does it launch?

9. Clean up `/tmp`.

10. Confirm where the system finds it:
    ```bash
    which micro
    ```
    The output should be `/usr/local/bin/micro`.

> [!TIP]
> **Going further:** Some of you may have already installed `micro` using `apt` during Unit 1. If `which micro` shows `/usr/bin/micro` before you start, that is the `apt`-installed version. After your manual install to `/usr/local/bin/`, run `which micro` again. Which version does the shell find first, and why? (Hint: look at the order of directories in your PATH.)
