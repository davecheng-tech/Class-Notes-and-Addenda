# TEJ4M — Computer Engineering Technology

Course notes, labs, assignments, and teacher planning materials for TEJ4M (Grade 12 Computer Engineering Technology, Ontario), built out over the 2025–26 school year.

**Provenance:** the unit sequencing, project structure, and assessment weighting here are largely inherited from another teacher's course outline for this course. This repo formalizes that outline into a single written reference — one source of truth the students can be taught from and study from directly, with the planning rationale kept alongside it for whoever teaches it next. If you taught the original outline this is based on, you'll recognize the shape of each unit; what's been added is the full student-facing text, worked examples, labs, and the day-by-day teacher planning underneath it.

If you're a teacher picking this up to borrow or adapt: start with this page, then each unit's `_planning/unit-N-overview.md` for the why and when, and the student-facing `.md` files in each `unit-N-.../` folder for the what.

---

## How the repo is organized

```
TEJ4M/
├── index.md                    ← this file
├── final-exam-review.md        ← student-facing exam review guide
├── unit-1-networking/          ← student-facing notes + assignments
├── unit-2-linux/               ← student-facing notes + troubleshooting exercises
├── unit-3-digital-logic/       ← student-facing notes + practice + ALU assignment
├── unit-4-rpi/                 ← student-facing labs + CPT (sumo robot) spec
└── _planning/                  ← teacher-facing only — not linked from student materials
    ├── unit-N-overview.md          ← per-unit arc, sequencing table, assessment breakdown
    ├── unit-3-alu-lesson-plans.md  ← detailed day-by-day plans, ALU section
    ├── unit-4-day*-lesson-plans.md ← detailed day-by-day plans, RPi unit (selected days)
    ├── rpi-network-scan.md         ← how to find Pi IPs on the school network
    ├── troubleshooting_solutions.md← answer key for unit-2 troubleshooting scenarios
    └── cpt-reference-2025/         ← archived student code from last year's CPT cohort
```

**Student-facing** material (everything outside `_planning/`) is written to be read by students — it's the actual course text, used both for teaching from and for independent review/study.

**`_planning/`** is teacher-facing sequencing and rationale: how many periods, what order, why that order, how marks break down, what to watch for. Nothing in here is meant for student eyes — it includes answer keys, calibration notes, and candid notes on past student work.

**`_planning/cpt-reference-2025/`** is a special case: it's archived *student* code (three full robot codebases plus individual students' lab-progression files) from last year's sumo-robot CPT, kept as a teacher reference — for calibrating expectations, anticipating common bugs, and pulling real teaching examples. See its `README.md` for a team-by-team breakdown and a cross-team table of bugs/patterns worth pre-empting in lab. It is not a model solution set — all three teams had bugs, and the point is realism, not polish.

---

## Unit 1: Networking

*No `_planning` overview written yet — sequencing lives only in the student-facing files below.*

Concepts: TCP/IP model, network devices, IP and MAC addressing, ARP, DNS, DHCP, TCP vs UDP, wireless networking, diagnostics. Hands-on: Lubuntu installation on student Chromebooks, terminal fundamentals, a network-services deployment project.

| # | Topic | Type |
|---|-------|------|
| — | [Installing Linux (Lubuntu) on a Chromebook](unit-1-networking/chromebook_lubuntu_install.md) | Setup guide |
| — | [Terminal Reference](unit-1-networking/terminal_reference.md) | Reference |
| — | [Terminal Reference — CLI, Networking, and Linux](unit-1-networking/terminal_linux_reference.md) | Reference |
| 1 | [Networking Review](unit-1-networking/networking_review.md) | Notes |
| 2 | [Network Services Project](unit-1-networking/network_services_project.md) | Assignment |

---

## Unit 2: Linux and Processor Architecture

**Planning:** [`_planning/unit-2-overview.md`](_planning/unit-2-overview.md) · 16 × 75 min periods · prerequisite: Unit 1 terminal/SSH fluency

**Arc:** hardware (architecture) → OS abstractions that manage it (filesystem, permissions, processes) → practical install/config skill (package management) → capstone synthesis (install an emulator, explain *why* it works, document it).

