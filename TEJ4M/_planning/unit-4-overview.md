# Unit 4: Physical Computing — Raspberry Pi — Overview

**Course:** TEJ4M — Computer Engineering Technology (Grade 12)\
**Duration:** 20 periods × 60 minutes\
**Dates:** May 15 – June 12, 2026 (exam review fallback: June 15–16)\
**Prerequisites:** Unit 3 (Digital Logic) — students understand binary, logic gates, transistors as switches, CPU architecture. Unit 2 (Linux) — students can SSH, navigate the terminal, run scripts.

## Unit Arc

This unit answers the question: **How do we connect the digital world of circuits to real-world physical inputs and outputs?**

Unit 3 established how a CPU computes using logic gates. This unit moves up the stack: a real CPU (RPi) wired to real-world components via GPIO pins, controlled by Python code, producing physical behaviour. Students build from the ground up — LED → button → motor control → autonomous edge detection — then apply everything in a 2-week CPT: a self-contained sumo robot that must detect arena edges and compete autonomously.

The unit has three phases:
- **Concepts** (Day 1): Analog/Digital bridge — why sensors produce analog signals and how ADC converts them to digital
- **Python + GPIO labs** (Days 2–9): Python fundamentals in GPIO context → four guided hardware labs
- **CPT** (Days 11–20): Guided chassis build → open build → test battles → tournament

<br>

## Sequencing

| Day | Date | Topic | Format | Deliverable | Hardware |
|-----|------|-------|--------|-------------|----------|
| 1 | May 15 (Fri) | Analog vs Digital — AC/DC, ADC/DAC, sample rate, bit depth | Lecture + discussion | — | None |
| 2 | May 19 (Tue) | Python for GPIO — variables, loops, conditionals | Laptop coding | — | Laptops |
| 3 | May 20 (Wed) | Python for GPIO — imports, `try/finally`, full GPIO script structure | Laptop coding | — | Laptops |
| 4 | May 21 (Thu) | RPi setup — SSH in, filesystem orientation, run first `.py` | Guided demo + independent | — | RPi, imaged SD cards, network |
| 5 | May 22 (Fri) | **GPIO Lab 1: LED** — digital output, BCM pin numbering, `GPIO.output` | Lab | Completion | RPi, LED, 330Ω, breadboard, M-F jumpers |
| 6 | May 25 (Mon) | **GPIO Lab 2: Button** — digital input, polling loop, debounce | Lab | Completion | + tactile button, 10kΩ resistor |
| 7 | May 26 (Tue) | **GPIO Lab 3: H-Bridge + Motors** — H-bridge wiring, forward/reverse | Lab | Completion | + L298N or L9110S, TT motors, wheels |
| 8 | May 27 (Wed) | GPIO Lab 3 continued — turn logic, combined movement sequences | Lab | Completion | Same |
| 9 | May 28 (Thu) | **GPIO Lab 4: PWM** — duty cycle, `GPIO.PWM`, motor speed control | Lab | Completion | Same |
| **10** | **May 29 (Fri)** | **Unit test** | Closed-note written | **Summative /20** | None |
| 11 | Jun 1 (Mon) | CPT launch — spec + constraints; distribute laser-cut chassis; begin assembly | Guided | — | Chassis kits |
| 12 | Jun 2 (Tue) | Guided: mount TT motors + wheels, test rolling chassis | Guided build | — | + TT motors, caster/skid |
| 13 | Jun 3 (Wed) | Guided: wire RPi + power bank + H-bridge; motor test code on chassis | Guided build | — | + RPi, power bank, H-bridge |
| 14 | Jun 4 (Thu) | Guided: sensor wiring + basic autonomous edge-detection loop | Guided build | — | + photoresistor/IR sensor + comparator |
| 15 | Jun 5 (Fri) | Open build + troubleshooting | Independent | — | Full kit |
| 16 | Jun 8 (Mon) | Open build + programming | Independent | — | Full kit |
| 17 | Jun 9 (Tue) | Open build + programming | Independent | — | Full kit |
| 18 | Jun 10 (Wed) | Open build + programming | Independent | — | Full kit |
| 19 | Jun 11 (Thu) | Test battles — shake out bugs, refine strategy | — | — | Full kit + arena |
| **20** | **Jun 12 (Fri)** | **Sumo tournament + demos** | Battle + demo | **Summative /16** | Full kit + arena |
| — | Jun 15–16 | Exam review | — | Fallback buffer if CPT runs over | — |

