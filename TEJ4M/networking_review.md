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

<br>

## 2. The TCP/IP Model (How to Think in Layers)

### Why We Use a Layered Model

Networking systems are complex. Many different tasks must occur for data to move successfully from one device to another: signals must be transmitted, devices must be addressed, data must be routed, and applications must interpret the information correctly.

Rather than treating networking as a single monolithic process, engineers divide responsibilities into layers. Each layer has a specific role, and each layer depends on the layer below it while serving the layer above it. This separation allows systems to be designed, implemented, and troubleshot in a structured way.

The model used throughout this course is the **TCP/IP model**, which consists of four layers.

### The Four Layers of the TCP/IP Model

From lowest to highest, the TCP/IP model consists of:

1. Physical/Link
2. Internet
3. Transport
4. Application

Each layer answers a different question:
- How does data physically move?
- How do devices find each other?
- How is data delivered reliably (or quickly)?
- What is the data actually used for?

### An Analogy: Roads, Vehicles, and Rules

A useful way to understand the TCP/IP model is to compare it to a road transportation system.

- **Physical/Link layer** is the road infrastructure itself: roads, lanes, intersections, and traffic lights. It defines how movement is physically possible.
- **Internet layer** is the addressing and routing system: street addresses, city names, and GPS directions that determine where vehicles need to go.
- **Transport layer** is the type of vehicle and delivery method: a courier truck, a motorcycle, or a convoy. Some deliveries prioritize speed, others prioritize reliability.
- **Application layer** is the purpose of the trip: delivering a package, transporting passengers, or providing a service.

Each layer operates independently. A delivery truck does not need to know how asphalt is poured, and a road does not care what is being transported.

### Physical/Link Layer

The Physical/Link layer is responsible for moving raw data between directly connected devices. It includes physical media such as Ethernet cables, fibre optic cables, and wireless radio signals, as well as the rules that govern how devices share those media.

At this layer, devices are identified using hardware addresses (**MAC addresses**). Communication is limited to the local network segment. This layer does not understand IP addresses, applications, or data meaning.

### Internet Layer

The Internet layer is responsible for logical addressing and routing. It determines whether data should remain within the local network or be forwarded to another network.

This is where IP addresses are used. The Internet layer does not guarantee delivery or correctness; it focuses on moving packets toward their destination using routers.

### Transport Layer

The Transport layer manages communication between applications running on different devices. It controls how data is broken into pieces, sent, and reassembled.

Two major transport approaches are used:
- **TCP**, which prioritizes reliability, ordering, and error recovery.
- **UDP**, which prioritizes speed and low overhead.

In the transportation analogy, TCP is like a tracked delivery service that confirms every package arrives intact, while UDP is like sending loose flyers to all homes in a neighbourhood where speed matters more than certainty.

### Application Layer

The Application layer is where network services live. This layer defines how applications format data and how users interact with networked systems.

Examples include web browsing, email, file sharing, and remote access. Encryption, session handling, and data formatting are handled here as part of the application itself.

### Why Layers Matter

Using a layered model allows engineers and technicians to reason about problems systematically. When something fails, it is possible to ask which layer is responsible rather than guessing randomly.

For example:
- If there is no signal, the problem is likely at the Physical/Link layer.
- If a device has no valid IP address, the problem is at the Internet layer.
- If data arrives but applications fail, the issue is likely at the Transport or Application layer.

Thinking in layers is essential for understanding, designing, and troubleshooting networks.

<br>


## 3. Devices on a Network (Switches, Routers, APs, Modems)

### Why Network Devices Matter

Networks are not simply collections of end devices connected by cables or wireless signals. Specialized network devices exist to manage how data moves, where it goes, and who is allowed to communicate.

Understanding what each device does, and more importantly which TCP/IP layer it operates at, is essential. Many networking errors come from confusing the roles of switches and routers or assuming all network devices perform the same function.

### Switches (Local Traffic Managers)

A switch operates at the **Physical/Link layer** of the TCP/IP model. Its primary job is to move data within a local network.