| # | Topic | Type |
|---|-------|------|
| — | [Retro Computing Exploration](unit-2-linux/retro_computing.md) | Class activity |
| 1 | [Processor Architecture](unit-2-linux/processor_architecture.md) | Notes |
| 2 | [Filesystem Hierarchy](unit-2-linux/filesystem_hierarchy.md) | Notes |
| 3 | [Permissions and Ownership](unit-2-linux/permissions_and_ownership.md) | Notes |
| 4 | [Processes and Services](unit-2-linux/processes_and_services.md) | Notes |
| 5 | [Pipes and Redirection](unit-2-linux/pipes_and_redirection.md) | Notes |
| 6 | [Troubleshooting Exercise 1](unit-2-linux/troubleshooting/scenario-1/README.md) (Scenarios 1–3) | Exercise |
| 7 | [Package Management](unit-2-linux/package_management.md) | Notes |
| — | [Troubleshooting Exercise 2](unit-2-linux/troubleshooting-2/scenario-4/README.md) (Scenarios 4–6) | Exercise |
| 8 | [Capstone: Retro Gaming — Emulation on Linux](unit-2-linux/capstone_emulator_project.md) | Assignment (summative) |
| — | [Tech Supplement: Emulation Setup](unit-2-linux/tech_supplement.md) | Reference |

Both troubleshooting exercises are scripted, scenario-based (`setup.sh` / `teardown.sh` per scenario); answer key in [`_planning/troubleshooting_solutions.md`](_planning/troubleshooting_solutions.md). Unit closes with a closed-note written test (periods 1–8 content); the test paper itself is deliberately not stored in this public repo (see [`_planning/README.md`](_planning/README.md)).

---

## Unit 3: Digital Logic

**Planning:** [`_planning/unit-3-overview.md`](_planning/unit-3-overview.md) + [`_planning/unit-3-alu-lesson-plans.md`](_planning/unit-3-alu-lesson-plans.md) (detailed day-by-day for periods 9–16) · 16 × 60 min periods · prerequisite: Unit 2 + prior-year (TEJ3M) 7-gate CircuitVerse/breadboard experience

**Arc:** review the 7 basic gates → the four representations of combinational logic (truth table / circuit / equation / SOP) and all six conversions between them → Boolean algebra simplification → apply all of it to design a 4-bit ALU in CircuitVerse (adder, subtractor, AND, LST, 4-in-1 MUX).

| # | Topic | Type |
|---|-------|------|
| 1 | [From Transistors to Gates](unit-3-digital-logic/01-from-transistors-to-gates.md) | Notes |
| 2 | [Combinational Logic](unit-3-digital-logic/02-combinational-logic.md) | Notes |
| 3 | [Boolean Algebra Simplification](unit-3-digital-logic/03-boolean-simplification.md) | Notes |
| 4 | [ALU Design](unit-3-digital-logic/04-alu-design.md) | Notes |
| — | [Practice: Logic Conversions](unit-3-digital-logic/practice-conversions.md) | Practice |
| — | [Practice: Boolean Simplification](unit-3-digital-logic/practice-simplification.md) (+ [solutions](unit-3-digital-logic/practice-simplification-solutions.md)) | Practice |
| — | [Practice: More Simplification](unit-3-digital-logic/practice-more-simplification.md) (+ [solutions](unit-3-digital-logic/practice-more-simplification-solutions.md)) | Practice |
| — | [Homework: Logic Conversions](unit-3-digital-logic/homework.md) | Homework |
| — | [Practice: ALU Guided Build](unit-3-digital-logic/practice-alu-guided-build.md) | In-class guided activity (periods 9–11); also used as a reference during the assignment |
| — | [Review Problems](unit-3-digital-logic/review-problems.md) (+ [solutions](unit-3-digital-logic/review-solutions.md)) | Review |
| — | [Schematic Conventions](unit-3-digital-logic/schematic-conventions.md) | Reference |
| — | [Binary Number Review](unit-3-digital-logic/binary_number_review.md) | Reference |
| — | [ALU Assignment](unit-3-digital-logic/alu-assignment.md) | Assignment (summative) |
| — | [ALU Extension](unit-3-digital-logic/alu-extension.md) | Extension (students working ahead) |

