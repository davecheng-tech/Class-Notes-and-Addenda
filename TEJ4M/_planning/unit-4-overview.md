# Unit 4: Physical Computing — Raspberry Pi — Overview

**Course:** TEJ4M — Computer Engineering Technology (Grade 12)\
**Duration:** 20 periods × 70 minutes\
**Dates:** May 15 – June 12, 2026 (exam review fallback: June 15)\
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
| 7 | May 26 (Tue) | **GPIO Lab 3: Motors** — L293D H-bridge wiring, one motor forward/reverse | Lab | Completion | + L293D (DIP-16), 1× TT motor |
| 8 | May 27 (Wed) | GPIO Lab 3 continued — two motors, PWM speed control, duty cycle | Lab | Completion | + 1× additional TT motor |
| 9 | May 28 (Thu) | **GPIO Lab 4: Photoresistor** — RC timing circuit, count loop, edge detection logic | Lab | Completion | + GL5528, ~1µF cap, white LED |
| 10 | May 29 (Fri) | Flex / buffer | — | — | — |
| 11 | Jun 1 (Mon) | **Lab 5: Chassis assembly — Day 1** | Guided build | — | Chassis kits, TT motors, zip ties |
| 12 | Jun 2 (Tue) | **Lab 5: Chassis assembly — Day 2**; rolling chassis proof due; CPT rubric intro; groups finalized | Guided build | Rolling chassis video (completion) | Full kit |
| 13 | Jun 3 (Wed) | Open build | Independent | — | Full kit |
| **14** | **Jun 4 (Thu)** | **Unit test** + bot teardown / component cleanup | Written + cleanup | **Summative /20** | None |
| 15 | Jun 5 (Fri) | Open build — floor check: edge detection running on assembled robot | Independent | — | Full kit |
| 16 | Jun 8 (Mon) | Open build | Independent | — | Full kit |
| 17 | Jun 9 (Tue) | Open build | Independent | — | Full kit |
| 18 | Jun 10 (Wed) | Open build — **feature freeze end of day** | Independent | — | Full kit |
| 19 | Jun 11 (Thu) | Test battle day — practice rounds, final ring calibration | — | — | Full kit + arena |
| **20** | **Jun 12 (Fri)** | **Sumo tournament** | Battle | — | Full kit + arena |
| — | Jun 13 (Sat) | — | — | **CPT submission due 11:59 PM ET** | — |
| — | Jun 15 (Mon) | Exam review | — | — | — |

### CPT Milestones (teacher reference)

| Date | Milestone | Action if missed |
|------|-----------|-----------------|
| Jun 2 | Groups finalized, rolling chassis proof submitted | Group locked; teacher assigns if students stall |
| Jun 5 | Edge detection running on assembled robot (teacher circulates, not submitted) | Teacher check-in each subsequent day |
| Jun 10 | Feature freeze — no new hardware or code after today | Hard stop; document what exists |
| Jun 11 | Final ring calibration | Last chance before scored rounds |
| Jun 13 23:59 | Final document submission | Late = 0 on CPT |

<br>

## Assessment Structure

### Lab completion marks (Days 5–9)

Low-stakes, graded for completion. Purpose: build GPIO fluency before the test and CPT. One mark per lab (4 labs = 4 completion marks, plus the rolling chassis proof on Day 12). No formal rubric — working circuit + functioning script = credit.

### Unit test (Day 14 — Jun 4)

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

### CPT — Sumo Robot (Days 11–20, 15% of course mark)

Groups of 2–3. Deliverable: `README.md` + `images/` + `src/` folder, submitted as a `.zip` archive by Jun 13 at 11:59 PM ET. See `unit-4-rpi/cpt-sumo-robot.md` for full spec and student-facing rubric.

| Category | Weight |
|----------|--------|
| Engineering Design & Planning | 20% |
| Build Process & Technical Evidence | 25% |
| Software Implementation | 25% |
| Competition Performance & Reflection | 30% |

