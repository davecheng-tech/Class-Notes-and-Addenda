# Network Services  Project

**Course:** TEJ4M - Computer Engineering (Grade 12)\
**Unit:** Networking\
**Timeline:** \~1 Week (4–5 class periods) + optional at‑home work

## Project Overview

You have transformed an obsolete Chromebook into a working Lubuntu Linux system. Your task is to convert this machine into a functional network server by installing, configuring, verifying, and documenting multiple real network services.

This project emphasizes the workflow used by professional system administrators:

**Install > Configure > Restart > Verify (Local) > Verify (Remote) > Diagnose**

You must implement a **minimum** **of four (4) services** and demonstrate that they are reachable from other devices. Your documentation must show evidence of TCP/IP model understanding: Internet layer (IP addressing), Transport layer (TCP/UDP ports), and Application layer (service protocol).

To earn the highest achievement level, you must demonstrate one competency that operates at the Internet layer (beyond simple local application access). Specific options and requirements are described later in this document.

## Service Selection

Choose a **minimum of** **four (4)** services from the menu below.

**Level 4+ requirement:** At least one service must come from Tier 3.

### Tier 1: Foundation Services (Standard)

These establish core server functionality on a LAN and are the easiest to install and verify.

**Web Server — Nginx (HTTP)**\
Nginx is a web server that delivers webpages and other web content to clients over HTTP.

- Install nginx
- Configure the server to present a custom welcome page that clearly identifies the server machine (at minimum, include the server name)

**Remote Access — SSH (Secure Shell)**\
SSH is a secure remote login service that lets you administer a Linux machine from another computer over the network.

- Change default port from 22 to 2222
- Disable root login in `sshd_config`

**Time Service — NTP (Chrony or systemd-timesyncd)**\
NTP is a time synchronization service that keeps computers accurate by syncing their clocks to a trusted time source.

- Install and enable NTP service
- Demonstrate another device syncing time from your server

### Tier 2: Resource Sharing (Intermediate)

These provide shared resources or user-facing services on the network.

**File Sharing — Samba (SMB/CIFS)**\
Samba is a file-sharing service that lets other devices access shared folders on your Linux server as network drives.

- Create network-accessible folders on the server and populate them with some documents or data to share
- One Public share (read-only)
- One Private share (password required)
- Connect to the folder from a network client machine running Windows (File Explorer), macOS (Finder), iOS (Files), Android (Android Samba Client, CX File Explorer)

**File Sync — Syncthing (P2P Sync)**\
Syncthing is a peer-to-peer file synchronization service that keeps a folder identical across multiple devices.

- Sync a folder between server and another device
- Must use the Web GUI

**Print Server — CUPS (IPP)**\
CUPS is a print server that shares a printer on the network so other devices can print through your Linux server.

- Share a USB printer (connected to the server) on the network
- Printer must be usable from another device

**Media Server — MiniDLNA (ReadyMedia)**\
MiniDLNA is a lightweight media server that shares music and video on a LAN using DLNA/UPnP so clients can stream content.

- Host at least one media file
- Demonstrate playback from another device (e.g., VLC on a phone, or a smart TV with native DLNA support)

**Game Server — Minetest (Open-Source Sandbox)**\
Minetest is a lightweight open-source sandbox game that can run as a multiplayer server on a LAN.

- Install the Minetest server package
- Initialize a world and server configuration
- Configure server properties (server name, game mode, maximum players, etc.)

**Service of Your Choice**\
This option lets you propose another client-server network service that can run reliably on this hardware.

- Service must run reliably on the limited hardware of the Chromebook
- Must be installable using standard Linux tools (e.g., apt or official binaries)
- Must be client-server style and network-accessible from another device on the LAN
- You must demonstrate that it operates correctly and document how you configured it

### Tier 3 - Internet Layer Competencies (Advanced)

These demonstrate understanding of networking beyond the local subnet.

**DNS Sinkhole / Ad-Blocker — Pi-hole**\
Pi-hole is a local DNS server that provides network-wide ad blocking and domain filtering by intercepting and controlling DNS queries from client devices.

- Configure a client to use your server as its ONLY DNS server
- Demonstrate blocked ads or domains

