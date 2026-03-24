# Processor Architecture

This note introduces processor architecture: what it is, why it matters, and how to identify it on your own machine. It covers:

- What a processor architecture actually is
- The two major families: x86-64 and ARM
- Where each architecture appears in real devices
- Why architecture affects software compatibility and performance
- How architecture relates to emulation
- Reading hardware information from the terminal

<br>

## 1. What Is Processor Architecture?

Every processor executes **instructions**: operations like "add these two numbers," "store this value in memory," or "jump to this address if the result was zero." The complete set of instructions a processor understands, and the rules for how those instructions are encoded, is called its **instruction set architecture (ISA)**, or simply its **architecture**.

Different processor families use different instruction sets. A program compiled for one architecture produces machine code that a processor of a different architecture cannot understand or execute directly. Architecture is the fundamental language a CPU speaks.

This is why you cannot take a Windows `.exe` file compiled for a PC and run it natively on an iPhone, or take an app compiled for an Apple M1 Mac and run it unchanged on an older Intel Mac. The machine code is different.

### Why Architecture Is Not Just a Technical Detail

Architecture determines:

- **What software can run on a device:** software must be compiled for the target architecture
- **How efficient a chip can be:** some architectures are designed for performance, others for low power consumption
- **What hardware can run what operating systems:** an OS must also be compiled for the target architecture
- **Whether emulation is needed:** running software designed for a different architecture requires a translation layer

<br>

## 2. The Two Major Families: x86-64 and ARM

### x86-64

The **x86** architecture traces back to Intel's 8086 processor from 1978. Over decades, Intel and AMD extended it while maintaining backwards compatibility, meaning software written for older chips continued to work on newer ones. The modern 64-bit version is called **x86-64** (also written as AMD64, since AMD introduced the 64-bit extensions).

x86-64 has dominated desktop computers, laptops, and servers for decades. It belongs to a design philosophy called **CISC** (Complex Instruction Set Computing), which uses a large number of specialized instructions.

x86-64 processors tend to prioritize raw computational performance and are found in environments where power consumption is a secondary concern: plugged-in laptops, desktop workstations, and data centres.

### ARM

**ARM** (originally Acorn RISC Machine) takes a different approach: **RISC** (Reduced Instruction Set Computing), which uses a smaller, simpler set of instructions that can be executed more efficiently per clock cycle and per watt of power consumed.

