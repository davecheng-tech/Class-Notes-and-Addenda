# Unit 3: Digital Logic — Overview

**Course:** TEJ4M — Computer Engineering Technology (Grade 12)\
**Duration:** 16 periods × 60 minutes\
**Prerequisites:** Unit 2 (Linux and Processor Architecture) — students understand CPU architecture, instruction sets, binary. Unit TEJ3M — students built all 7 basic logic gates in CircuitVerse and on a TinkerCAD breadboard.

## Unit Arc

This unit answers the question: **How does a CPU actually compute anything?**

Unit 2 established that a CPU is a processor with an instruction set. This unit goes one level deeper: a CPU is billions of transistors — switches — arranged into logic gates, which combine into circuits that can perform arithmetic and make decisions. Students move from review (the 7 gates) through the design language of digital logic (truth tables, circuits, equations) to Boolean algebra simplification, and culminate in building a functional 4-bit ALU in CircuitVerse.

The unit has two natural halves:
- **Combinational logic** (notes 01–03): the design language and how to work with it
- **ALU design** (note 04 + assignment): applying that language to build a real CPU component

## Sequencing

| Per. | Topic | Format | Deliverable | Notes file |
|------|-------|--------|-------------|------------|
| 1 | Transistors → binary → history → logic gates; 7-gate review | Lecture + start CircuitVerse activity | — | `01-from-transistors-to-gates.md` |
| — | **Homework:** Build all 7 gates in one CircuitVerse project (label inputs/outputs, test all combinations) | Independent | Completion | — |
| 2 | Four representations; SOP method; Truth Table → Circuit and Equation (car starter worked example) | Socratic + demo | — | `02-combinational-logic.md` §1–4 |
| — | **In-class practice:** A1–A2 (`practice-conversions.md`) — students build in CircuitVerse and verify | Paired | Completion | — |
| — | **Homework:** A3–A4 (`practice-conversions.md`) | Independent | Completion | — |
| 3 | All six conversions: Equation → Circuit (inside-out), Circuit → Equation, Circuit → Truth Table, Equation → Truth Table; summary conversion map | Socratic lecture + live CircuitVerse build demo | `homework.md` assigned (due period 5) | `02-combinational-logic.md` §5–9 |
| — | **In-class practice:** B1–B4 and Parts C, D (`practice-conversions.md`) as time allows | Independent | Completion | — |
| 4 | `homework.md` work period — all six conversion types | Independent with check-ins | `homework.md` in progress | — |
| 5 | Boolean simplification: laws, worked examples, before/after gate count | Lecture + guided practice | `homework.md` due | `03-boolean-simplification.md` |
| — | Homework review; Practice Parts A–B (`practice-simplification.md`) | — | Completion | — |
| 7 | Simplification practice + consolidation | Independent work | — | `practice-simplification.md` Parts B–C |
| 8 | Additional simplification practice — `practice-more-simplification.md` | Independent work | Completion | `practice-more-simplification.md` |
| 9 | ALU context; CircuitVerse multi-tab workflow demo; half adder + full adder derivation + build; 4-bit ripple carry concept | Lecture + guided build | Distribute `04-alu-design.md` and `practice-alu-guided-build.md` | `04-alu-design.md` §1–5 |
| 10 | Binary subtraction; half + full subtractor; 2-in-1 MUX; 1-bit 2-op mini-ALU (ADD/SUB) | Guided build together | `practice-alu-guided-build.md` Parts 1–4 in progress | `04-alu-design.md` §6–9, §11 |
| 11 | ANDer; LST unit; 4-in-1 MUX; complete 1-bit 4-op ALU; assign 4-bit project | Guided + independent | Distribute `alu-assignment.md`; distribute `alu-extension.md` to students working ahead | `04-alu-design.md` §10–12 |
| 12 | **Combinational logic test** (conversions + simplification) | Written, closed-note | **Summative (KU, APP, COMM, TIPS)** | — |
| 13 | Work period 1 — milestone: Tabs 1–4 (1-bit adder ref, 4-bit adder, 1-bit subtractor ref, 4-bit subtractor) | Independent with check-ins | Milestone: Tabs 1–4 complete and verified | — |
| 14 | Work period 2 — milestone: Tabs 5–7 (ANDer, LSTer, MUX ref) | Independent with check-ins | Milestone: Tabs 5–7 complete and verified | — |
| 15 | Work period 3 — milestone: Tab 8 (ALU assembly) + design document progress | Independent with check-ins | Milestone: Tab 8 wired; document intro + 2 sections drafted | — |
| 16 | ALU assignment due + demos; buffer | Submission + show-and-tell | **Summative (APP, KU, COMM, TIPS)** | — |

