# Network Services Project

**Course:** TEJ4M - Computer Engineering (Grade 12)\
**Unit:** Networking\
**Timeline:** \~1 Week (4–5 class periods) + optional at‑home work

## Contents

- [Project Overview](#project-overview)
- [Service Selection](#service-selection)
- [Required Workflow](#required-workflow-per-service)
- [Final Deliverable: Server Documentation](#final-deliverable-server-documentation)
- [Academic Integrity](#academic-integrity)
- [Technical Reference](#technical-reference-lubuntu)
- [Assessment Rubric](#assessment-rubric)
- [Suggested Timeline](#suggested-timeline)

## Project Overview

You have transformed an obsolete Chromebook into a working Lubuntu Linux system. Your task is to convert this machine into a functional network server by installing, configuring, verifying, and documenting multiple real network services.

This project emphasizes the workflow used by professional system administrators:

**Install > Configure > Restart > Verify (Local) > Verify (Remote) > Diagnose**

You must implement a **minimum of four (4) services** and demonstrate that they are reachable from other devices. Your documentation must show evidence of TCP/IP model understanding: Internet layer (IP addressing), Transport layer (TCP/UDP ports), and Application layer (service protocol).

To earn the highest achievement level, you must demonstrate one competency that operates at the Internet layer (beyond simple local application access). Specific options and requirements are described later in this document.

## Service Selection

Choose a **minimum of four (4)** services from the menu below.

**Level 4+ requirement:** At least one service must come from Tier 3.

**Tier 1: Foundation Services**
- [Web Server: Nginx (HTTP)](#web-server-nginx-http)
- [Remote Access: SSH (Secure Shell)](#remote-access-ssh-secure-shell)
- [Time Service: NTP](#time-service-ntp-chrony-or-systemd-timesyncd)

**Tier 2: Resource Sharing**
- [File Sharing: Samba (SMB/CIFS)](#file-sharing-samba-smbcifs)
- [File Sync: Syncthing (P2P Sync)](#file-sync-syncthing-p2p-sync)
- [Print Server: CUPS (IPP)](#print-server-cups-ipp)
- [Music Server: Navidrome (Web Music Player)](#music-server-navidrome-web-music-player)
- [Media Server: MiniDLNA (ReadyMedia)](#media-server-minidlna-readymedia)
- [Game Server: Minetest (Open-Source Sandbox)](#game-server-minetest-open-source-sandbox)
- [Service of Your Choice](#service-of-your-choice)

**Tier 3: Internet Layer Competencies**
- [DNS Sinkhole / Ad-Blocker: Pi-hole](#dns-sinkhole--ad-blocker-pi-hole)
- [Mesh VPN: Tailscale](#mesh-vpn-tailscale)
- [NAT Gateway: Port Forwarding (Home Network)](#nat-gateway-port-forwarding-home-network)
- [Dynamic DNS: DuckDNS](#dynamic-dns-duckdns)

### Tier 1: Foundation Services (Standard)

These establish core server functionality on a LAN and are the easiest to install and verify.

#### Web Server: Nginx (HTTP)

Nginx is a web server that delivers webpages and other web content to clients over HTTP.

- [Install](https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview) nginx with `sudo apt install nginx`.
- [Configure](https://ubuntu.com/tutorials/install-and-configure-nginx#3-creating-our-own-website) the server to present a custom welcome page that clearly identifies the server machine (at minimum, include the server name).
- You can start by replacing the default web page with your own `index.html` in `/var/www/html`.
- **Estimated Difficulty:** 1/5 (Straightforward).

#### Remote Access: SSH (Secure Shell)

SSH is a secure remote login service that lets you administer a Linux machine from another computer over the network.

- [Install](https://documentation.ubuntu.com/server/how-to/security/openssh-server/) SSH with `sudo apt install openssh-server`.
- Edit the default configuration at `/etc/ssh/sshd_config` and do the following:
    - Change default port from 22 to 2222
    - Disable root login
- Restart the `ssh` server with these two commands (as described in the header of the configuration file you edited above):

```
sudo systemctl daemon-reload
sudo systemctl restart ssh.socket
```

> **Note:** Restarting most Linux services is usually simpler than this. For example, many services can be restarted with a single command like `sudo systemctl restart nginx`. OpenSSH on Lubuntu is configured a bit differently, so restarting it is a little more complex than the typical service restart.

- Log into your server remotely (e.g., from one of the lab iMac computers) using `ssh` with the added switch for the non-standard port number:

```
ssh your-username@<your-server-ip> -p 2222
```
- End your remote session by pressing Ctrl+D or entering `logout` at the prompt.
> **Note:** This configuration above makes SSH slightly more secure (e.g., by using a non-standard port). This is especially useful if a machine is exposed to the public internet. You may switch the port back to the default 22 after you've gathered the required screenshots and documentation if using a non-standard port becomes inconvenient.

- **Estimated Difficulty:** 2/5 (Easy).

#### Time Service: NTP (Chrony or systemd-timesyncd)

NTP is a time synchronization service that keeps computers accurate by syncing their clocks to a trusted time source.

- Install and enable NTP service on the server (e.g. [Chrony](https://documentation.ubuntu.com/server/how-to/networking/serve-ntp-with-chrony/)).
- Demonstrate another device syncing time or reading time from your server (e.g., `sntp` command).
- **Estimated Difficulty:** 2/5 (Easy).

### Tier 2: Resource Sharing (Intermediate)

These provide shared resources or user-facing services on the network.

#### File Sharing: Samba (SMB/CIFS)

Samba is a file-sharing service that lets other devices access shared folders on your Linux server as network drives.

- [Install and configure](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview) Samba with `sudo apt install samba`.
- Create network-accessible folders on the server and populate them with some documents or data to share.
- Create at least one private share (require password and user authentication, must set up Samba user account).
- Connect to the folder from a network client machine running Windows (File Explorer), macOS (Finder), iOS (Files), Android (Android Samba Client, CX File Explorer).
- **Estimated Difficulty:** 3/5 (Moderate).

#### File Sync: Syncthing (P2P Sync)

Syncthing is a peer-to-peer file synchronization service that keeps a folder identical across multiple devices.

- [Install](https://docs.syncthing.net/intro/getting-started.html) Syncthing on the server with `sudo apt install syncthing`.
- Start the Syncthing service (user mode, `systemctl --user start syncthing`) and open the Web GUI in a browser at http://127.0.0.1:8384.
- Install Syncthing on a second device and connect both by interchanging their Device IDs in the Web GUI.
- Verify that a configured folder is automatically synchronized between the two devices.
- **Estimated Difficulty:** 4/5 (Challenging).

#### Print Server: CUPS (IPP)

CUPS is a print server that shares a printer on the network so other devices can print through your Linux server.

- [Install](https://documentation.ubuntu.com/server/how-to/networking/cups-print-server/) the CUPS server with `sudo apt install cups`.
- Share a USB printer (connected to the server) on the network.
- Add the shared printer on a client device (via Printers settings on Windows or macOS) and print a test page.
- **Estimated Difficulty:** 4/5 (Challenging).

#### Music Server: Navidrome (Web Music Player)

Navidrome is a self-hosted music streaming server with a built-in web interface and Subsonic API support, letting you browse and stream your music collection from any browser or compatible mobile app.

- It is not available directly via `apt` — follow the [Quick Start](https://www.navidrome.org/docs/installation/linux/) guide to obtain and install a release package from its GitHub page.
- Add at least a few music files to the configured music folder.
- Access the Navidrome web UI from another device on the LAN and log in.
- Browse your library and demonstrate playback in the browser.
- **Estimated Difficulty:** 3/5 (Moderate).

#### Media Server: MiniDLNA (ReadyMedia)

MiniDLNA is a lightweight media server that shares music and video on a LAN using DLNA/UPnP so clients can stream content.

- [Install](https://minidlna.com) MiniDLNA with `sudo apt install minidlna`.
- Host at least one media file.
- Demonstrate playback from another device (e.g., VLC on a phone, or a smart TV with native DLNA support).
- If your smart TV (or other DLNA player) doesn't automatically detect the presence of the media server, you can force a VLC client to connect to it explicitly at `upnp://<server-ip>:8200` for testing.
- **Estimated Difficulty:** 3/5 (Moderate).

#### Game Server: Minetest (Open-Source Sandbox)

Minetest is a lightweight open-source sandbox game that can run as a multiplayer server on a LAN.

- Install the Minetest server package.
- Initialize a world and server configuration.
- Configure server properties (server name, game mode, maximum players, etc.).
- Connect to the server from another device using the Minetest client (`sudo apt install minetest` on Linux, or download from [minetest.net](https://www.minetest.net)) and verify that multiplayer works.
- **Estimated Difficulty:** 3/5 (Moderate).

#### Service of Your Choice

This option lets you propose another client-server network service that can run reliably on this hardware.

- Service must run reliably on the limited hardware of the Chromebook.
- Must be installable using standard Linux tools (e.g., apt or official binaries).
- Must be client-server style and network-accessible from another device on the LAN.
- You must demonstrate that it operates correctly and document how you configured it.
- **Estimated Difficulty:** Varies.

### Tier 3: Internet Layer Competencies (Advanced)

These demonstrate understanding of networking beyond the local subnet.

#### DNS Sinkhole / Ad-Blocker: Pi-hole

Pi-hole is a local DNS server that provides network-wide ad blocking and domain filtering by intercepting and controlling DNS queries from client devices.

- [Install](https://docs.pi-hole.net/main/basic-install/) Pi-hole with the `curl` command.

> **Note:** Your Lubuntu machine is most likely getting a dynamic IP address from DHCP. During setup, ignore the warning about needing a static IP address. This is a proof-of-concept deployment, so a changing IP is acceptable.

> **Note:** Pi-hole's admin interface installs on port 80 by default, falling back to port 8080 if port 80 is in use. If you are already running a web server, be aware of this conflict. If both ports are unavailable, you can manually configure the admin portal port (see [documentation](https://docs.pi-hole.net/main/prerequisites/)).

- Once set up, configure a client to use your server as its ONLY DNS server.
- Demonstrate blocked ads or domains (e.g., screenshot of a webpage using a normal DNS server vs. using Pi-hole DNS server).
- **Estimated Difficulty:** 3/5 (Moderate).

#### Mesh VPN: Tailscale

Tailscale is a VPN overlay network that creates secure, private connectivity between devices across the Internet.

- Begin by signing up for a free account. (You might have to use a personal Google or Apple ID in lieu of your school account, which may be blocked.) You can use the [admin console](https://login.tailscale.com/admin/machines) to keep track of your "tailnet" as you bring machines into your VPN.
- [Install](https://tailscale.com/docs/install/linux) Tailscale client on your server.
- [Install](https://tailscale.com/download) a client on a second device (e.g., mobile phone or laptop) which will be used outside of your LAN.
- Access your server from a device outside of your LAN, for example:
    - If the server is on school Wi-Fi, you can access it with a mobile phone on cellular data.
    - If the server is on a home LAN, you can leave the machine at home for the day and access it from school.
- Each machine on your tailnet is assigned a unique IP address in the `100.x.x.x` range — use this address to reach that machine over the VPN from any other tailnet device, regardless of where it is.
- **Estimated Difficulty:** 3/5 (Moderate).

#### NAT Gateway: Port Forwarding (Home Network)

Port forwarding is a router configuration that maps incoming Internet traffic to a specific device and port on your home network.

- Configure your home router to forward external traffic to your server.
- For example, if you have nginx running a web server on the machine at port 80, you can set your router's incoming port 8081 to forward traffic to the internal machine (IP + port).
- Demonstrate external access with a mobile device on cellular data, or another network entirely (e.g. school Wi-Fi).
- Pairs well with **Dynamic DNS**. Together they give your server a stable, named public presence on the Internet.

> **Note:** Be careful when modifying your home router's configuration. This level of tinkering is often not officially supported by service providers and could disrupt your home Internet if misconfigured.

- **Estimated Difficulty:** 4/5 (Challenging).

#### Dynamic DNS: DuckDNS

Dynamic DNS (DDNS) maps a persistent hostname to your public IP address, automatically updating when it changes. This makes a home server reliably reachable by name even when an ISP assigns a new IP.

- **Requires NAT Gateway (Port Forwarding).** A DNS hostname pointing to your public IP is only useful if that IP has services exposed through your router.
- Sign up at [DuckDNS](https://www.duckdns.org) and register a free subdomain (e.g., `yourname.duckdns.org`).
- Install and configure the [DuckDNS update client](https://www.duckdns.org/install.jsp) so the hostname stays synchronized with your current public IP.
- Demonstrate that the hostname resolves correctly from outside your LAN, for example using `nslookup yourname.duckdns.org` or `dig yourname.duckdns.org` from a phone on cellular data.
- **Estimated Difficulty:** 2/5 (Easy).

## Required Workflow (Per Service)

For each selected service, you must perform and understand the following steps:

1. Install the software (apt).
2. Modify configuration files as needed (commonly in `/etc/`).
3. Restart the service using systemctl.
4. Verify the service is listening locally.
5. Verify access from a different device.
6. Troubleshoot any issues encountered.

## Final Deliverable: Server Documentation

Submit one Google Document containing a section for each service.

### For Each Service Include:

#### 1. Identity

- Service name.
- Brief description of what the service does and/or what it provides to clients.
- What resource or capability the service is delivering (e.g., webpages, files, remote access, time, media, etc.).

#### 2. Transport Details

- TCP or UDP.
- Configured port number.

#### 3. Local Network Evidence

Screenshot showing BOTH:

- `ip -br addr`.
- A filtered port check showing ONLY your service in the LISTEN state, e.g., `sudo ss -ltnp | grep :PORT`.

#### 4. Configuration Evidence

Screenshot(s) proving your configuration changes.

- Must clearly show the line(s) you added, changed, etc.
- Evidence must be captured from the terminal using commands such as `cat`, `less`, or `grep` (recommended).
- You may still use `nano` (or another terminal editor) to make the change, but your proof should show the final file contents in the terminal.

#### 5. Remote Access Evidence

Screenshot(s) or photo(s) showing proof of access from a different device (laptop, phone, tablet).

- Web interface, terminal session, file browser, etc.
- Visual evidence should ideally show that server access is across LAN or WAN (e.g. server IP is visible in the browser address bar).

#### 6. Troubleshooting Log

Describe one real challenge, problem, or difficulty you encountered installing and configuring this service. Include how you fixed it, referencing:

- Symptoms.
- Diagnostic commands used.
- Root cause.

If you did not encounter a real problem, demonstrate how you verified that the service was functioning correctly or describe how you would diagnose a failure.

## Academic Integrity

You may consult documentation and online resources. However:

- All configuration work must be performed by you.
- Documentation must be written in your own words.
- You must understand every command you use.

## Technical Reference (Lubuntu)

Find IP addresses:

```
ip -br addr
```

Show all listening ports (TCP):

```
sudo ss -ltnp
```

Show all listening ports (TCP + UDP):

```
sudo ss -tulpn
```

Filter to one service port (replace PORTNUMBER):

```
sudo ss -ltnp | grep :PORTNUMBER
```

Edit configuration files (common location):

```
sudo nano /etc/[service]/[config_file]
```

Restart a service:

```
sudo systemctl restart [service]
```

Check service status:

```
systemctl status [service]
```

Connect to Wi-Fi (if working from home):

```
nmcli device wifi list
```

```
nmcli device wifi connect "NetworkName" password "mypassword"
```

> **Note:** The Wi-Fi adapter on your machine is `wlp1s0`. The commands above will use it automatically. Once connected, verify your IP address with `ip -br addr`.

## Assessment Rubric

This project will be evaluated based on both the successful deployment of network services and your demonstrated understanding of how they function within the TCP/IP model.

Achievement levels correspond approximately to Ontario grading bands:

- **Level 1:** 50–59%.
- **Level 2:** 60–69%.
- **Level 3:** 70–79%.
- **Level 4 / 4+:** 80–100%.

<br>

## Service Implementation & Functionality

**Assesses how successfully the selected services are installed, configured, customized, and made accessible from other devices.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All Level 4 criteria are met. At least one Tier 3 service is fully functional and demonstrates understanding of networking beyond the local subnet (e.g., DNS control, VPN routing, or external access via NAT). |
| **4** | Four or more services are fully functional and reliably accessible. Configurations go beyond defaults and clearly demonstrate intentional customization. |
| **3** | Four services are functional on the LAN with appropriate configuration changes. Minor issues may be present but do not prevent normal use. |
| **2** | Some services function, but others are incomplete, unreliable, or largely unchanged from default configuration. |
| **1** | Few services function correctly, or major configuration problems prevent reliable access. |


## TCP/IP Understanding (Layers & Ports)

**Assesses understanding of how each service operates within the TCP/IP model, including IP addressing, transport protocols, and ports.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All Level 4 criteria are met. Demonstrates clear insight into how traffic moves between networks, as evidenced by the Tier 3 service (e.g., DNS resolution, NAT traversal, or VPN routing). |
| **4** | Demonstrates clear and accurate understanding of Internet, Transport, and Application layers, including how services use IP addressing and ports. |
| **3** | Correctly identifies protocol type (TCP/UDP) and port numbers for services and demonstrates solid understanding of local network communication. |
| **2** | Demonstrates partial understanding. Some confusion about ports, protocols, or how clients reach the server. |
| **1** | Demonstrates minimal understanding of how the services communicate over the network. |


## Diagnostic Process & Troubleshooting

**Assesses the ability to verify service operation and resolve problems using appropriate tools and reasoning.**

| Level | Descriptor |
|:-----:|------------|
| **4** | Uses a systematic, layer-by-layer approach to diagnosis. Independently applies tools such as `ip`, `ss`, and `systemctl` to identify root causes and resolve issues. |
| **3** | Successfully verifies services using standard commands and can resolve common issues with minimal guidance. |
| **2** | Requires assistance to diagnose problems. Troubleshooting steps are incomplete or unsystematic. |
| **1** | Demonstrates little ability to verify or troubleshoot services independently. |


## Documentation & Communication

**Assesses clarity, completeness, and professionalism of the submitted evidence and explanations.**

Your Google Document must use a consistent and clear hierarchy using Google Docs Styles (e.g., Title, Heading 1, Heading 2, Heading 3) rather than manually formatting text.

| Level | Descriptor |
|:-----:|------------|
| **4** | Documentation is thorough, well-organized, and professional. All required evidence is present and clearly supports the claims made. Technical terminology is used accurately. |
| **3** | Documentation is clear and complete with required screenshots and explanations. Minor gaps or organization issues may be present. |
| **2** | Documentation is incomplete, unclear, or missing important evidence. Explanations lack detail. |
| **1** | Documentation is minimal, disorganized, or fails to demonstrate that requirements were met. |


## Suggested Timeline

**Day 1 - System Preparation**\
Updates, networking checks, choose services.

**Day 2-3 - Implementation**\
Install and configure services.

**Day 4 - Verification and Troubleshooting**\
Local and remote testing.

**Day 5 - Documentation and Demonstration**\
Finalize report and submit.