**Competition format:** 4-robot battle royale on a donut-shaped ring (white foamcore base, black mat interior, black outer boundary line). Multiple rounds in a round-robin rotation. Points for placement order; bonus points for causing eliminations. Robots must keep moving — idle robots are eliminated. Autonomous only; no SSH during a match.

**Minimum viable robot:** button start with 5-second delay, wander state, photoresistor edge detection triggers reversal. This is achievable with the guided-build codebase.

**L4+ path:** thorough documentation, in-progress photos, calibration log with context, annotated code snippets, `try/finally` GPIO cleanup, and a technically specific post-mortem. Competition performance contributes but does not gate L4+.

<br>

## Chassis — Laser-Cut Corrugated Cardboard

Pre-cut two-layer chassis provided to all groups. See `lab-05-chassis.md` for assembly instructions. OnShape reference: [Chassis CAD](https://cad.onshape.com/documents/5348ff0bd57b3a2cea242434/w/6562db79663996135ecdf5b8/e/768ff86290f46d6c1236f710)

Custom chassis work is available for CPT: must fit within 11 × 17 inch sheet of corrugated cardboard. Laser cutter on-site — speak to teacher. Groups modifying the chassis should document the design intent in their CPT document.

<br>

## Differentiation

Wide skill range expected: some students have FIRST Robotics (FTC) provincial experience; others have no prior hardware background.

**Minimum viable robot spec** (everyone): rolling chassis, edge detection triggers response, autonomous operation.

**Extension tiers:**
- *Intermediate:* GPIO start/stop button; variable-speed turns using PWM
- *Advanced:* HC-SR04 ultrasonic for opponent detection; LED state indicators; strategy state machine (aggressive vs defensive modes); threading for concurrent sensor/motor control; custom chassis

Group pairing — one stronger student per group. Extension spec gives FTC-level students somewhere to go.

<br>

## Platform Decision

**RPi, not Micro:bit.** Micro:bit + Cute Bot Pro is Grade 9 territory. TEJ4M Grade 12 students do real Python, SSH, and GPIO breadboarding. Keep Micro:bit as a silent fallback only — if a group cannot get RPi working by Day 15, hand them a Cute Bot kit so they still have a robot on battle day. Do not advertise this option.

Mixed RPi 3B/4/5 is fine — BCM GPIO pin numbering is identical across all three models.

<br>

## Key Decisions

- Lab 4 (photoresistor + RC timing) runs as a standalone guided lab on Day 9 — students learn the sensor on the bench before mounting it on the chassis, which reduces CPT build complexity
- CodeHS Python curriculum used as self-paced reference, not as class instruction — Python taught in GPIO context directly
- Unit test moved to Jun 4 (Day 14) — after chassis build days — so students have seen sensor and motor integration in a physical context before the written assessment
- CPT deliverable is a written document (README.md + images/ + src/) submitted after tournament day, not an oral demo — enables more rigorous assessment and works well with subagent-assisted grading

<br>

## Files to Produce

### Student-facing (in `unit-4-rpi/`)
- [x] `01-analog-digital.md` — AC/DC, analog vs digital, ADC/DAC, sample rate, bit depth
- [x] `02-python-for-gpio.md` — variables, loops, conditionals, imports, `try/finally`, full GPIO script walkthrough
- [x] `03-rpi-setup.md` — SSH workflow, filesystem orientation, running a `.py` script, BCM pin reference
- [x] `lab-01-led.md` — LED circuit, GPIO output code, wiring diagram
- [x] `lab-02-button.md` — button circuit, GPIO input code, debounce, extensions
- [x] `lab-03-motors.md` — L293D H-bridge, one motor (Day 7), two motors + PWM (Day 8)
- [x] `lab-04-photoresistor.md` — RC timing circuit, count loop, threshold calibration, edge detection
- [x] `lab-05-chassis.md` — guided chassis assembly, electronics stack, wiring, boot test
- [x] `cpt-sumo-robot.md` — CPT spec, milestones, deliverable format, rubric

### Teacher-facing (in `_planning/`)
- [x] `unit-4-overview.md` — this file
- [ ] Unit test question paper (Jun 4)

<br>

## Open Items

- Unit test question paper not yet written — needed before Jun 4