ARM processors have dominated mobile devices for decades. Every major smartphone chip (Apple's A-series, Qualcomm Snapdragon, Samsung Exynos) is an ARM processor. The 64-bit version of the ARM instruction set is called **AArch64**, sometimes also written as **ARM64**.

In 2020, Apple transitioned its Mac lineup from Intel x86-64 to their own ARM-based chips, the **Apple Silicon** series (M1, M2, M3, M4). This was a significant shift: for the first time, a major PC platform moved from x86-64 to ARM at scale.

> [!NOTE]
> The terms AArch64, ARM64, and Apple Silicon all refer to 64-bit ARM architecture. AArch64 is the technical specification name; ARM64 is used colloquially; Apple Silicon refers specifically to Apple's custom ARM chips.

<br>

## 3. Architecture in the Devices Around You

The table below shows common devices, their processors, and the architecture they use.

| Device | Processor | Architecture | Notes |
|---|---|---|---|
| Acer C720 Chromebook (our machines) | Intel Celeron 2955U | x86-64 | Haswell microarchitecture, released 2013 |
| Desktop PC / most Windows laptops | Intel Core or AMD Ryzen | x86-64 | Consumer x86-64 |
| MacBook / iMac (2020 and later) | Apple M1, M2, M3, M4 | ARM64 (AArch64) | Apple Silicon; ARM with desktop-class performance |
| MacBook / iMac (pre-2020) | Intel Core | x86-64 | Apple used Intel before the ARM transition |
| iPhone | Apple A-series (A17, A18, etc.) | ARM64 (AArch64) | Same ISA as Apple Silicon Macs |
| Android phone (most models) | Qualcomm Snapdragon | ARM64 (AArch64) | Snapdragon is ARM-licensed |
| Android phone (Samsung flagship) | Samsung Exynos | ARM64 (AArch64) | Also ARM-licensed |
| Raspberry Pi 4 / 5 | Broadcom BCM2711/BCM2712 | ARM64 (AArch64) | Common in embedded and hobby projects |
| Nintendo Switch | Nvidia Tegra X1 | ARM64 (AArch64) | ARM in a gaming console |
| Original NES | Ricoh 2A03 (based on MOS 6502) | 6502 | 8-bit; not x86 or ARM |
| Game Boy / Game Boy Color | Sharp LR35902 | Custom (Z80-like) | 8-bit; unique to Nintendo hardware |
| SNES | Ricoh 5A22 (based on 65816) | 65816 | 16-bit extension of the 6502 family |

Notice that nearly every mobile device uses ARM, while most general-purpose desktop and server hardware still uses x86-64. The retro gaming consoles in the bottom rows use entirely different, older architectures. That will be relevant context for later in this unit.

<br>

## 4. Why Architecture Matters

### Software Compatibility

When software is **compiled**, source code (like Java, C, or C++) is translated into machine code for a specific architecture. That compiled binary only runs natively on processors that understand its instruction set.

This means:
- A program compiled for x86-64 will not run natively on an ARM processor
- An app built for ARM64 will not run natively on x86-64
- Installing software on Linux with `apt` pulls packages compiled for your architecture; the package manager handles this automatically
- Docker images are also architecture-specific; an image built for x86-64 will not run on an ARM machine unless specifically handled

> [!IMPORTANT]
> When you see errors like "Exec format error" or "wrong architecture" in Linux, it almost always means you are trying to run a binary compiled for a different architecture than your machine.

Apple's Rosetta 2 translation layer allows x86-64 binaries to run on Apple Silicon Macs, but this is software emulation, not native execution. It works, but it has a performance cost.

### Performance and Power Efficiency

The design goals of x86 and ARM reflect the environments they were built for:

- **x86-64** was designed for performance-first computing, connected to wall power. More complex instructions can do more work per instruction, but each instruction consumes more power.
- **ARM** was designed for battery-powered devices. Simpler, more uniform instructions execute efficiently, generating less heat and consuming less power.

Apple's M-series chips demonstrated that this tradeoff is not fixed. A well-designed ARM chip can match or exceed x86 performance in many workloads while still consuming far less power.

### Emulation

**Emulation** is software that simulates a different hardware platform, including a different processor architecture. An emulator translates the instructions of the target machine into instructions the host machine can execute.

This is computationally expensive: the host processor is doing its own work *and* simulating another processor's work at the same time.

The classic example: running a Nintendo Entertainment System emulator on your laptop. The NES contained a Ricoh 2A03 processor based on the MOS 6502, a completely different architecture from x86-64 or ARM64. An NES emulator does not run NES software directly. It reads the original machine code, understands what the 6502 would have done, and produces equivalent results on your x86-64 or ARM processor.

> [!NOTE]
> Emulation is the technical foundation for the capstone project later in this unit. When you install a video game emulator, you are installing software that translates one CPU's instruction set for another. Understanding architecture is what makes that make sense.

<br>

## 5. Reading Your Machine from the Terminal

The following commands let you inspect your machine's hardware directly from the Linux terminal. These are useful for understanding what you are working with before installing software, debugging compatibility issues, or documenting a system. These commands are Linux-specific and will not work on macOS or Windows as written — though each has an equivalent if you are curious enough to look.

### `uname -m`: Architecture

```bash
uname -m
```

This prints the machine hardware name, specifically the architecture of the running kernel.

**On our Chromebooks:**
```
x86_64
```

On an Apple Silicon Mac you would see `arm64`. On a Raspberry Pi or Android device running Linux you would see `aarch64`.

> **On macOS:** `uname -m` works identically — it is a standard Unix command, not Linux-specific.  
> **On Windows:** `$env:PROCESSOR_ARCHITECTURE` in PowerShell returns similar information.

---

### `lscpu`: Processor Details

```bash
lscpu
```

`lscpu` reads from the kernel's CPU information and displays a structured summary.

**Partial output on our Chromebooks:**
```
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         39 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  2
  On-line CPU(s) list:   0,1
Vendor ID:               GenuineIntel
  Model name:            Intel(R) Celeron(R) CPU 2955U @ 1.40GHz
    CPU family:          6
    Model:               69
    Thread(s) per core:  1
    Core(s) per socket:  2
    Socket(s):           1
```

Key fields to understand:

| Field | Meaning |
|---|---|
| `Architecture` | The ISA: `x86_64`, `aarch64`, `armv7l`, etc. |
| `CPU(s)` | Total logical processors (cores × threads) |
| `Model name` | The specific chip, including clock speed |
| `Core(s) per socket` | Physical cores on the die |
| `Thread(s) per core` | Logical threads per core (Intel Hyper-Threading = 2; this Celeron = 1) |
| `Vendor ID` | `GenuineIntel` or `AuthenticAMD` for x86; ARM chips show the implementer code |

> **On macOS:** `sysctl -n machdep.cpu.brand_string` prints the CPU model name; `sysctl -a | grep machdep.cpu` gives a fuller dump.  
> **On Windows:** `wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors` in Command Prompt, or `Get-WmiObject Win32_Processor` in PowerShell.

---

### `free -h`: Memory

```bash
free -h
```

`free` reports on system memory. The `-h` flag formats values in human-readable units (MB, GB).

**Output on our Chromebooks:**
```
               total        used        free      shared  buff/cache   available
Mem:           3.7Gi       1.1Gi       1.8Gi        45Mi       820Mi       2.5Gi
Swap:          3.9Gi          0B       3.9Gi
```

| Column | Meaning |
|---|---|
| `total` | Total installed RAM |
| `used` | Currently in use by processes |
| `free` | Unused and not allocated |
| `buff/cache` | Used by the OS for disk caching (can be reclaimed) |
| `available` | Realistically available for new processes (`free` + reclaimable cache) |
| `Swap` | Disk space used as overflow when RAM is full |

> [!NOTE]
> The `available` value is more useful than `free` in practice. Linux aggressively uses spare RAM for caching, which makes `free` appear low even on an idle machine.

> **On macOS:** `vm_stat` shows raw memory page counts; `top -l 1 | grep PhysMem` gives a more readable one-line summary.  
> **On Windows:** `wmic OS get FreePhysicalMemory,TotalVisibleMemorySize` in Command Prompt, or `Get-WmiObject Win32_OperatingSystem` in PowerShell.

---

### `lsblk`: Storage Devices

```bash
lsblk
```

`lsblk` lists **block devices**: storage devices that the OS reads and writes in fixed-size blocks. This includes SSDs, HDDs, USB drives, and SD cards.

**Output on our Chromebooks:**
```
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda      8:0    0  29.8G  0 disk
├─sda1   8:1    0   512M  0 part /boot/efi
├─sda2   8:2    0     1G  0 part /boot
└─sda3   8:3    0  28.3G  0 part /
```

| Column | Meaning |
|---|---|
| `NAME` | Device name (`sda` = first disk; `sda1`, `sda2` = partitions) |
| `SIZE` | Capacity of the device or partition |
| `TYPE` | `disk` = physical device; `part` = partition |
| `MOUNTPOINTS` | Where in the filesystem this device is accessible |

The C720 machines have a single SSD (`sda`) divided into three partitions: an EFI boot partition, a `/boot` partition for the kernel, and the root filesystem (`/`) where the OS lives.

> [!TIP]
> `lsblk` is the first command to run when troubleshooting storage. It shows you exactly what devices exist and how they are partitioned, without modifying anything.

> **On macOS:** `diskutil list` shows all disks and their partition layout.  
> **On Windows:** `wmic diskdrive list brief` in Command Prompt, or `Get-Disk` in PowerShell.

<br>

## 6. Key Terms

| Term | Definition |
|---|---|
| **Architecture (ISA)** | The instruction set a processor understands; the "language" of the CPU |
| **x86-64** | 64-bit extension of Intel's x86 architecture; used in most PCs and servers |
| **ARM / AArch64** | A RISC architecture dominant in mobile devices, Apple Silicon, and embedded systems |
| **CISC** | Complex Instruction Set Computing; uses many specialized instructions (x86) |
| **RISC** | Reduced Instruction Set Computing; uses fewer, simpler instructions (ARM) |
| **Emulation** | Software that simulates a different hardware platform, translating one CPU's instructions for another |
| **Compilation** | Translating source code into machine code for a specific architecture |
| **Binary** | Compiled executable; machine code tied to a specific architecture |
| **Block device** | A storage device the OS accesses in fixed-size blocks (SSD, HDD, USB) |
| **Swap** | Disk space used as an overflow extension of RAM when physical memory is full |
