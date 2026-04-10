# Unit 2: Linux and Processor Architecture — Overview

**Course:** TEJ4M — Computer Engineering Technology (Grade 12)\
**Duration:** 16 periods × 75 minutes\
**Prerequisites:** Unit 1 (Networking) — students can navigate the terminal, use apt for basic installs, edit config files, use sudo, SSH into machines.

## Unit Arc

This unit answers the question: **What is this machine, how does the OS organize it, and how does software get installed and run on it?**

Students move from understanding the hardware (architecture) through the OS abstractions that manage it (filesystem, permissions, processes) to the practical skill of installing and configuring software (package management, manual installation). The capstone synthesizes everything: install a video game emulator, understand why emulation works (architecture), and document the entire process as a technical README.

## Sequencing

| Per. | Topic | Format | Deliverable | Notes file |
|------|-------|--------|-------------|------------|
| 1 | Processor architecture (x86 vs ARM, ISA, lscpu/free/lsblk) | Socratic + demo | — | `processor_architecture.md` ✓ |
| 2 | Filesystem hierarchy (FHS, /etc, /var, /usr, /home, /dev, /proc) | Short lecture + scavenger hunt | Completion | `filesystem_hierarchy.md` |
| 3 | Users, groups, permissions (chmod, chown, sudo, reading ls -l) | Demo + permissions puzzle | Completion | `permissions_and_ownership.md` |
| 4 | Processes and services (ps, top, kill, systemctl, backgrounding) | Demo + process detective | Completion | `processes_and_services.md` |
| 5 | Pipes, redirection, grep (|, >, >>, composing tools) | Pipeline challenges | Completion | `pipes_and_redirection.md` |
| 6 | Consolidation troubleshooting exercise | Scripted scenario, independent | Completion | `troubleshooting_exercise.md` + `troubleshooting_setup.sh` |
| 7 | How apt works (repos, deps, dpkg) | Socratic + trace a real install | — | `package_management.md` |
| 8 | Manual installation (tarballs, PATH, deps) | Guided walkthrough: btop (together), micro (independent) | Completion | (covered in `package_management.md`) |
| 9 | Capstone launch + planning | Assignment intro, emulator selection | — | `capstone_emulator_project.md` |
| 10–13 | Capstone work periods | Independent with check-ins | — | |
| 14 | Capstone due + demos | Submission + show-and-tell | **Summative (A, C)** | |
| 15 | Unit test (closed-note) | Written | **Summative (K, T)** | |
| 16 | Buffer | — | — | |

## Assessment Structure

- **Completion marks (periods 2–6, 8):** Small hands-on exercises at the end of each note. Graded for completion, not perfection. Purpose: reinforce concepts and build fluency before the capstone.
- **Capstone — Emulator Project (period 14):** Summative, weighted toward Application and Communication. Deliverable is a folder containing `README.md` + `images/` subfolder with screenshots. Students document the full installation, configuration, and architecture analysis.
- **Unit test (period 15):** Closed-note written assessment, weighted toward Knowledge and Thinking. Drawn from the canonical notes (periods 1–8).

## Capstone Emulator Menu

| Emulator | Target System | Target Architecture | Install Method | Difficulty |
|----------|--------------|-------------------|----------------|------------|
| snes9x | Super Nintendo | 65C816 | `apt` | Lower |
| VICE | Commodore 64 | 6502/6510 | `apt` | Medium |
| DOSBox | IBM PC (DOS) | x86 real-mode | `apt` | Medium (interesting: x86-on-x86, different OS model) |
| BasiliskII | Macintosh Classic | Motorola 68000 | Manual (binary/build) | Higher |
| Hatari | Atari ST | Motorola 68000 | `apt` or manual | Medium-high |

Students who finish early or want more can explore additional platforms (e.g., Z80-based systems, MAME) as extensions.

## Files to Produce

### Student-facing (in `unit-2-linux/`)
- [x] `processor_architecture.md`
- [x] `filesystem_hierarchy.md` — FHS, key directories, scavenger hunt (10 questions)
- [x] `permissions_and_ownership.md` — multi-user model, chmod, chown, sudo, permissions puzzle (8 tasks)
- [x] `processes_and_services.md` — ps, top, fg/bg, signals, kill, systemctl, pstree, process detective (13 tasks)
- [x] `pipes_and_redirection.md` — stdin/stdout/stderr, redirection, pipes, grep, pipeline challenges (10 questions)
- [x] `package_management.md` — how apt works, dpkg, PATH, manual install walkthrough (btop), independent exercise (micro)
- [ ] `troubleshooting_exercise.md` — student instructions for period 6 scripted scenario
- [x] `capstone_emulator_project.md` — emulator install + README.md deliverable, rubric, emulator menu

### Teacher-facing (in `_planning/`)
- [x] `unit-2-overview.md` — this file
- [ ] `troubleshooting_setup.sh` — setup script for period 6 exercise

### Open items for next session
- Test btop/micro manual install walkthrough on C720 (package_management.md exercise)
- Write troubleshooting exercise + setup script
- Write capstone assignment description with rubric
- Decide: should troubleshooting exercise sandbox simulate a broken service (Samba-like) or something more generic?
