# Retro Computing Exploration

Today you will explore real operating systems and computers from the 1980s and 1990s — running in your browser, on actual emulated hardware.

This is not a worksheet. There are no marks. Poke around, break things, and see what you discover.

<br>

## The Hardware Behind the Software

Every machine in this exploration is running on emulated real hardware. The processor, RAM, display adapter, and disk controller are all faithfully reproduced — the software has no idea it isn't running on actual 1980s components.

The machines you'll encounter today span one of the most dramatic hardware generations in computing history:

| Processor | Year | Word size | Clock speed | Appears in |
|-----------|------|-----------|-------------|------------|
| Intel 8088 | 1979 | 16-bit (8-bit bus) | 4.77 MHz | IBM PC 5150, PC XT |
| Motorola 68000 | 1979 | 32-bit internal / 16-bit bus | 8 MHz | Apple Macintosh 128K |
| Intel 80286 | 1982 | 16-bit protected mode | 6–12 MHz | IBM PC AT |
| Intel 80386 | 1985 | 32-bit, virtual memory | 16–33 MHz | COMPAQ DeskPro 386 |

The Intel x86 line — 8088 → 286 → 386 — is the direct ancestor of the x86-64 processors in your Chromebook. Every Intel and AMD processor today is still backwards-compatible with code written for the 8088 in 1981.

The Motorola 68000 in the Macintosh was a completely separate architecture — faster in some ways, with a cleaner design — but it lost the market battle entirely. By the mid-1990s, the PC had won.

<br>

---

## The Story

Personal computing didn't start with a plan. It started with a series of accidents, rivalries, lawsuits, and missed opportunities.

In 1981, IBM launched the IBM PC with Intel's 8088 processor. They needed an operating system quickly and approached a company called Digital Research, whose CP/M was already the dominant OS for personal computers. That meeting fell apart — and IBM ended up licensing DOS from Microsoft instead. That one decision changed everything.

Three years later, Apple released the Macintosh — the first affordable computer with a graphical interface and a mouse, running on a Motorola processor that had nothing to do with IBM. It was a completely different vision of computing.

Microsoft spent the next decade trying to match the Mac's GUI on IBM-compatible hardware. The result was Windows 1.0, then 2.0 (and a lawsuit), then a detour through a failed IBM collaboration, then Windows 3.1, then finally Windows 95.

By 1995, the modern desktop was essentially invented. Everything since has been refinement.

<br>

---

## 1. Apple Macintosh — System 1.0 (1984)