**Mesh VPN — Tailscale**\
Tailscale is a VPN overlay network that creates secure, private connectivity between devices across the Internet.

- Access your server from a phone using cellular data (not school Wi-Fi)
- Alternately, you can leave your server at home and access it from school

**NAT Gateway — Port Forwarding (Home Network)**\
Port forwarding is a router configuration that maps incoming Internet traffic to a specific device and port on your home network.

- Configure your home router to forward external traffic to your server
- Demonstrate external access

## Required Workflow (Per Service)

For each selected service, you must perform and understand the following steps:

1. Install the software (apt)
2. Modify configuration files in `/etc/`
3. Restart the service using systemctl
4. Verify the service is listening locally
5. Verify access from a different device
6. Troubleshoot any issues encountered

## Final Deliverable: Server Documentation

Submit one Google Document containing a section for each service.

### For Each Service Include:

#### 1. Identity

- Service name
- Brief description of what the service does and/or what it provides to clients
- What resource or capability the service is delivering (e.g., webpages, files, remote access, time, media, etc.)

#### 2. Transport Details

- TCP or UDP
- Configured port number

#### 3. Local Network Evidence

Screenshot showing BOTH:

- `ip -br addr`
- A filtered port check showing ONLY your service in the LISTEN state, e.g., `sudo ss -ltnp | grep :PORT`

#### 4. Configuration Evidence

Screenshot(s) proving your configuration changes.

- Must clearly show the line(s) you added, changed, etc.
- Evidence must be captured from the terminal using commands such as `cat`, `less`, or `grep` (recommended)
- You may still use `nano` (or another terminal editor) to make the change, but your proof should show the final file contents in the terminal

#### 5. Remote Access Evidence

Screenshot(s) or photo(s) showing proof of access from a different device (laptop, phone, tablet)

- Web interface, terminal session, file browser, etc.
- Visual evidence should ideally show that server access is across LAN or WAN (e.g. server IP is visible in the browser address bar)

#### 6. Troubleshooting Log

Describe one real challenge, problem, or difficulty you encountered installing and configuring this service. Include how you fixed it, referencing:

- Symptoms
- Diagnostic commands used
- Root cause

If you did not encounter a real problem, demonstrate how you verified that the service was functioning correctly or describe how you would diagnose a failure.

## Academic Integrity

You may consult documentation and online resources. However:

- All configuration work must be performed by you
- Documentation must be written in your own words
- You must understand every command you use

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

## Assessment Rubric

This project will be evaluated based on both the successful deployment of network services and your demonstrated understanding of how they function within the TCP/IP model.

Achievement levels correspond approximately to Ontario grading bands:

- **Level 1:** 50–59%
- **Level 2:** 60–69%
- **Level 3:** 70–79%
- **Level 4 / 4+:** 80–100%

<br>

## Service Implementation & Functionality

**Assesses how successfully the selected services are installed, configured, customized, and made accessible from other devices.**

| Level | Descriptor |
|:-----:|------------|
| **4** | Four or more services are fully functional and reliably accessible. Configurations go beyond defaults and clearly demonstrate intentional customization. Includes a valid Internet-layer competency for 4+. |
| **3** | Four services are functional on the LAN with appropriate configuration changes. Minor issues may be present but do not prevent normal use. |
| **2** | Some services function, but others are incomplete, unreliable, or largely unchanged from default configuration. |
| **1** | Few services function correctly, or major configuration problems prevent reliable access. |


## TCP/IP Understanding (Layers & Ports)

**Assesses understanding of how each service operates within the TCP/IP model, including IP addressing, transport protocols, and ports.**

| Level | Descriptor |
|:-----:|------------|
| **4** | Demonstrates clear and accurate understanding of Internet, Transport, and Application layers, including how services use IP addressing and ports. Shows insight into reachability issues such as DNS, NAT, or routing for 4+. |
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
Updates, networking checks, choose services

**Day 2-3 - Implementation**\
Install and configure services

**Day 4 - Verification and Troubleshooting**\
Local and remote testing

**Day 5 - Documentation and Demonstration**\
Finalize report and submit

