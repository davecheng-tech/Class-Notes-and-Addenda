# Networking Review

## Table of Contents

- What a Network Is (and Is Not)
- The TCP/IP Model (How to Think in Layers)
- Devices on a Network (Switches, Routers, APs, Modems)
- IP Addresses, MAC Addresses, and Why Both Exist
- How Devices Find Each Other (ARP, DNS, DHCP)
- Moving Data Reliably (TCP vs UDP)
- Wireless Networks (802.11 at a Conceptual Level)
- What Happens When Something Breaks (Basic Diagnostics)

## 1. What a Network Is (and Is Not)

### What a Network Is

A computer network is a collection of two or more devices connected for the purpose of communication and resource sharing. The defining feature of a network is the ability for data to move between devices in an organized and predictable way.

Devices on a network may include computers, mobile devices, servers, printers, appliances, and smart home electronics. What matters is not the type of device, but the fact that it can send, receive, and interpret data.

Common resources shared over networks include:
- Internet connectivity
- Files and storage
- Printers and peripherals
- Web services and applications
- Audio and video streams

If devices are physically connected but cannot exchange data meaningfully, the network is not functioning.

### What a Network Is Not

A network should not be confused with any single component or technology.

A network is not:
- The Internet itself
- Wi-Fi specifically
- A single cable or wireless signal
- A group of devices located near each other

Clarifying these distinctions is important. The Internet is a global network made up of many interconnected networks. Wi-Fi is only one method of connecting devices; many networks rely entirely on wired connections. A single device, regardless of how powerful, does not form a network on its own.

For a network to exist, three conditions must be met:
1. Multiple devices must be present.
2. There must be a physical or wireless means of connection.
3. The devices must follow agreed-upon rules that govern communication.

### Types of Networks (By Scope)

Networks are often classified by the size of the area they cover.

A **Local Area Network (LAN)** connects devices within a limited physical space, such as a home, classroom, office, or school.

A **Wide Area Network (WAN)** connects multiple LANs across larger geographic distances. The Internet is the most well-known example of a WAN.

These labels describe scale, not quality or speed. Both LANs and WANs can use wired or wireless technologies.

### Why Networks Exist

Networks exist to make computing practical at scale. They allow information to be shared quickly, hardware resources to be reused, and services to be centralized. Many modern systems assume the presence of a network and are designed to operate poorly or not at all without one.

From cloud storage to real-time communication, networking is a foundational layer beneath most modern software systems.

### A Guiding Principle

Networks operate according to structure and rules. 

Whenever data is transmitted:
- The source and destination must be identifiable.
- A path must exist between them.
- The data must be packaged, transmitted, and interpreted correctly.

Understanding how these responsibilities are divided is essential. In the next section, we will introduce the TCP/IP model, which provides a layered way to reason about how networks function. 