**[Open in browser →](https://infinitemac.org/)**

*Macintosh 128K · Motorola 68000 @ 8 MHz · 128 KB RAM · 9" monochrome display*

The original Macintosh. Everything — the OS, the apps — fit on a single 400 KB floppy disk.

The Motorola 68000 was a genuine 32-bit processor with a clean instruction set that many engineers considered superior to Intel's 8088. Apple chose it specifically because it was powerful enough to drive a graphical interface at interactive speeds. The 128 KB of RAM was tight by design — Steve Jobs insisted on keeping the machine affordable.

This was the first time most people had ever seen a computer with windows, icons, and a mouse. It was also the first consumer computer with proportional fonts on screen. Before this, everything on a screen was fixed-width characters on a grid.

**Try this:**
- Open **MacPaint** and draw something. This was a flagship app that showed off what a mouse could do.
- Open **MacWrite** and type a few sentences. Notice the font rendering — this is a bitmap font drawn pixel by pixel, not the vector fonts we use today.
- Notice the CPU: 8 MHz, 128 KB RAM. A single emoji image today is larger than the entire Macintosh operating system.

<br>

---

## 2. IBM PC — CP/M-86 (1981 hardware)

**[Open in browser →](https://www.pcjs.org/software/pcx86/sys/cpm/1.00/)**

*IBM PC Model 5150 · Intel 8088 @ 4.77 MHz · 256 KB RAM · MDA (monochrome text only)*

Before DOS, there was **CP/M**.

Gary Kildall of Digital Research created CP/M in 1974, and by 1980 it was the standard operating system for personal computers. When IBM was building the IBM PC, they needed an OS — and CP/M was the obvious choice. IBM sent a team to meet with Kildall. The meeting collapsed. Accounts differ: Kildall may have been out flying his plane; his wife and lawyer may have refused to sign IBM's non-disclosure agreement. Whatever the reason, IBM left without a deal.

IBM went to Bill Gates instead. Microsoft didn't have an operating system either — Gates bought one from a small Seattle company for $50,000 and licensed it to IBM as PC-DOS. That OS became MS-DOS. That $50,000 deal eventually made Microsoft the most valuable company in the world.

CP/M-86 was Digital Research's attempt to port CP/M to the 8086/8088 processor and compete with DOS. It largely failed. By 1983, DOS had won.

The IBM PC 5150 used the Intel 8088 — a cost-reduced variant of the 8086 with a 16-bit internal architecture but only an 8-bit external data bus. IBM chose it over the full 8086 because it was cheaper and worked with existing 8-bit support chips. That decision set the cost-vs-capability tradeoff that defined IBM-compatible PCs for years.

**Try this:**
- Type `dir` to list files.
- Notice: this feels almost identical to DOS below. CP/M and DOS used very similar commands — MS-DOS deliberately imitated CP/M's interface to ease the transition for existing users.
- Think about the alternate history: if this had won instead of DOS, Microsoft might not exist.

<br>

---

## 3. IBM PC XT — PC DOS 3.20 (1983 hardware, 1986 OS)

**[Open in browser →](https://www.pcjs.org/machines/pcx86/ibm/5160/vga/)**

*IBM PC XT Model 5160 · Intel 8088 @ 4.77 MHz · 640 KB RAM · IBM VGA*

The IBM PC XT was an upgraded PC 5150 — same 8088 processor, but with a 10 MB hard disk and up to 640 KB of RAM. The "640 KB barrier" became famous: DOS and the 8088's memory addressing limited usable RAM to 640 KB, which seemed enormous in 1981 but became a crippling constraint by the late 1980s.

DOS itself is a purely text-based environment. No mouse. No icons. Just a blinking cursor and a command prompt.

**Try this:**
- Type `dir` and press Enter — this lists files (equivalent to `ls` in Linux).
- Type `cd GAMES` then `dir` to see what's available, then try running something.
- Notice the file extensions: `.EXE`, `.COM`, `.BAT` — these are DOS executable formats. `.COM` files are the older format; `.EXE` files support more memory and features.

> [!NOTE]
> DOS commands (`dir`, `cd`, `copy`, `del`) are the direct ancestors of the Windows Command Prompt (`cmd.exe`). Linux commands (`ls`, `cd`, `cp`, `rm`) serve identical purposes with different names. Both traditions trace back to the same era of computing. The reason they differ is that Linux descended from Unix, which predates DOS and had its own conventions.

<br>

---

## 4. Microsoft Windows 1.0 (1985)

**[Open in browser →](https://www.pcjs.org/software/pcx86/sys/windows/1.00/)**

*IBM PC XT · Intel 8088 @ 4.77 MHz · 640 KB RAM · IBM EGA*

Microsoft's first attempt at a graphical interface. Windows 1.0 ran on top of DOS — it was a shell, not a real operating system. It was also constrained by the 8088's limitations: with only 640 KB of RAM and a 4.77 MHz processor, there wasn't much room for a GUI.

Windows couldn't even overlap windows. They could only tile side by side, like bathroom tiles — because the system didn't have enough memory to keep track of what was underneath an overlapping window.

Apple noticed the similarities to the Mac's interface and quietly noted it. They would sue two years later.

**Try this:**
- Open a few programs from the MS-DOS Executive (the file manager).
- Try to move and resize windows. Confirm they can't overlap.
- Open **Reversi** — one of the few games that shipped with Windows 1.0.
- Compare this honestly to the Mac above. The Mac shipped in 1984. This shipped in 1985. Why does the Mac feel so much more polished?

<br>

---

## 5. Microsoft Windows/386 2.01 (1987)

**[Open in browser →](https://www.pcjs.org/software/pcx86/sys/windows/2.0x/)**

*COMPAQ DeskPro 386 · Intel 80386 @ 16 MHz · 2 MB RAM · IBM VGA*

Notice the hardware jump. This machine has a **386 processor** — Intel's first true 32-bit CPU, released in 1985. Clock speed up from 4.77 MHz to 16 MHz. RAM up from 640 KB to 2 MB. This is a fundamentally more capable machine than anything above.

Windows 2.0 finally allowed overlapping windows. It also introduced keyboard shortcuts and desk accessories — features the Mac had had since 1984.

Apple sued.

The lawsuit — *Apple Computer, Inc. v. Microsoft Corporation* — argued that Microsoft had copied the "look and feel" of the Macintosh GUI. It dragged on until 1994. Microsoft ultimately won on a technicality: Apple had previously licensed some GUI elements to Microsoft for Windows 1.0, and the court ruled that license covered Windows 2.0 as well. The case established that you cannot copyright a user interface concept — only specific implementations.

**Try this:**
- Confirm that windows now overlap. This was worth a lawsuit.
- Open a few applications and compare the interface to Windows 1.0 above.
- Notice the machine: a 386 at 16 MHz. This is the same processor family that will run Windows 95 eight years later — just slower and with less RAM.

<br>

---

## 6. IBM OS/2 1.0 (1987)

**[Open in browser →](https://www.pcjs.org/software/pcx86/sys/os2/ibm/1.0/)**

*IBM PC AT · Intel 80286 @ 8 MHz · 2 MB RAM · 20 MB Hard Disk · IBM EGA*

In 1985, IBM and Microsoft agreed to jointly develop a successor to DOS — a real, modern operating system that would take full advantage of the 80286 processor's protected mode. They called it OS/2.

The 80286 introduced **protected mode**: a hardware feature that let the processor protect memory regions from each other, so one program crashing couldn't bring down the whole system. DOS never used protected mode at all. OS/2 was designed around it.

The IBM/Microsoft partnership collapsed in 1990. Microsoft had secretly been developing Windows for the consumer market while IBM focused on OS/2 for businesses. When Windows 3.1 took off in 1992 and Windows 95 dominated in 1995, OS/2 was left behind — even though it was technically superior in several ways. IBM's OS/2 Warp (1994) was actually more stable and more capable than Windows 95, but Microsoft had the software ecosystem and the marketing. OS/2 is still used today in some ATMs and point-of-sale terminals.

> [!NOTE]
> OS/2 1.0 used the 80286 processor's protected mode, but the 286's protected mode had a significant limitation: you could switch *into* protected mode, but switching back to real mode (required for DOS compatibility) required a hardware reset. The 80386 fixed this with a cleaner protected mode implementation — which is partly why Windows 2.0 ran on the 386 rather than the 286.

**Try this:**
- Explore the interface. OS/2 1.0 is character-based (no GUI yet — that came in OS/2 1.1 with Presentation Manager).
- Try running a few programs.
- Think about what you know about protected mode and memory management: this OS was designed to use hardware features that DOS completely ignored.

<br>

---

## 7. Apple Macintosh — System 7.5.3 (1996)

**[Open in browser →](https://infinitemac.org/)**

*(Scroll down on the page to find System 7.5.3)*

*Motorola 68030 or 68040 · 8 MHz+ · Colour display*

While Microsoft and IBM were fighting over the PC, Apple kept evolving the Mac.

System 7 (1991) was the first version of the Mac OS to support colour graphics. It also added virtual memory (using disk space to extend RAM), file sharing over a network, and multitasking. The Mac went from a single-purpose personal computer to a networked workstation.

The processor had evolved too. By the time of System 7, Macs were running on the **Motorola 68030** — a full 32-bit processor with an on-chip instruction cache and a memory management unit (MMU) that enabled virtual memory. The 68030 was in many ways cleaner and more powerful than Intel's contemporary offerings. Apple would switch to PowerPC in 1994, and then to Intel in 2006 — and then to their own ARM-based Apple Silicon in 2020.

**Try this:**
- Notice the colour. Compare this directly to System 1.0 — same interface paradigm, evolved over 7 years.
- Open a few applications. System 7 ships with more software than System 1.0.
- The interface conventions — menu bar at the top, desktop with icons, overlapping windows — are essentially identical to macOS today. Apple maintained backwards compatibility with System 1.0 applications for over a decade.

<br>

---

## 8. Microsoft Windows 3.10 (1992)

**[Open in browser →](https://www.pcjs.org/software/pcx86/sys/windows/3.10/)**

*IBM PC AT · Intel 80286 @ 8 MHz · 2 MB RAM · IBM VGA*

Seven years after Windows 1.0, this is the version of Windows that people actually wanted to use.

Windows 3.1 could run in **standard mode** (using the 286's protected mode) or **386 enhanced mode** (using the 386's virtual memory to run multiple DOS programs simultaneously). Running on the 286 AT here means you get protected mode — programs are isolated from each other — but not the full virtual memory capabilities of the 386.

Windows 3.1 sold 3 million copies in its first two months. It wasn't a standalone OS — it still launched from DOS — but it was stable, had a growing library of third-party applications, and was affordable. This is the version of Windows that built Microsoft's dominance.

**Try this:**
- Open **Solitaire** — it was deliberately included to teach people how to use a mouse.
- Open **Paintbrush** and compare it to MacPaint from 1984 (and to the Mac System 7 interface you just used).
- Open **File Manager** and browse the directory structure. This is the first Windows with a file manager that feels genuinely usable.
- Compare: the Mac has had a coherent, polished GUI since 1984. Windows reaches this point in 1992. That's an 8-year gap.

<br>

---

## 9. Wolfenstein 3D — id Software (1992, shareware)

**[Open in browser →](https://www.pcjs.org/software/pcx86/game/id/wolf3d/)**

*COMPAQ DeskPro 386 · Intel 80386 @ 16–33 MHz · 2 MB RAM · IBM VGA*

A shareware release of Wolfenstein 3D, running on real emulated DOS hardware.

id Software released Wolfenstein 3D in 1992 as shareware — the first episode was free, distributed on floppy disks and bulletin board systems. It invented the first-person shooter genre. A year later, id released **Doom** (1993) on the same engine concept, which became one of the most influential games ever made.

Wolfenstein 3D ran entirely in software on the 386 — no GPU, no hardware graphics acceleration. Every frame was rendered by the CPU using a technique called **raycasting**: for each column of pixels on screen, the CPU cast a ray from the player's position, calculated where it hit a wall, and drew a scaled vertical stripe. The entire visual output of the game was arithmetic performed by the processor, 35 times per second.

The game *required* a 386. It would run too slowly on a 286, and wouldn't run at all on an 8088. This was one of the first mainstream games that explicitly required a 32-bit processor.

**Try this:**
- Press Enter through the intro screens to start.
- **Arrow keys** to move and turn. **Ctrl** to shoot. **Space** to open doors.
- Think about what the 386 is doing: no graphics card is involved in rendering this scene. Every pixel is a floating-point calculation. At 16–33 MHz with no dedicated graphics hardware, this was genuinely impressive.

<br>

---

## 10. Microsoft Windows 95 (1995)

**[Open in browser →](https://www.pcjs.org/software/pcx86/sys/windows/win95/4.00.950/)**

*COMPAQ DeskPro 386 · Intel 80386 · 4 MB RAM · IBM VGA*

Microsoft spent $300 million launching Windows 95. They licensed the Rolling Stones' *Start Me Up*, held launch events worldwide, and had people lining up outside stores at midnight. Jay Leno hosted the launch party.

For the first time, Windows was a real operating system — not a shell on top of DOS. It required at least a **386 processor** (a 486 was recommended), because it used 32-bit protected mode throughout. The 8088 and 286 machines above could not run Windows 95 at all.

It introduced the **Start button**, the **taskbar**, and **desktop shortcuts** — the layout that Windows 10 and 11 still use today. The underlying architecture (32-bit protected mode, preemptive multitasking, per-process memory) was a generation ahead of Windows 3.1.

Despite the marketing, Windows 95 on a 386 with 4 MB of RAM was genuinely slow. Microsoft's recommended spec was a 486 with 8 MB. But it ran, and it ran recognizably.

**Try this:**
- Click the **Start** button. Notice how familiar this feels — this interface is now 30 years old.
- Right-click on the desktop. Explore the context menu — right-click menus were a Windows 95 innovation.
- Open **My Computer** and browse the file system.
- Compare the machine specs: this 386 at 4 MB RAM is the minimum spec for Windows 95. Your phone has roughly 1,000× more RAM.

<br>

---

## 11. Video Games — SNES (1991–1996)

**[Try SNESLive →](https://sneslive.com/)**

*(May be blocked on the school network — try on your personal device)*

While the PC and Mac worlds were fighting over GUIs and lawsuits, console gaming was having its own golden age. The **Super Nintendo Entertainment System** launched in 1991 and ran games like *Super Mario World*, *The Legend of Zelda: A Link to the Past*, and *Street Fighter II*.

The SNES used a **Ricoh 5A22**, a custom 16-bit processor based on the WDC 65C816 running at 3.58 MHz — a completely different architecture from the Intel x86 line. It was paired with dedicated audio and graphics chips (the SPC700 and PPU) that handled sound and visuals independently of the CPU. This is the fundamental difference between a game console and a PC: consoles use specialized hardware tuned for one workload, while PCs use general-purpose components.

The SNES's 3.58 MHz CPU looks laughably slow next to a 33 MHz 386 — but because graphics and audio were handled by dedicated chips, the CPU was free to run game logic. The result was smooth, colourful gameplay on hardware that a PC couldn't match without expensive add-on cards.

Browse the game library and try a few. Controller mapping: **arrow keys** to move, **Z/X** for B/A, **A/S** for Y/X, **Enter** for Start.

<br>

---

## The Arc

From 1981 to 1995 — roughly the span of your parents' school years — personal computing went from a blinking cursor on a black screen to Windows 95. The processor went from 4.77 MHz with 256 KB of RAM to 33+ MHz with 4–16 MB. The operating system went from 50 KB of code to tens of megabytes.

The x86-64 processor in your Chromebook is a direct descendant of the Intel 8088 in the IBM PC 5150. It runs the same instruction set — extended and expanded over 45 years, but backwards compatible. A program compiled for DOS in 1981 can still run (in compatibility mode) on a modern 64-bit processor. That's an extraordinary engineering commitment.

The `dir` command you typed in DOS and the `ls` command you've been typing in Linux do the same thing. DOS and Linux are siblings from the same era, shaped by the same constraints, separated by different design philosophies — Unix on one side, IBM compatibility on the other.
