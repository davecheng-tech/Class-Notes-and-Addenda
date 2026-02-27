# Terminal Reference - CLI, Networking, and Linux

This is a quick command reference for Lubuntu (Ubuntu Linux). Use it as a study sheet and troubleshooting checklist.

## 1) CLI basics (navigation and files)

| Task | Command | Notes |
|---|---|---|
| Show current directory | `pwd` | Prints the full path of where you are. |
| List files/folders | `ls` | Add `-l` for details. |
| Detailed list | `ls -l` | Permissions, owner, size, date. |
| Change directory | `cd <path>` | Example: `cd ~/Documents` |
| Home directory | `cd ~` | `~` means your home folder. |
| Make a folder | `mkdir <name>` | Creates one folder. |
| Make nested folders | `mkdir -p a/b/c` | Creates the full path if needed. |
| Create an empty file | `touch file.txt` | Also updates timestamp if file exists. |
| Delete a file | `rm file.txt` | Permanent. No recycle bin in terminal. |
| Delete a folder | `rm -r foldername` | Dangerous. Deletes folder contents. |

## 2) Getting help

| Task | Command | Notes |
|---|---|---|
| Quick help | `<command> --help` | Fast overview. |
| Manual page | `man <command>` | Full docs. Press `q` to quit. |
| Search in man | `/word` | Type `/address` then Enter. |

## 3) Editing text files (`nano`)

| Task | Command | Notes |
|---|---|---|
| Open a file | `nano file.txt` | Creates it if it does not exist. |
| Save (write out) | `Ctrl-O` then Enter | Writes changes to disk. |
| Exit | `Ctrl-X` | Prompts to save if needed. |

## 4) Admin privileges (`sudo`)

| Task | Command | Notes |
|---|---|---|
| Run as admin | `sudo <command>` | Prompts for your password. |

## 5) Software management with `apt`

| Task | Command | What it does |
|---|---|---|
| Update package list | `sudo apt update` | Refreshes what versions are available from repositories. |
| Upgrade installed packages | `sudo apt upgrade` | Installs available upgrades for installed packages. |
| Install a package | `sudo apt install <package>` | Example: `sudo apt install curl` |
| Remove a package | `sudo apt remove <package>` | Uninstalls a package. |

Common packages for this unit:

| Package | Why you might install it |
|---|---|
| `net-tools` | Adds legacy tools like `ifconfig`. |
| `curl` | Download files over HTTP/HTTPS from the terminal. |
| `openssh-server` | Enables SSH server (remote login). |

## 6) Network tools (addresses, routing, DNS)

| Task | Command | Notes |
|---|---|---|
| Show IP addresses (compact) | `ip -br addr` | Best first command to find your IPv4. |
| Show routes (gateway) | `ip route` | Look for `default via ...` |
| Show DNS configuration | `resolvectl status` | Lists DNS servers and interface info. |
| Legacy interface view | `ifconfig` | Requires `net-tools`. |

## 7) Connectivity tests

| Task | Command | Notes |
|---|---|---|
| Ping default gateway | `ping -c 2 <gateway_ip>` | Tests local network reachability. Stops after 2 ping count.|
| Ping a public IP | `ping -c 2 8.8.8.8` | Tests internet routing (not DNS). |

## 8) Hosting a simple HTTP service

| Task | Command | Notes |
|---|---|---|
| Start web server | `python3 -m http.server 8000` | Runs a simple HTTP server on TCP port 8000. |
| Test locally (same machine) | Browser: `http://127.0.0.1:8000` | `127.0.0.1` means "this computer". |
| Test from LAN (another device) | Browser: `http://<your_ipv4>:8000` | Uses the server's LAN IP and port. |

## 9) Ports and processes (what is listening?)

| Task | Command | Notes |
|---|---|---|
| Show listening sockets | `ss -tulpen` | Look for `:8000` or `:22`. |
| Show which process owns a port | `sudo lsof -nP -iTCP:8000 -sTCP:LISTEN` | Replace 8000 with your port. |