<br>

## Assessment Structure

### Lab completion marks (Days 5–9)

Low-stakes, graded for completion. Purpose: build GPIO fluency before the test and CPT. One mark per lab (4 labs = 4 completion marks). No formal rubric — working circuit + functioning script = credit.

### Unit test (Day 10 — May 29)

Closed-note written assessment. Covers: analog vs digital, AC/DC, ADC/DAC concepts (sample rate, bit depth), Python essentials (variables, loops, conditionals, imports), RPi GPIO concepts (SSH, pin modes, `GPIO.setup`, `GPIO.output/input`).

| Category | Question | Marks |
|----------|----------|-------|
| KU | Define *analog* data and *digital* data. Give one real-world example of each. | /2 |
| KU | What is *sample rate*? What is *bit depth*? Why does each matter? | /2 |
| KU | What do `GPIO.setmode(GPIO.BCM)` and `GPIO.setup(18, GPIO.IN)` do? | /2 |
| APP | Given a voltage graph (values shown at 6 sample points) and 4-bit format (1 sign bit + 3 value bits), convert each sample to binary. | /4 |
| APP | Read the Python script below. What does the robot do? Identify the role of each highlighted line. | /3 |
| APP | A wristband measures heart rate from 40–167 bpm. What is the minimum bit depth to represent every whole-number bpm? Show reasoning. | /2 |
| COMM | A student says "just use the highest sample rate and bit depth for everything." Give two specific reasons this is not always right. | /2 |
| TIPS | Design an ADC for a new device (teacher-provided device). Choose sample rate and bit depth. Justify each. | /3 |
| **Total** | | **/20** |

The Python script in the APP section is a simple GPIO loop — close to what students wrote in lab. Reading and interpreting, not writing from scratch.

### CPT — Sumo Robot (Days 11–20, /16, 15% of course mark)

Minimum viable robot: moves, detects edge, operates autonomously. Extension is open-ended.

**Arena:** 2×2 m "donut" — robots are eliminated by falling into the centre hole or being pushed off the outer edge.

**Autonomous operation:** Script runs without live SSH during battle. Students may use a GPIO start button to trigger the script; the robot then operates independently.

| Category | Criteria | Marks |
|----------|----------|-------|
| APP | Motor control: forward, reverse, and turn all functional | /3 |
| APP | Edge detection: sensor reading correctly triggers automated response | /3 |
| APP | Autonomous operation: runs without live SSH during battle | /2 |
| KU | Demo: student explains circuit (GPIO pins, motor driver wiring, sensor wiring) in ~2 minutes | /3 |
| COMM | Code is readable: variable names, structure, and logic are followable by another person | /2 |
| TIPS | Extension beyond minimum spec (examples: start button, opponent detection via HC-SR04, PWM speed strategy, LED indicators, custom chassis modification) | /3 |
| **Total** | | **/16** |

<br>

## Chassis — Laser-Cut Corrugated Cardboard

Single flat sheet, fold-up sides, tabs and slots for assembly. No glue required (or minimal). Teacher has ready laser cutter access — design anytime, cut before June 1.

**Design requirements:**
- Platform sized for: RPi (85×56 mm footprint, same for 3B/4/5), power bank lying flat, half-breadboard, H-bridge module
- Rear motor mounts: D-shaft slots for TT motors
- Front caster mount or low HDPE skid for third contact point
- Wiring notches along edges
- Motor mounts doubled/reinforced (two layers of cardboard, glued) — sumo impacts are hard
- Optional: front bumper lip or plow zone for students to customize
- RPi mounted via standoffs through the cardboard (M2.5 hardware or zip ties)

**Design tools:** Inkscape (SVG → laser), or any laser cutter CAD tool. Standard fold-and-tab box construction. Corrugated cuts fast (~30 s/sheet).

**Test cut deadline:** May 25 (before any student touches cardboard)\
**Production cut deadline:** May 31 (ready to hand out June 1)

<br>

## Equipment Procurement Checkpoints