## Assessment Structure

- **Completion marks (homework + in-class practice):** Low-stakes, graded for completion. Purpose is to build fluency with conversions before the test and with CircuitVerse before the assignment.
- **7-gate CircuitVerse homework (after period 1):** Completion. Ensures students are functional in CircuitVerse before the unit depends on it.
- **Combinational logic test (period 12):** Summative, closed-note written assessment. Covers all six conversions and Boolean simplification. Moved to period 12 (after the ALU guided build) so students benefit from three additional periods of derivation practice before being assessed. Format drawn from the prior teacher's test (Spring 2025): students choose one of two conversion methods to explain for each KU question, then complete APP circuit problems, and answer COMM/TIPS reflection questions.
- **ALU assignment (due period 16):** Summative project. Students submit one CircuitVerse project (8 tabs) and a design document. Weighted toward Application; also assesses Knowledge (component designs), Communication (document structure), and Thinking (LST explanation).

### Test breakdown (period 12)

| Category | Question | Marks |
|----------|----------|-------|
| KU | Describe steps for one of: circuit → equation, equation → circuit | /2 |
| KU | Describe steps for one of: truth table → circuit, circuit → truth table | /2 |
| KU | Describe steps for one of: equation → truth table, circuit → equation | /2 |
| APP | Simplify a Boolean equation (≥2 laws, name them, gate count before/after) | /2 |
| APP | Convert truth table → circuit diagram | /2 |
| APP | Convert circuit diagram → Boolean equation | /2 |
| APP | Convert circuit diagram → truth table | /2 |
| COMM | How do you ensure all input combinations are covered in a truth table? | /1 |
| COMM | Naming pattern for inputs/outputs (A, B, C… / Z) | /1 |
| TIPS | Two benefits of Boolean algebra simplification | /2 |
| **Total** | | **/18** |

### ALU assignment breakdown (period 16)

| Category | Criteria | Marks |
|----------|----------|-------|
| APP | Circuit components working — 1 mark each (Adder, Subtractor, AND, LST, MUX) | /5 |
| APP | ALU tab: all four operations functional | /3 |
| COMM | Document format (intro, conclusion, subsections present) | /3 |
| KU | Component designs (truth table + equation + circuit for Adder, Subtractor, AND, MUX) | /4 |
| TIPS | LST explanation: how it was derived from an existing component | /1 |
| **Total** | | **/16** |

## Files

### Student-facing (in `unit-3-digital-logic/`)
- [x] `01-from-transistors-to-gates.md` — transistors, binary, history, 7-gate review
- [x] `02-combinational-logic.md` — all 6 conversions with worked examples and circuit images
- [x] `03-boolean-simplification.md` — laws, worked examples, before/after circuits
- [x] `04-alu-design.md` — half/full adder and subtractor, ANDer, LST, MUX, ALU structure; reference for the full ALU section
- [x] `practice-conversions.md` — Parts A–D, all conversion types
- [x] `practice-simplification.md` — equation → circuit, simplification practice, law reference
- [x] `practice-simplification-solutions.md` — solutions for `practice-simplification.md`
- [x] `practice-more-simplification.md` — additional simplification problems (Part C onward), increasing difficulty
- [x] `practice-more-simplification-solutions.md` — solutions for `practice-more-simplification.md`
- [x] `practice-alu-guided-build.md` — in-class guided build activity (periods 9–11); truth table derivation, CircuitVerse steps, verification checklists; doubles as a reference during the assignment
- [x] `homework.md` — independent practice set, due period 6
- [x] `alu-assignment.md` — CircuitVerse project spec, design document spec, test cases, milestones, rubric
- [x] `alu-extension.md` — optional extension challenges for students working ahead (add OR operation, overflow indicator, carry-lookahead adder)

### Teacher-facing (in `_planning/`)
- [x] `unit-3-overview.md` — this file
- [x] `unit-3-alu-lesson-plans.md` — detailed period-by-period lesson plans for the ALU section (periods 9–16), including timing, key questions, common misconceptions, and differentiation notes

## Open items
- Practice problems in `practice-conversions.md` Parts C and D use text-described circuits — consider adding CircuitVerse screenshots if students find them hard to follow from description alone
- `homework.md` is intentionally long (16 problems, all six conversion directions) — period 4 is a dedicated work period; students should not expect to finish it entirely at home after period 3
- ALU assignment: confirm CircuitVerse has a Splitter component available before assigning (needed for 4-bit bus routing)
- Buffer period at end of unit (period 16) doubles as ALU demo day — if demos run short, can use time for unit 4 preview or free build