A switch examines **MAC addresses**, not IP addresses. When a device sends data on a local network, the switch determines which physical port leads to the destination device and forwards the data only to that port.

Key characteristics of switches:
- Connect devices within the same local network (LAN)
- Use MAC addresses to make forwarding decisions
- Do not route traffic between different networks
- Reduce unnecessary network traffic compared to older hub-based designs

If all devices involved are on the same LAN, a router is not required. The switch alone can deliver the data.

### Routers (Network Boundary Devices)

A router operates at the **Internet layer** of the TCP/IP model. Its role is to move data between different networks.

Routers make decisions based on **IP addresses**, not MAC addresses. When data needs to leave the local network, the router determines the next network hop and forwards the packet accordingly.

Key characteristics of routers:
- Connect different networks together
- Use IP addresses to make forwarding decisions
- Act as the default gateway for devices on a LAN
- Separate broadcast domains

Every device that communicates beyond its local network relies on a router, even if the user is unaware of it.

### Reinforcing the Layer Distinction (Switch vs Router)

A useful rule of thumb:
- If communication stays inside the local network, the **switch** is responsible.
- If communication leaves the local network, the **router** is involved.

Switches do not understand IP routes, and routers do not manage individual physical ports for end devices. Confusing these roles leads to incorrect assumptions about how data moves through a network.

### Wireless Access Points (Bridging Wired and Wireless)

A wireless access point (AP) operates primarily at the **Physical/Link layer**. Its job is to allow wireless devices to connect to a wired network.

An access point does not assign IP addresses or decide where traffic should go. It simply acts as a bridge between wireless devices and the wired LAN.

Key characteristics of access points:
- Provide wireless connectivity (802.11)
- Bridge wireless clients onto a wired LAN
- Do not perform routing on their own

Many consumer devices marketed as "wireless routers" are actually combinations of a router, switch, and access point in a single enclosure.

### Modems (Network Translators)

A modem connects a local network to an Internet Service Provider (ISP). Its role is to translate between the signalling used by the ISP and the signalling used inside the local network.

Modems typically operate at the **Physical/Link layer**, handling modulation and demodulation of signals. 

The term modem originates from its role in **mo**dulating and **dem**odulating an electrical signal.

Key characteristics of modems:
- Interface between the ISP and the local network
- Do not route traffic internally
- Often paired with a router for Internet access

In many modern installations, the modem and router are combined into a single device, which can obscure their distinct roles.


### Putting It All Together

A typical home or school network includes:
- End devices connected to a **switch** (wired or wireless)
- A **router** that connects the local network to other networks
- An **access point** that provides wireless connectivity
- A **modem** that connects the network to the ISP

Each device exists for a specific reason and operates at a specific layer. 


<br>

## 4. IP Addresses, MAC Addresses, and Why Both Exist

### Two Different Problems to Solve

For data to move across a network, two different questions must be answered:
1. Which device is this data ultimately meant for?
2. How does the data get delivered across the current physical network?

These questions are solved using two different types of addresses. Confusing them is one of the most common sources of misunderstanding in networking.

### MAC Addresses (Local Identity)

A MAC address is a hardware identifier assigned to a network interface. It is designed to uniquely identify a device on a local network segment.

MAC addresses operate at the **Physical/Link layer**. Switches rely on MAC addresses to deliver data to the correct device within a LAN.

Key properties of MAC addresses:
- Associated with a specific network interface
- Used only for local network communication
- Not routable across networks
- Typically fixed, though they can be software-modified

When a device sends data to another device on the same local network, the destination MAC address determines where the data is delivered.

### IP Addresses (Logical Location)

An IP address identifies a device’s location within a networked system of networks. It answers the question of where the device exists logically, not physically.

IP addresses operate at the **Internet layer**. Routers rely on IP addresses to forward packets between networks.

Key properties of IP addresses:
- Assigned by configuration or automatically (for example, via DHCP)
- Used for communication beyond the local network
- Can change depending on the network the device joins
- Structured to support routing and segmentation

