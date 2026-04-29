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

## Evaluation

| Category | Criteria | Marks |
|----------|----------|-------|
| **APP** | Circuit components built and working — 1 mark per component (Adder, Subtractor, AND, LST, MUX) | /5 |
| **APP** | ALU tab: all components connected and all four operations functional | /3 |
| **COMM** | Document format: introduction, conclusion, all subsections present and clear | /3 |
| **KU** | Component designs: truth tables, equations, and circuit screenshots (one mark each for Adder, Subtractor, AND, MUX) | /4 |
| **TIPS** | LSTer explanation: correctly explains how the Less Than unit was derived from another component | /1 |
| **Total** | | /16 |

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