Two summatives: a closed-note combinational-logic test (period 12; breakdown in the overview) and the ALU assignment (8-tab CircuitVerse project + design document, due period 16).

---

## Unit 4: Physical Computing — Raspberry Pi

**Planning:** [`_planning/unit-4-overview.md`](_planning/unit-4-overview.md) + day-specific detail in [`unit-4-day2-day3-lesson-plans.md`](_planning/unit-4-day2-day3-lesson-plans.md), [`unit-4-day4-day5-lesson-plans.md`](_planning/unit-4-day4-day5-lesson-plans.md), [`unit-4-day6-lesson-plans.md`](_planning/unit-4-day6-lesson-plans.md) · 20 × 70 min periods (May 15 – Jun 12) · prerequisite: Unit 3 (logic) + Unit 2 (SSH/terminal)

**Arc:** analog↔digital bridge → Python in a GPIO context → four guided hardware labs (LED → button → motors → photoresistor) → a two-week CPT: a self-contained sumo robot that must edge-detect and compete autonomously, culminating in a tournament.

| Topic | File | Type |
|---|---|---|
| Analog vs Digital, ADC/DAC | [01-analog-digital.md](unit-4-rpi/01-analog-digital.md) | Notes |
| Python for GPIO | [02-python-for-gpio.md](unit-4-rpi/02-python-for-gpio.md) | Notes |
| RPi setup (SSH, filesystem) | [03-rpi-setup.md](unit-4-rpi/03-rpi-setup.md) | Notes |
| Lab 1: LED | [lab-01-led.md](unit-4-rpi/lab-01-led.md) | Lab |
| Lab 2: Button | [lab-02-button.md](unit-4-rpi/lab-02-button.md) | Lab |
| Lab 3: Motors (H-bridge, PWM) | [lab-03-motors.md](unit-4-rpi/lab-03-motors.md) | Lab |
| Lab 4: Photoresistor (RC timing, edge detection) | [lab-04-photoresistor.md](unit-4-rpi/lab-04-photoresistor.md) | Lab |
| Addendum: Motor Power | [addendum-motor-power.md](unit-4-rpi/addendum-motor-power.md) | Reference |
| Lab 5: Chassis Assembly | [lab-05-chassis.md](unit-4-rpi/lab-05-chassis.md) | Lab |
| **CPT: Sumo Robot** | [cpt-sumo-robot.md](unit-4-rpi/cpt-sumo-robot.md) | CPT spec (summative, 15% of course mark) |
| CPT Design Doc Template | [cpt-design-doc-template.md](unit-4-rpi/cpt-design-doc-template.md) | Template |
| CPT Tournament Bracket | [cpt-tournament-bracket.md](unit-4-rpi/cpt-tournament-bracket.md) / `.xlsx` (generated by `generate_bracket.py`) | Reference |

Also in `unit-4-rpi/`: `gpio_sim.py` (a GPIO simulator for testing lab code off-hardware) and `wave-sampling-explorer.html` (an interactive sample-rate/bit-depth demo for the analog/digital notes).

**Teacher-only support material** (not linked from student pages): [`_planning/rpi-network-scan.md`](_planning/rpi-network-scan.md) for locating imaged Pis on the school SSID, and [`_planning/cpt-reference-2025/`](_planning/cpt-reference-2025/) for last year's archived robot code — read its `README.md` before teaching the labs; it has a ready-made table of real student bugs mapped to the day you'd want to pre-empt each one.

A written unit test lands on Day 14 (after the chassis build days, deliberately — see the overview's "Key Decisions"); as with the other units, the test paper itself is deliberately not stored in this public repo (see [`_planning/README.md`](_planning/README.md)).

---

## Final Exam

[`final-exam-review.md`](final-exam-review.md) — student-facing review guide. Eight sections (MC/matching + written), 70 marks total, spanning all four units. The Boolean Laws reference table it points to is also the one distributed with the actual exam.
