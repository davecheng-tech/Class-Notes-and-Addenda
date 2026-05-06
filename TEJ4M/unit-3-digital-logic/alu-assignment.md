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

Submit **one CircuitVerse project** organized into tabs — one tab per component or sub-component. The minimum required components are listed below, but the total number of tabs will depend on how you decompose your design.

**Required components:**

| Component | Description |
|-----------|-------------|
| Full Adder (1-bit) | Single-bit full adder for design reference. |
| Adder (4-bit) | A 4-bit adder built from 1-bit full adders chained with ripple carry. If you prefer to build bottom-up, you may use separate tabs for a half adder and a full adder before the 4-bit adder. |
| Full Subtractor (1-bit) | Single-bit full subtractor for design reference. |
| Subtractor (4-bit) | A 4-bit subtractor built from 1-bit full subtractors chained with ripple borrow. |
| ANDer (4-bit) | Four independent AND gates. |
| LSTer (4-bit) | Less Than unit. |
| MUX 2:1 (1-bit) | A 1-bit 2-to-1 multiplexer built from basic gates (AND, OR, NOT). |
| MUX 4:1 (1-bit) | A 1-bit 4-to-1 multiplexer built by cascading your MUX 2:1 (1-bit) subcircuit instances. **Do not use CircuitVerse's built-in Multiplexer component.** |
| MUX 4:1 (4-bit) | Four MUX 4:1 (1-bit) subcircuit instances, one per output bit, each wired independently. This tab abstracts the full 4-bit selection into a single subcircuit so the ALU tab stays clean. **Do not use CircuitVerse's built-in Multiplexer component.** |
| ALU (4-bit, 4-function) | All four operation units connected through your MUX 4:1 (4-bit) subcircuit. Keep this tab as clean as possible — use subcircuits for every component rather than rebuilding gates directly. |

You may also add tabs for additional sub-components. Examples:
- A **Half Adder (1-bit)** tab before your full adder, if you are building bottom-up
- An **OVF gate** tab — overflow detection logic that suppresses the overflow flag when the operation is AND or LST, since those operations do not produce arithmetic overflow

Label all inputs and outputs on every tab. Use the label/annotation tool in CircuitVerse to name each sub-component.

**MUX hierarchy:** The multiplexer is built in three stages: (1) MUX 2:1 (1-bit) from basic gates; (2) MUX 4:1 (1-bit) by cascading three MUX 2:1 (1-bit) subcircuit instances; (3) MUX 4:1 (4-bit) by cascading four MUX 4:1 (1-bit) subcircuit instances. In the ALU tab, use your MUX 4:1 (4-bit) as a single subcircuit. Do not use CircuitVerse's built-in Multiplexer component at any stage.

---

## Work Period Milestones

Use these targets to pace your work across the three work periods.

| End of period | Target |
|---------------|--------|
| Work period 1 | 4-bit Adder and 4-bit Subtractor complete and verified. Adder: A=0011, B=0101 → Z=1000. Subtractor: A=0111, B=0011 → Z=0100. |
| Work period 2 | ANDer, LSTer, and all three MUX tabs complete and verified. LSTer: A=0011, B=0101 → Z=0001; A=0101, B=0011 → Z=0000. MUX 4:1 (4-bit) verified with all four control combinations. |
| Work period 3 | ALU tab wired and all five test cases passing. Design document at least half complete — introduction and sections 2–4 written. |

If you're ahead of a milestone, start on the design document section for whichever component you just finished — the details are freshest right after building.

---

## Design Document

Submit a Google Doc alongside your CircuitVerse project. Your guided build notes already contain the 1-bit truth tables and Boolean equations — your document should go beyond that and demonstrate understanding of the **4-bit design and how it is constructed from 1-bit components**.

Required sections:

1. **Introduction** — In your own words: what is an ALU? Describe what your 4-bit ALU does, list all four operations, and explain how the 2-bit control signal selects among them.

2. **4-bit Adder** — Explain how four 1-bit full adders chain together using ripple carry. Include a screenshot of your 4-bit adder tab and trace one test case step by step, showing how carry propagates from bit 0 through to bit 3. (Suggested: A = 0111, B = 0001.)

