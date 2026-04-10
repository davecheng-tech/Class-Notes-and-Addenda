# Retro Gaming Capstone: Emulation on Linux

**Course:** TEJ4M - Computer Engineering Technology (Grade 12)\
**Unit:** Linux and Processor Architecture\
**Timeline:** ~3 work periods × 75 minutes

## Contents

- [Overview](#overview)
- [What You're Building](#what-youre-building)
- [Part 1: Set Up Your Emulators](#part-1-set-up-your-emulators)
- [Part 2: Choose Your Subject](#part-2-choose-your-subject)
- [Part 3: Explore and Document](#part-3-explore-and-document)
- [Part 4: Where Are We Now?](#part-4-where-are-we-now)
- [Your Deliverable](#your-deliverable)
- [Getting ROMs](#getting-roms)
- [Writing in Markdown](#writing-in-markdown)
- [Assessment Rubric](#assessment-rubric)

---

## Overview

The Acer C720 is over a decade old. Its Intel Celeron processor runs at 1.4 GHz with 2 GB of RAM. A modern web browser can bring it to its knees. 

That said, it's still powerful enough that it can run every video game console released before the year 2000, including the NES, Game Boy, and Super Nintendo, at full speed in a window on your Lubuntu desktop.

The NES had a 1.79 MHz processor. Your Chromebook's CPU runs approximately 800 times faster. That gap is what emulation takes advantage of. A machine with enough headroom can simulate a slower one in software, cycle by cycle, accurately enough that the software on top has no idea it isn't running on real hardware. We've already looked at the vocabulary for this: Processor architecture, ISAs, clock speeds, the difference between x86-64 and ARM. 

For this project, you will install three emulators on your Linux machine, pick a subject to trace across three generations of gaming hardware, and write about what you find.

---

## What You're Building

Pick **something to trace across three generations of gaming hardware**: the NES, the Game Boy (or Game Boy Advance), and the Super Nintendo.

Your subject could be a franchise, a genre, or a concept:

**A franchise.** Follow a game series across all three systems. Mario, Zelda, Kirby, Mega Man, Tetris, Castlevania, Final Fantasy — pick something with entries on all three platforms and see how it changed, or didn't.

**A genre.** Pick a style of game and find a representative title on each system. How do platformers, racing games, RPGs, puzzle games, or fighting games hold up across hardware generations? What does each platform make possible?

**A concept.** Sound and music. Saving progress. Colour and art. Boss design. The hardware specs on these three systems differ in specific ways. How do those differences show up in how games were made?

Your deliverable is a `README.md` file: a written and illustrated retrospective organized around your subject. Write as a player and a critic. The install process is setup, not the point.

---

## Part 1: Set Up Your Emulators

Install all three emulators before you start playing.

### NES: FCEUX

```bash
sudo apt install fceux
```

Launch with `fceux` at the terminal, or find it in the application menu. **File > Open ROM** to load a game.

### Game Boy / GBA: mGBA

```bash
sudo apt install mgba-qt
```

Launch with `mgba-qt` at the terminal or from the application menu. mGBA handles original Game Boy, Game Boy Color, and Game Boy Advance ROMs in one package.

### Super Nintendo: Snes9x

```bash
snap install snes9x-gtk
```

> [!NOTE]
> `snap` is a separate packaging system from `apt` and `dpkg`, installed by default on Lubuntu. Snes9x is not in the standard Ubuntu repositories, so this is the install path for it. The command works the same way: run it, wait, done.

Launch Snes9x from the application menu after installing.

### No Configuration Required

All three emulators should work immediately after install. No config files to edit, no services to start. Install, open a ROM, play.

---

## Part 2: Choose Your Subject

Pick an angle before you start playing.

A retrospective needs a **focus**. Tracing how a specific game series controls and feels across three platforms is a subject. Playing three random games because they were the first ROMs you could find is not.

Some starting points:

**Franchise ideas**
- Mario: *Super Mario Bros.* (NES) / *Super Mario Land* (GB) / *Super Mario World* (SNES)
- Zelda: *The Legend of Zelda* (NES) / *Link's Awakening* (GB) / *A Link to the Past* (SNES)
- Kirby, Mega Man, Castlevania, and Final Fantasy all have entries across these three systems
- Tetris appears on every platform. The differences between versions are worth examining closely.

**Genre ideas**
- Choose representative games from each system and compare how the genre plays on each

**Concept ideas**
- *Sound:* The NES had 5 audio channels. The SNES had an 8-channel DSP chip with sample playback. How does that difference show up in the music?
- *Colour:* The NES outputs 52 colours. The SNES can display 32,768. How did designers use that range?
- *Saving:* Early NES games had no save feature. How did games handle that? When did it change?

> [!TIP]
> Browse the class ROM collection before you commit to anything. Interesting projects often start with something discovered while wandering around. Play a few things first.

---

## Part 3: Explore and Document

For **each of the three platforms**, your README needs to cover all of the following.

### Hardware Context *(2-4 sentences)*

What machine is this? What were the key specs: processor, speed, RAM, audio, colour depth? What made it capable or limited compared to what came before? You know where to find this kind of information.

### What You Played

Name the ROMs you tried. If you went through several before something clicked, say so. You do not have to pick one game per platform and stop there.

### Screenshots *(minimum 2 per platform)*

Take screenshots that are useful to your argument, not just proof that the emulator opened. A visual comparison, a moment of impressive or disappointing graphics given the hardware, a UI decision that tells you something about the era. Make the screenshots count. Make them something you actually want to show someone.

### Your Observations

What did you notice? What surprised you? Where do you see the hardware constraints shaping what designers could and couldn't do?

Write with enough specificity that the observation could only have come from you, playing this game. "The sound in Super Mario Land is noticeably thinner than the NES version, even though the Game Boy came out five years later, probably because the hardware had fewer audio channels" tells the reader something. "The graphics improved over time" tells them nothing.

> [!IMPORTANT]
> The observations section carries the most weight in the rubric. Describing what a game looks like is not enough. Noticing something specific and explaining why you think it is the way it is — that's what you're going for.

---

## Part 4: Where Are We Now?

Add a final section covering the same subject on a modern platform.

This does not need to run on your Chromebook. A screenshot from a phone game, a current console, a browser, a PC, or a streaming service all count.

What does your subject look like in 2025? What changed? What, surprisingly, stayed the same?

---

## Your Deliverable

Submit a folder containing:

```
README.md
images/
    nes-screenshot-1.png
    nes-screenshot-2.png
    gb-screenshot-1.png
    snes-screenshot-1.png
    today-screenshot.png
```

Give image files descriptive names. Reference them in your README using the image syntax described in the *Writing in Markdown* section below.

### Taking Screenshots on Lubuntu

These machines do not have a Print Screen key. Use **Graphics > ScreenGrab** from the application menu to capture your screen.

Before taking a screenshot, use the emulator's pause or save state feature to freeze the game at exactly the moment you want to show. A well-chosen frame tells a story. A blurry mid-action shot usually does not.

> [!CAUTION]
> Do not photograph your monitor or laptop screen with a phone or camera. Image quality is unacceptable for documentation purposes and marks will be deducted.

Move your screenshots into your `images/` folder and rename them descriptively.

---

## Getting ROMs

**Class file share.** NES, Game Boy, GBA, and SNES ROM collections are available on the class share (address on the board). Browse by system folder. Start here.

**Archive.org.** For ROMs not on the class share, [archive.org](https://archive.org) has large collections organized by system. Search the system name, for example *NES ROM set* or *Game Boy ROM collection*. These are copyrighted games and hosting them is legally grey, but Archive.org operates as a software preservation archive and is the most reputable place to find this material.

> [!TIP]
> Going beyond the three required systems is entirely optional, but it is one path to Level 4+. If you want to emulate a Sega Genesis, Nintendo 64, PlayStation, Atari, or Commodore 64, the emulators exist, the ROMs are on Archive.org, and you can figure it out. Start with a search for the system name and "Linux emulator."

---

## Writing in Markdown

Your `README.md` is a Markdown file. Markdown is plain text with lightweight formatting that renders as HTML. It is the standard format for documentation on GitHub and across the software industry.

Here is the syntax you need:

```markdown
# Heading 1
## Heading 2
### Heading 3

Normal paragraph text. Just write normally.

**Bold text** and *italic text*.

- Bullet item
- Another bullet item

![Image caption](images/filename.png)

[Link text](https://example.com)
```

Use a browser-based editor to write your markdown and see the rendered output side by side:

- [markdowneditor.net](https://markdowneditor.net/markdown-editor/)

When you are ready to save your work, copy the text into `README.md` using nano:

```bash
nano README.md
```

**Reference and tutorial:**
- [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Markdown Tutorial](https://www.markdowntutorial.com/) — interactive, takes about 10 minutes

---

## Academic Integrity

You may use any resources: documentation, online references, each other.

Screenshots must be your own, taken on your machine or your personal devices. Writing must be in your own voice, based on what you actually observed while playing.

AI-generated text is confident, well-organized, and has no actual opinions. It cannot tell you what surprised it about Super Mario Land because it never played it. Observations that could have been written by someone who never opened the emulator will read that way.

---

## Assessment Rubric

Achievement levels correspond to Ontario grading bands:

- **Level 1:** 50-59%
- **Level 2:** 60-69%
- **Level 3:** 70-79%
- **Level 4 / 4+:** 80-100%

<br>

### Exploration & Coverage — /15 (Application)

**Assesses how thoroughly you engaged with the three required platforms. Evidence of genuine time spent playing and exploring.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All three platforms covered with exceptional evidence of exploration and genuine curiosity. Reached two ways: by going beyond the required platforms (additional systems emulated, additional ROM collections explored), or by demonstrating unusual depth within them (multiple games per platform thoroughly compared, subject pursued from several angles, clear evidence of extended time within the prescribed ecosystem). |
| **4** | All three platforms covered with clear evidence of genuine play. Multiple games or moments documented per platform. Screenshots are varied and purposeful. |
| **3** | All three platforms covered. Evidence of genuine play is present but may be thin on one platform. Screenshots are adequate. |
| **2** | One or two platforms covered adequately; remaining platforms are superficial or missing. |
| **1** | Limited engagement across platforms. Little evidence of actual play. |

<br>

### Analysis & Voice — /20 (Communication / Thinking)

**Assesses the quality of your observations and writing. Are you describing what you see, or explaining why it is the way it is? Is this your voice?**

| Level | Descriptor |
|:-----:|------------|
| **4+** | Observations consistently connect what is seen to hardware, design choices, or historical context from the unit. Writing has a clear personal voice, including opinion, uncertainty, and surprise. The "Where Are We Now?" section draws a meaningful conclusion about what changed and what didn't. |
| **4** | Analysis goes beyond description. You explain *why* things are different across platforms: hardware constraints, design decisions, the limits of the era. Personal voice is clear. Writing is specific and concrete. |
| **3** | Observations are your own and show genuine engagement. Some analysis beyond pure description. Writing is clear, with occasional vagueness or generic statements. |
| **2** | Writing is mostly descriptive. Observations are present but generic ("the graphics got better over time"). Little evidence of analysis or personal engagement. |
| **1** | Writing is minimal, formulaic, or does not reflect the student's own observations and play. |

<br>

### Documentation & Presentation — /15 (Communication)

**Assesses the quality of your README as a document: structure, markdown formatting, screenshot quality and captions, and overall presentation.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | README reads as a polished, publication-quality retrospective. Image selection and captioning are strong; every screenshot earns its place. Markdown is used with confidence and creativity beyond the basics (tables, blockquotes, structure that serves the content). The document has a clear editorial identity. |
| **4** | README is well-structured with a clear heading hierarchy. Screenshots are purposeful and captioned. Markdown is used correctly and effectively throughout. The document reads as a coherent retrospective rather than a checklist. |
| **3** | README is organized and readable. Screenshots are present and correctly referenced. Markdown is used competently with minor formatting errors. |
| **2** | Structure is present but inconsistent. Screenshots are included but may be uncaptioned or loosely connected to the writing. Markdown errors affect readability in places. |
| **1** | Document is difficult to follow. Screenshots are missing or not integrated with the writing. Little evidence of intentional formatting. |

---

## Suggested Timeline

**Period 1 — Setup and Orientation**\
Install all three emulators. Browse the ROM collection. Decide on a subject. Start playing.

**Periods 2-3 — Exploration and Writing**\
Explore your subject across all three platforms. Take screenshots as you go. Write while impressions are fresh. Do not leave all the writing to the end.

**End of Period 3 — Finalize and Submit**\
Assemble your `README.md` and `images/` folder. Review formatting. Submit.