| Deadline | What | Risk |
|----------|------|------|
| May 20 (Wed) | RPis imaged + SSH confirmed on school network | Medium — mixed 3B/4/5, may need SD card reflash |
| May 21 (Thu) | LED lab kits sorted: breadboard, LEDs, 330Ω, M-F jumpers per group | Low |
| May 24 (Sun) | Tactile buttons confirmed in bins | Low |
| **May 25 (Mon)** | **H-bridge modules + TT motors + wheels, one set per group, tested** | **High — order by May 18 if not found** |
| May 31 (Sun) | Photoresistors + comparator OR IR line sensor modules ready | Medium |
| **May 31 (Sun)** | **Laser-cut chassis kits ready to hand out** | Low (laser cutter on-site) |
| May 31 (Sun) | Power banks tested: RPi stays on under load for 5+ min, no auto-shutoff | Medium |

**Power bank test:** plug in RPi, let it run 5 min idle, confirm it doesn't cut out. Flag any that fail — not all cheap power banks sustain low-current loads.

**Sensor note:** RPi has no native ADC, so bare photoresistors need a comparator circuit (LM393 + resistors) to produce a clean digital GPIO signal. IR line sensor modules (small PCBs with trim pot) do this internally and are plug-and-play. Check bins for IR modules from Grade 9 robotics kits — use those if available.

<br>

## Differentiation

Wide skill range expected: some students have FIRST Robotics (FTC) provincial experience; others have no prior hardware background.

**Minimum viable robot spec** (everyone): rolling chassis, edge detection triggers response, autonomous operation.

**Extension tiers:**
- *Intermediate:* GPIO start/stop button; variable-speed turns using PWM
- *Advanced:* HC-SR04 ultrasonic for opponent detection; LED state indicators; strategy state machine (aggressive vs defensive modes); PID-ish speed control

Group strategic pairing — one stronger student per group. Extension spec gives FIRST Robotics students somewhere to go so they're not done by Day 14.

<br>

## Platform Decision

**RPi, not Micro:bit.** Micro:bit + Cute Bot Pro is Grade 9 territory. TEJ4M Grade 12 students do real Python, SSH, and GPIO breadboarding. Keep Micro:bit as a silent fallback only — if a group cannot get RPi working by Day 15, hand them a Cute Bot kit so they still have a robot on battle day. Do not advertise this option.

Mixed RPi 3B/4/5 is fine — BCM GPIO pin numbering is identical across all three models.

<br>

## Key Decisions

- Photoresistor lab (originally Day 10) absorbed into CPT guided build (Day 14) — students learn the sensor while wiring their actual robot; more authentic, clears Day 10 for the test
- CodeHS Python curriculum used as self-paced reference, not as class instruction — Python taught in GPIO context directly (reading real scripts, not abstract drills)
- Test moved to end of Week 2 (after all GPIO labs) so students have applied the concepts before being assessed — mirrors the Unit 3 decision to test after the guided build
- CPT demo component (KU /3) is oral, ~2 min, on tournament day — no separate written document required

<br>

## Files to Produce

### Student-facing (in `unit-4-rpi/`)
- [ ] `01-analog-digital.md` — AC/DC, analog vs digital, ADC/DAC, sample rate, bit depth, practice problems
- [x] `02-python-for-gpio.md` — variables, loops, conditionals, imports, `try/finally`, full GPIO script walkthrough
- [ ] `03-rpi-setup.md` — SSH workflow, filesystem orientation, running a `.py` script, BCM pin reference
- [ ] `lab-01-led.md` — LED circuit, GPIO output code, wiring diagram
- [ ] `lab-02-button.md` — button circuit, GPIO input code, debounce
- [ ] `lab-03-motors.md` — H-bridge wiring, direction control, turn sequences
- [ ] `lab-04-pwm.md` — PWM concept, `GPIO.PWM`, duty cycle, speed control
- [ ] `cpt-sumo-robot.md` — CPT spec, minimum requirements, extension tiers, rubric, demo expectations, academic integrity

### Teacher-facing (in `_planning/`)
- [x] `unit-4-overview.md` — this file

<br>

## Open Items

- Confirm H-bridge module model in bins (L298N vs L9110S vs L293D chip) — affects lab wiring diagrams
- Confirm sensor solution: IR line sensor modules vs bare photoresistor + LM393 — affects Day 14 guided build instructions
- Confirm RPi OS versions across the 3B/4/5 fleet — Bookworm is current; older images may need reflash before Day 4
- Confirm school network allows mDNS (`raspberrypi.local`) or whether students need static IP assignment for SSH
- Chassis design: finalize before May 25 test cut
- Decide group size (pairs recommended given hardware count and wide skill range)
- Decide whether CPT is individual or group mark (group recommended given shared chassis; could split: circuit/code = group, demo explanation = individual)