3. **4-bit Subtractor** — Explain how four 1-bit full subtractors chain together using ripple borrow. Include a screenshot and trace one test case showing how borrow propagates across the four stages.

4. **ANDer and LSTer** — Include a screenshot of each 4-bit unit. For the LSTer specifically: which output of which component produces the Less Than signal, and why does that output indicate A < B? Verify with two test cases — one where A < B and one where A ≥ B.

5. **MUX Design** — Document both stages of the MUX hierarchy. First, explain how three MUX 2:1 (1-bit) subcircuits cascade to produce a MUX 4:1 (1-bit), and include a screenshot of that tab. Then explain how four MUX 4:1 (1-bit) subcircuits combine to produce a MUX 4:1 (4-bit), and include a screenshot of that tab. Include a table showing how C1 and C0 together select each of the four operations.

6. **ALU Architecture** — Describe how all components connect in the ALU tab. What four signals feed into the MUX? What controls the MUX? Include a screenshot of your ALU tab and a completed verification table showing all five standard test cases, your ALU's actual output for each, and whether each passed.

7. **Conclusion** — Describe one thing that surprised or challenged you during this project.

Each section must have a clear heading. Sections 2–6 must include screenshots of the corresponding CircuitVerse tab.

---

## Testing Your ALU

Before submitting, test each operation manually:

**ADD test:** Set A = 0011 (3), B = 0101 (5), Control = 00. Expected output: 1000 (8).

**SUB test:** Set A = 0111 (7), B = 0011 (3), Control = 01. Expected output: 0100 (4).

**AND test:** Set A = 1010, B = 1100, Control = 10. Expected output: 1000.

**LST test (A < B):** Set A = 0011 (3), B = 0101 (5), Control = 11. Expected output: 0001.

**LST test (A ≥ B):** Set A = 0101 (5), B = 0011 (3), Control = 11. Expected output: 0000.

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
| **4+** | All required tabs functional and all five standard test cases pass. Student has gone beyond the spec: overflow behaviour documented, an OVF gate implemented, additional test cases explored, or a genuine extension (e.g., a fifth operation, wider bit-width, additional subcircuit). |
| **4** | All required tabs functional. All five standard test cases pass in the ALU tab. |
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

**Assesses whether all required sections are present and demonstrate understanding of the 4-bit design — not just that the guided build was completed.**

| Level | Descriptor |
|:-----:|------------|
| **4+** | All sections present and technically rigorous. Ripple carry and ripple borrow traces are correct bit-by-bit. The MUX 4:1 section clearly explains the cascading structure and correctly shows the full control encoding. The LSTer explanation identifies the exact output used and explains the logic of why it signals A < B. Introduction and conclusion are substantive — the conclusion reflects genuinely on a challenge or surprise. |
| **4** | All sections present. Ripple carry and ripple borrow traces are correct. MUX 4:1 control encoding table is correct. LSTer explanation correctly identifies which component output is used and why. Screenshots are clear and correspond to the described tab. Document uses consistent headings and is well organized. |
| **3** | All or nearly all sections present. Carry and borrow traces are attempted but may have minor errors. MUX 4:1 section explains cascading but the control encoding may be incomplete. LSTer explanation is partially correct or lacks depth. Screenshots are included but may be loosely connected to the text. |
| **2** | Some sections missing or incomplete. Carry and borrow propagation is not explained or is incorrect. MUX 4:1 and LSTer explanations are vague or missing. Screenshots are present but uncaptioned or poorly chosen. |
| **1** | Multiple required sections missing. Content is sparse and does not demonstrate understanding of the 4-bit design. |

---

## Notes on CircuitVerse

- Save frequently. Use **Project → Export as File** if not signed in. Older versions of the `.cv` file can be kept as backup for version history.
- Name your inputs and outputs using the **Label** property in the properties panel — this makes the project much easier to read and debug.
- Build your multiplexer in three stages: MUX 2:1 (1-bit) from basic gates → MUX 4:1 (1-bit) by cascading three MUX 2:1 (1-bit) instances → MUX 4:1 (4-bit) by cascading four MUX 4:1 (1-bit) instances. Do not use the built-in Multiplexer component at any stage. Use your MUX 4:1 (4-bit) as a single subcircuit in the ALU tab.
- Test each tab independently before wiring the final ALU tab.

