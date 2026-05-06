# ALU Assignment

## Goal

Build the Arithmetic Logic Unit (ALU) portion of a CPU using CircuitVerse. Your ALU will support 4-bit inputs, 4-bit output, and four operations selected by a 2-bit control signal.

This assignment requires both a working CircuitVerse project and a written design document.

---

## The ALU Specification

| Control | Operation | Description |
|---------|-----------|-------------|
| 00 | ADD | Add A and B (4-bit result) |
| 01 | SUB | Subtract B from A (4-bit result) |
| 10 | AND | Bitwise AND of A and B |
| 11 | LST | Less Than: output 0001 if A < B, else 0000 |

---

## CircuitVerse Project

Submit **one CircuitVerse project** with a separate tab for each component:

| Tab | Component | Description |
|-----|-----------|-------------|
| 1 | Full Adder (1-bit) | Single-bit full adder for design reference |
| 2 | 4-bit Adder | Four full adders chained with ripple carry |
| 3 | Full Subtractor (1-bit) | Single-bit full subtractor for design reference |
| 4 | 4-bit Subtractor | Four full subtractors chained with ripple borrow |
| 5 | ANDer (4-bit) | Four independent AND gates |
| 6 | LSTer (4-bit) | Less Than unit |
| 7 | MUX (2-in-1, 1-bit) | Basic multiplexer for design reference |
| 8 | ALU (4-bit, 4-function) | All components connected through a 4-in-1 MUX |

Label all inputs and outputs on every tab. Use the label/annotation tool in CircuitVerse to name each sub-component.

**MUX note:** Tab 7 must be built from basic gates (AND, OR, NOT) — this is the design you'll document. For Tab 8 (the ALU assembly), you may use CircuitVerse's built-in Multiplexer component configured as a 4-in-1 selector, or instantiate your Tab 7 design as a subcircuit. Either is acceptable.

---

## Work Period Milestones

Use these targets to pace your work across the three work periods.

| End of period | Target |
|---------------|--------|
| Work period 1 | Tabs 1–4 complete and verified. At minimum, Tab 2 (4-bit adder) should pass: A=0011, B=0101, Control=00 → Z=1000. |
| Work period 2 | Tabs 5–7 complete and verified. Tab 6 (LSTer) should pass: A=0011, B=0101 → Z=0001; A=0101, B=0011 → Z=0000. |
| Work period 3 | Tab 8 (ALU) wired and all five test cases passing. Design document introduction and at least two component sections written. |

If you're ahead of a milestone, start on the design document section for whichever component you just finished — the details are freshest right after building.

---

## Design Document

Submit a Google Doc alongside your CircuitVerse project. It must include:

1. **Introduction** — What is an ALU? What does your ALU do?
2. **Full Adder Design** — 1-bit truth table, Boolean equations for sum and carry out, circuit diagram or screenshot
3. **Full Subtractor Design** — 1-bit truth table, Boolean equations for difference and borrow out, circuit diagram or screenshot
4. **ANDer Design** — 1-bit truth table, Boolean equation, circuit diagram or screenshot
5. **LSTer Design** — Explain in words or with a diagram how the Less Than unit was built. Which other component does it reuse?
6. **MUX Design** — 1-bit 2-in-1-out truth table, Boolean equation, circuit diagram or screenshot
7. **Conclusion** — Describe one thing that surprised or challenged you during this project

Each design section should be its own subsection. Use clear headings.

---

## Testing Your ALU

Before submitting, test each operation manually:

**ADD test:** Set A = 0011 (3), B = 0101 (5), Control = 00. Expected output: 1000 (8).

**SUB test:** Set A = 0111 (7), B = 0011 (3), Control = 01. Expected output: 0100 (4).

**AND test:** Set A = 1010, B = 1100, Control = 10. Expected output: 1000.

**LST test (A < B):** Set A = 0011 (3), B = 0101 (5), Control = 11. Expected output: 0001.

**LST test (A ≥ B):** Set A = 0101 (5), B = 0011 (3), Control = 11. Expected output: 0000.

Include screenshots of at least two of these tests in your design document.

---

## Assessment Rubric

Achievement levels correspond to Ontario grading bands:

- **Level 1:** 50–59%
- **Level 2:** 60–69%
- **Level 3:** 70–79%
- **Level 4 / 4+:** 80–100%