Two devices on different networks can never communicate using MAC addresses alone. IP addressing is required.

### What Happens During Communication

When data is sent:
- The **IP address** determines where the data should go overall.
- The **MAC address** determines how the data is delivered on the current local network.

If the destination is on the same LAN, the sender delivers the data directly using the destination MAC address.

If the destination is on a different network, the sender forwards the data to the router’s MAC address instead. The router then takes responsibility for moving the packet closer to its final destination.

### The Role of the Default Gateway

The default gateway is the router a device uses when it needs to communicate outside its local network.

Devices do not attempt to discover the entire Internet. They simply send non-local traffic to the gateway and trust the routing infrastructure to handle the rest.

Without a valid default gateway, a device may appear connected but will be unable to reach external networks.

### Why This Matters

Understanding the separation between MAC addresses and IP addresses explains:
- Why switches and routers perform different roles
- Why ARP is necessary
- Why devices can change networks but still function

This distinction is foundational. In the next section, we will examine how devices automatically discover IP addresses and map IP addresses to MAC addresses using ARP and DHCP.

<br>

## 5. How Devices Find Each Other (ARP, DNS, DHCP)

### The Discovery Problem

Modern networks appear simple to users, but several discovery problems must be solved before communication can occur:
- A device needs an IP address that is valid on the current network.
- A device must be able to translate human-readable names into IP addresses.
- A device must be able to deliver data to the correct physical interface on the local network.

These problems are solved by three core mechanisms: DHCP, DNS, and ARP. Each operates at a different stage and serves a distinct purpose.

### DHCP (Automatic IP Address Assignment)

Dynamic Host Configuration Protocol (DHCP) is responsible for automatically assigning IP configuration to devices when they join a network.

When a device connects to a network, it does not initially know:
- Its IP address
- The subnet it belongs to
- The default gateway
- The DNS servers it should use

DHCP solves this by allowing the device to request configuration information from a DHCP server, which is typically built into a router on small networks.

Key characteristics of DHCP:
- Operates at the Internet and Application layers
- Assigns IP addresses temporarily (leases)
- Prevents address conflicts
- Allows devices to move between networks without manual reconfiguration

Without DHCP, networks would require manual IP configuration for every device, which does not scale beyond very small setups.

### DNS (Name Resolution)

Domain Name System (DNS) translates human-readable names into IP addresses.

Users interact with names such as `www.example.com`, but networks operate using IP addresses. DNS acts as a lookup system that bridges this gap.

When a user enters a website address:
- The device queries a DNS server for the corresponding IP address.
- The DNS server responds with the IP address.
- The device then initiates communication using that IP address.

Key characteristics of DNS:
- Operates at the Application layer
- Does not transfer website data itself
- Is required for most Internet usage, but not for direct IP communication

If DNS fails, devices may still be connected to the Internet but will be unable to access services by name.

### ARP (Mapping IP Addresses to MAC Addresses)

Address Resolution Protocol (ARP) maps IP addresses to MAC addresses on the local network.

When a device needs to send data to another device on the same LAN, it must know the destination MAC address. The IP address alone is not sufficient for local delivery.

ARP works by:
- Broadcasting a request asking which device owns a given IP address
- Receiving a response containing the corresponding MAC address
- Caching the result for future use

Key characteristics of ARP:
- Operates at the boundary between the Physical/Link and Internet layers
- Used only within the local network
- Never crosses a router

ARP is one of the most commonly misunderstood mechanisms, yet it is essential for all local network communication.

### How These Mechanisms Work Together

In a typical scenario:
1. A device joins a network and uses DHCP to obtain an IP address.
2. The user enters a website address.
3. DNS resolves the name to an IP address.
4. The device determines whether the destination is local or remote.
5. ARP is used to identify the correct MAC address for local delivery.
6. Data transmission begins.

Each step depends on the previous one. Failure at any stage prevents communication, even if the physical connection appears to be working.

