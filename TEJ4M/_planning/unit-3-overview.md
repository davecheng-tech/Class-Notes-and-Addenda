# Unit 3: Digital Logic — Overview

**Course:** TEJ4M — Computer Engineering Technology (Grade 12)\
**Duration:** 14 periods × 60 minutes\
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
| 8 | **Combinational logic test** (conversions + simplification) | Written, closed-note | **Summative (KU, APP, COMM, TIPS)** | — |
| 9 | ALU context + adder design: half adder → full adder → 4-bit chain | Lecture + build | — | `04-alu-design.md` §1–5 |
| — | **In-class:** Build 1-bit full adder in CircuitVerse before end of period | — | — | — |
| 10 | Subtractor design (half → full → 4-bit); ANDer | Lecture + build | — | `04-alu-design.md` §6–9 |
| 11 | LST unit; MUX (2-in-1 → 4-in-1); ALU structure overview | Lecture + build | — | `04-alu-design.md` §10–12 |
| — | **Introduce ALU assignment** | — | — | `alu-assignment.md` |
| 12 | ALU assignment work period 1 | Independent with check-ins | — | — |
| 13 | ALU assignment work period 2 | Independent with check-ins | — | — |
| 14 | ALU assignment due + demos; buffer | Submission + show-and-tell | **Summative (APP, KU, COMM, TIPS)** | — |

## Assessment Structure

- **Completion marks (homework + in-class practice):** Low-stakes, graded for completion. Purpose is to build fluency with conversions before the test and with CircuitVerse before the assignment.
- **7-gate CircuitVerse homework (after period 1):** Completion. Ensures students are functional in CircuitVerse before the unit depends on it.
- **Combinational logic test (period 8):** Summative, closed-note written assessment. Covers all six conversions and Boolean simplification. Format drawn from the prior teacher's test (Spring 2025): students choose one of two conversion methods to explain for each KU question, then complete APP circuit problems, and answer COMM/TIPS reflection questions.
- **ALU assignment (due period 14):** Summative project. Students submit one CircuitVerse project (8 tabs) and a design document. Weighted toward Application; also assesses Knowledge (component designs), Communication (document structure), and Thinking (LST explanation).

### Test breakdown (period 8)

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

### ALU assignment breakdown (period 14)

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
- [x] `04-alu-design.md` — half/full adder and subtractor, ANDer, LST, MUX, ALU structure
- [x] `practice-conversions.md` — Parts A–D, all conversion types
- [x] `practice-simplification.md` — equation → circuit, simplification practice, law reference
- [x] `practice-simplification-solutions.md` — solutions for `practice-simplification.md`
- [x] `practice-more-simplification.md` — additional simplification problems (Part C onward), increasing difficulty
- [x] `practice-more-simplification-solutions.md` — solutions for `practice-more-simplification.md`
- [x] `homework.md` — independent practice set, due period 6
- [x] `alu-assignment.md` — CircuitVerse project spec, design document spec, test cases, rubric

### Teacher-facing (in `_planning/`)
- [x] `unit-3-overview.md` — this file

## Open items
- Practice problems in `practice-conversions.md` Parts C and D use text-described circuits — consider adding CircuitVerse screenshots if students find them hard to follow from description alone
- `homework.md` is intentionally long (16 problems, all six conversion directions) — period 4 is a dedicated work period; students should not expect to finish it entirely at home after period 3
- ALU assignment: confirm CircuitVerse has a Splitter component available before assigning (needed for 4-bit bus routing)
- Buffer period at end of unit (period 14) doubles as ALU demo day — if demos run short, can use time for unit 4 preview or free build
