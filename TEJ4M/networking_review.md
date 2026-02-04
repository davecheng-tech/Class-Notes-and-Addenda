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