### Why This Matters

Understanding DHCP, DNS, and ARP explains many common networking issues, including:
- Devices that connect but cannot reach the Internet
- Situations where some websites load and others do not
- Problems caused by incorrect gateways or DNS servers

These mechanisms are foundational. In the next section, we will examine how data is transported reliably or quickly using TCP and UDP.

<br>

## 6. Moving Data Reliably (TCP vs UDP)

### The Transport Problem

Once devices are addressed and able to find each other, another question remains: how should data actually be delivered between applications?

Different applications have different priorities. Some require accuracy and completeness, while others value speed and low delay. The Transport layer exists to manage these tradeoffs.

At this layer, the network is no longer concerned with cables, signals, or routing paths. The focus shifts to communication between applications running on different devices.

### The Role of the Transport Layer

The Transport layer is responsible for:
- Breaking data into manageable pieces
- Delivering data to the correct application on the destination device
- Managing ordering, reliability, and error handling when required

This is accomplished using transport protocols. The two most important are TCP and UDP.

### TCP (Transmission Control Protocol)

TCP is designed for reliability.

Before data is sent, TCP establishes a connection between the source and destination. During transmission, it tracks which pieces of data have arrived and which need to be retransmitted. Data is delivered to the application in the correct order.

Key characteristics of TCP:
- Connection-oriented
- Guarantees delivery
- Ensures correct ordering of data
- Performs error detection and recovery
- Slower due to additional overhead

TCP is used when accuracy matters more than speed.

Common TCP-based applications include:
- Web browsing (HTTP/HTTPS)
- Email
- File transfers

### UDP (User Datagram Protocol)

UDP is designed for speed and simplicity.

UDP sends data without establishing a connection and without checking whether packets arrive. There is no retransmission or ordering guarantee. Any necessary error handling is left to the application itself.

Key characteristics of UDP:
- Connectionless
- No delivery guarantee
- No ordering guarantee
- Minimal overhead
- Lower latency

UDP is used when timeliness matters more than perfect accuracy.

Common UDP-based applications include:
- Live audio and video streaming
- Online gaming
- Voice over IP (VoIP)

### Choosing Between TCP and UDP

Neither protocol is universally better. Each exists to support different application requirements.

A general guideline:
- Use TCP when data must arrive correctly and completely.
- Use UDP when late or missing data is less harmful than delay.

For example, a dropped packet in a file transfer is unacceptable, but a dropped packet in a live video stream may go unnoticed.

### Why This Matters

Understanding the difference between TCP and UDP explains:
- Why some applications feel responsive but occasionally glitch
- Why others feel slower but more reliable
- Why transport behaviour is tied to application design, not network quality alone

In the next section, we will examine wireless networking and how data is transmitted without physical cables.

<br>

## 7. Wireless Networks (802.11 at a Conceptual Level)

### How Wireless Networking Is Different

Wireless networking solves the same fundamental problem as wired networking: moving data between devices. However, the medium used for communication is fundamentally different.

Instead of electrical signals on copper or light pulses in fibre, wireless networks use radio signals transmitted through shared airspace. This difference introduces constraints and behaviours that do not exist in wired networks.

Understanding these constraints explains why wireless networks can feel less predictable than wired ones, even when configured correctly.

### The Shared Medium Problem

In a wired network, each device typically has a dedicated physical connection to a switch. Multiple conversations can occur simultaneously without interference.

In a wireless network, all devices connected to the same access point share the same radio channel. Only one device can successfully transmit at a time. Others must wait.

This leads to several consequences:
- Bandwidth is shared among all connected devices
- More devices increase contention and delay
- Interference affects all devices using the same channel

Wireless performance is therefore influenced not just by signal strength, but by how many devices are competing for access.

### Role of the Wireless Access Point

A wireless access point (AP) acts as a bridge between the wired LAN and wireless clients.

At a conceptual level, the access point:
- Coordinates access to the shared radio channel
- Receives wireless frames and forwards them onto the wired network
- Receives wired frames and transmits them wirelessly to clients