<br>

### Circuit Functionality — /20 (Application)

**Assesses whether each component works correctly and whether the full ALU integrates them all. Each tab should function independently; the ALU tab must route all four operations correctly through the MUX.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All eight tabs functional and all five standard test cases pass. Student has gone beyond the spec: overflow behaviour documented, additional test cases explored, or a genuine extension (e.g., a fifth operation, wider bit-width, additional subcircuit). |
| **4** | All eight tabs functional. All five standard test cases pass in the ALU tab. |
| **3** | Most tabs functional. ALU tab is wired and most operations work; one operation may fail or produce unexpected output on edge cases. |
| **2** | Some tabs functional; others are incomplete or produce incorrect output. ALU tab is partially wired or has multiple operations failing. |
| **1** | Few tabs functional. ALU tab is missing or non-functional. |

<br>

### Schematic Style & Conventions — /10 (Application)

**Assesses how well the CircuitVerse project follows schematic drawing conventions. Circuits should be readable to someone who has never seen them before.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All conventions followed consistently across every tab. Signal flows left to right; data and control signals are visually distinct; stubs are present on gate pins before any wire turns; parallel components (e.g., the four 1-bit operation units) are aligned; every input and output is labelled with consistent naming across tabs. The circuit reads as a professional diagram. |
| **4** | Conventions followed in most tabs with only minor lapses. Labelling is consistent across tabs. Signal flow direction and data/control separation are clear. |
| **3** | Conventions followed in places but inconsistently applied. Most inputs and outputs are labelled. One or two conventions (e.g., pin stubs, data/control separation) may be missing or unclear in some tabs. |
| **2** | Some labelling present but conventions are largely unobserved. Wires turn immediately at gate pins, parallel components are misaligned, or data and control signals are difficult to distinguish. |
| **1** | Little attention to conventions. Circuits are difficult to read and trace. Few or no labels on inputs and outputs. |

<br>

### Design Document — /20 (Knowledge & Understanding / Communication)

**Assesses whether all required sections are present, technically accurate, and clearly explained. The document should demonstrate understanding of what was built, not just that something was built.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All sections present and technically rigorous. Truth tables are complete and correct. Boolean equations are correctly derived and simplified where applicable. The LSTer explanation identifies the underlying relationship to another component and explains *why* it works. Introduction and conclusion are substantive — the conclusion reflects genuinely on a challenge or surprise rather than restating what was built. |
| **4** | All sections present. Truth tables and equations are correct. The LSTer explanation correctly identifies the derived component and how it is reused. Screenshots are clear and relevant. Document uses consistent headings and is well organized. |
| **3** | All or nearly all sections present. Truth tables and equations are mostly correct with minor errors. The LSTer explanation is partially correct or lacks depth. Screenshots are included but may be loosely connected to the text. |
| **2** | Some sections missing or incomplete. Truth tables may have errors. Equations are absent or incorrect in places. The LSTer explanation is vague or missing. Screenshots are present but uncaptioned or poorly chosen. |
| **1** | Multiple required sections missing. Content is sparse and does not demonstrate understanding of the components designed. |

---

## Notes on CircuitVerse

- Save frequently. Use **File → Save Online** if signed in, or export regularly as a backup.
- Use the **Splitter** component to separate a 4-bit bus into individual bits when connecting to components that expect single-bit inputs.
- Name your inputs and outputs using the **Label** property in the properties panel — this makes the project much easier to read and debug.
- The 4-in-1 MUX in the ALU tab can be built by combining three 2-in-1 MUXes (see the design notes).
- Test each tab independently before wiring the final ALU tab.

---

## Reference: ALU Operation Truth Table (for testing)

Fill this table in as you test your final ALU. All values are in binary.

| A | B | Control | Expected Z | Your ALU Z | Correct? |
|---|---|---------|------------|------------|----------|
| 0011 | 0101 | 00 (ADD) | 1000 | | |
| 0111 | 0011 | 01 (SUB) | 0100 | | |
| 1010 | 1100 | 10 (AND) | 1000 | | |
| 0011 | 0101 | 11 (LST) | 0001 | | |
| 0101 | 0011 | 11 (LST) | 0000 | | |
| 1111 | 0001 | 00 (ADD) | — | | (overflow — what happens?) |