The access point does not route traffic or assign IP addresses on its own. Those functions belong to routers and DHCP services elsewhere on the network.

### 802.11 and Network Identification

Wireless networks that follow the 802.11 standard are commonly referred to as Wi-Fi networks.

Each wireless network advertises a **Service Set Identifier (SSID)**, which is the human-readable network name users see when connecting.

Important characteristics of SSIDs:
- Case sensitive
- Do not provide security on their own
- Used only for identification, not encryption

Security is provided separately through authentication and encryption mechanisms layered on top of 802.11.

### Wireless Security at a High Level

Because wireless signals extend beyond physical walls, security is a critical concern.

Modern wireless networks typically use:
- Authentication to verify which devices are allowed to connect
- Encryption to protect data transmitted over the air

Without encryption, wireless traffic can be intercepted by any device within range.

### Why Wireless Feels Less Reliable

Wireless networks are affected by factors that do not impact wired networks, including:
- Physical obstructions
- Distance from the access point
- Interference from other wireless devices
- Channel congestion

These factors can cause variability in performance even when configuration is correct.

### Why This Matters

Understanding wireless behaviour explains:
- Why moving closer to an access point improves performance
- Why adding more devices can slow a network
- Why wired connections are still preferred for critical systems

In the next section, we will examine what happens when networking problems occur and how basic diagnostic tools are used to identify where failures happen.

<br>

## 8. What Happens When Something Breaks (Basic Diagnostics)

### Why Diagnostics Matter

Networks rarely fail in obvious ways. More often, they appear partially functional: a device connects to Wi-Fi but cannot load websites, or some services work while others do not.

Effective troubleshooting depends on understanding how the network is structured and which layer is responsible for each task. Guessing randomly is inefficient. A systematic approach saves time and reduces errors.

### Thinking in Layers

When diagnosing a network problem, the most important habit is to think in layers.

Rather than asking “What is broken?”, a better question is:
- At which layer is communication failing?

Each layer has distinct responsibilities, and failures at lower layers prevent higher layers from functioning.

A simplified diagnostic progression:
1. Is there a physical or wireless connection?
2. Does the device have a valid IP configuration?
3. Can the device reach other networks?
4. Can applications successfully communicate?

### Common Symptoms and Likely Causes

Some typical examples:
- No network connection at all: likely a Physical/Link layer issue
- Connected to Wi-Fi but no Internet access: often an Internet layer issue (IP address, gateway, or routing)
- Internet access works by IP address but not by name: DNS issue
- Slow or unreliable performance in real-time applications: Transport layer considerations (often UDP-related)

Recognizing these patterns allows problems to be narrowed down quickly.

### Basic Diagnostic Tools

Several simple tools are commonly used to observe network behaviour.

#### ipconfig

The `ipconfig` command displays a device’s IP configuration.

It can be used to check:
- Whether the device has an IP address
- Whether the address appears valid for the network
- Whether a default gateway is present

An address in the range `169.254.x.x` indicates that the device failed to obtain an address via DHCP.

#### ping

The `ping` command tests basic reachability between devices.

It works by sending small messages and measuring whether responses are received.

Ping can help determine:
- Whether a device is reachable
- Whether delays or packet loss are occurring

Successful ping responses indicate that lower network layers are functioning.

#### tracert

The `tracert` command shows the path data takes as it moves across networks.

Each step represents a router along the path. This tool helps identify where communication stops or slows down.

Tracert is useful for distinguishing local network issues from wider routing problems.

### Putting It All Together

Effective diagnostics combine:
- Knowledge of network structure
- Awareness of layer responsibilities
- Targeted use of diagnostic tools

Most networking problems are not mysterious. They follow predictable patterns tied to how networks are designed.

### Final Perspective

Understanding how networks work is not about memorizing commands or configurations. It is about reasoning clearly about systems.

When you can identify which layer is responsible for a failure, you are no longer guessing. You are diagnosing.