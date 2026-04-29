# Unit 3: ALU Section — Detailed Lesson Plans (Periods 9–16)

These plans cover the ALU design section of Unit 3. The combinational logic section (periods 1–8) is in `unit-3-overview.md`. These plans assume:
- Students have passed the combinational logic test (period 8)
- Fluency with truth table → equation → circuit conversion (all 6 directions)
- Some CircuitVerse experience (single-tab circuits from earlier in the unit)

The core pedagogical arc: **familiar workflow (truth table → equation → circuit) applied to new circuits**, then building toward the ALU in stages — 1-bit components → 1-bit ALU together → 4-bit ALU independently.

---

## Materials by Period

| Period | Distribute to students |
|--------|----------------------|
| 9 | `04-alu-design.md`, `practice-alu-guided-build.md` |
| 10 | — (already distributed) |
| 11 | — |
| 12 | `alu-assignment.md`; `alu-extension.md` (for students working ahead) |
| 13–16 | — |

The class guided build (periods 9–12) uses a separate CircuitVerse project from the assignment. Make this explicit on day 1: students create a learning project in class, then start a fresh project for the assignment.

---

## Period 9 — ALU Context + CircuitVerse Multi-Tab Workflow + Half Adder

**Goal:** Students understand what an ALU does, can navigate CircuitVerse's multi-tab project structure, and have built and tested a working half adder.

**Distribute:** `04-alu-design.md` and `practice-alu-guided-build.md`

### Timing

| Time | Activity |
|------|----------|
| 0–10 | What is an ALU? |
| 10–20 | CircuitVerse multi-tab workflow demo |
| 20–50 | Half adder derivation + build |
| 50–60 | Verify, wrap-up |

### What is an ALU? (10 min)

Return to the Unit 2 framing: a CPU executes an instruction set. Each instruction is carried out by hardware. Today students go one level deeper — the hardware that does the arithmetic.

Put the ALU block diagram from `04-alu-design.md` §1 on the projector. Don't explain all of it — just show it as the destination. "By the end of this section, you'll have built this."

Key questions:
- "What operations do you think the bare minimum useful ALU would need?"
- "Why would you need a control signal?" → one circuit performing multiple operations, selected at runtime

Establish the spec: 4-bit inputs A and B, 2-bit control, 4 operations (ADD, SUB, AND, LST).

### CircuitVerse Multi-Tab Workflow (10 min)

Open CircuitVerse on the projector with a new blank project.

Walk through explicitly:
1. Rename Tab 1 by double-clicking its name → type "Half Adder"
2. Place an AND gate. Add labeled inputs A and B, labeled output Y. Test it.
3. Click the + icon to create Tab 2. Name it "Full Adder". Leave it empty.
4. Switch between tabs. Show they're independent circuits in the same project.
5. Briefly show Subcircuits: in the Circuits panel, one tab can be dragged into another as a component. Say: "this exists and you'll use it in the assignment — we'll return to it." Don't dwell.

Say: "This is how we'll organize the ALU. Every component gets its own tab. You test each tab independently before connecting them. The final ALU tab assembles everything."

### Half Adder (30 min)

On the board:
```
Half Adder: adds two single bits.
Inputs: A, B
Outputs: Z (sum), Y (carry out)
```

Have students fill in the output columns on Part 1 of `practice-alu-guided-build.md` before revealing the answers (2–3 minutes).

| A | B | Z | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Ask: "What pattern does Z follow?" → outputs 1 when inputs differ → XOR

Ask: "What pattern does Y follow?" → outputs 1 only when both are 1 → AND

Write equations: `Z = A ⊕ B`, `Y = A · B`

Ask: "How many gates?" → 2 total. Simple.

Students build on Tab 1 of a **new CircuitVerse project** (emphasise: new project, not the same one as earlier in the unit). Circulate and check:
- Inputs labeled A and B; outputs labeled Z and Y
- Tab named "Half Adder"
- Both gates present

Verify as a class: go through all 4 input combinations.

Wrap-up: "Notice we used the exact same process you've been practising for weeks — truth table to equation to circuit. New circuit, same method. It's called a *half* adder because it can't handle a carry arriving from a previous column. We fix that next class."

### Watch For

- **XOR vs. OR confusion:** The truth table is the authority. 1⊕1=0 is the distinguishing row. If a student uses an OR gate for Z, their circuit will fail on A=1, B=1.
- **Tab naming:** Some students won't see that you double-click to rename. Walk the whole class through it before they start.
- **New vs. old project:** Students may open a previous CircuitVerse project. Check at the start of the build that everyone has a fresh project.
- **CircuitVerse slowness or issues:** If the tool is unresponsive, have students draw the half adder on paper. They can build in CircuitVerse at the start of period 10.

---

## Period 10 — Full Adder: Derivation + Build

**Goal:** Students derive and build a full adder in CircuitVerse and understand how four of them chain into a 4-bit adder.

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Binary addition review |
| 5–25 | Full adder derivation (guided) |
| 25–50 | Build in CircuitVerse |
| 50–60 | 4-bit ripple carry concept |

### Binary Addition Review (5 min)

On the board:
```
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10  ← sum = 0, carry = 1
```

"When two bits sum to 2, we generate a carry into the next column. In multi-bit addition, each column may also receive a carry from the column to its right. A full adder handles that carry coming *in*."

### Full Adder Derivation (20 min)

Three inputs: A, B, Cin. Two outputs: Z (sum), Cout.

Have students fill in the 8-row truth table on Part 2 of `practice-alu-guided-build.md` independently (3–4 minutes). Then fill it in together on the board.

After the truth table, have students attempt to derive the equations using SOP — they've done this many times. Give them 3–4 minutes before stepping in.

Target equations:
- `Z = A ⊕ B ⊕ Cin` — the sum is XOR of all three inputs
- `Cout = AB + ACin + BCin` — carry out when any two of the three inputs are 1

Ask: "How would you build Z? You could go straight from the truth table, but we already have something that computes A ⊕ B — what is it?" → the half adder. Point out that Z = (A ⊕ B) ⊕ Cin: chain two XORs.

Show the two-half-adder construction (also in `04-alu-design.md` §4):
```
Half Adder 1: A, B → partial sum S1 = A ⊕ B, partial carry C1 = A·B
Half Adder 2: S1, Cin → sum Z = S1 ⊕ Cin, partial carry C2 = S1·Cin
Final carry: Cout = C1 + C2  (one OR gate)
```

This is the modular insight — the half adder becomes a building block.

### Build (25 min)

Tab 2: "Full Adder (1-bit)"

Recommend building from two half adders + OR gate (enforces modular thinking). Students who are ahead can try building from scratch from the truth table equations — both are valid.

Have students use the half adder logic directly (either redraw the XOR and AND gates, or use Tab 1 as a subcircuit if they're comfortable with that from the demo).

Verify all 8 input combinations. Have students check off on the guided build sheet.

### 4-Bit Ripple Carry Concept (10 min)

Draw on the board:
```
Bit 1 (LSB)     Bit 2           Bit 3           Bit 4 (MSB)
┌──────┐        ┌──────┐        ┌──────┐        ┌──────┐
│ Full │─Cout─▶ │ Full │─Cout─▶ │ Full │─Cout─▶ │ Full │─▶ Overflow
│ Add  │        │ Add  │        │ Add  │        │ Add  │
└──┬───┘        └──┬───┘        └──┬───┘        └──┬───┘
   Z1              Z2              Z3              Z4
Cin=0
```

"The carry-out of each adder feeds into the carry-in of the next. The first adder's Cin is always 0. The carry-out of the last adder is an overflow flag — it means the result didn't fit in 4 bits."

Don't build it yet. This is conceptual setup for the assignment. Students will build the 4-bit adder in period 13.

### Watch For

- **SOP derivation of Cout:** Students often miss that the three SOP terms simplify to AB + ACin + BCin. A useful frame: "carry out when any two of the three inputs are 1." Let them work through it; don't simplify for them immediately.
- **Building the full adder from scratch vs. from two half adders:** Both approaches work in CircuitVerse. The two-half-adder approach is preferred — it's modular and sets up the subcircuit concept. If a student builds it from scratch, that's fine but note the connection.
- **OR gate for Cout:** Students often forget this gate. "C1 or C2 — if either half adder produced a carry, we carry out."
- **Floating Cin:** Students may leave Cin unconnected. In CircuitVerse this defaults to 0, but they should wire a constant 0 explicitly.

---

## Period 11 — Full Subtractor + 2-in-1 MUX + 1-bit 2-op Mini-ALU

**Goal:** Students build a full subtractor and a 2-in-1 MUX, then wire a 1-bit mini-ALU that selects between ADD and SUB based on a single control bit. The payoff: flipping one bit changes the operation.

### Timing

| Time | Activity |
|------|----------|
| 0–10 | Binary subtraction + half subtractor |
| 10–25 | Full subtractor build |
| 25–40 | 2-in-1 MUX concept + build |
| 40–58 | Wire 1-bit 2-op mini-ALU |
| 58–60 | Verify, celebrate |

### Binary Subtraction + Half Subtractor (10 min)

On the board:
```
0 - 0 = 0
1 - 0 = 1
1 - 1 = 0
0 - 1 = 1, borrow 1   ← just like decimal: 10 - 1 = 1, borrow from next column
```

Half subtractor truth table (4 rows):

| A | B | Z (difference) | Y (borrow out) |
|---|---|----------------|----------------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

Ask students to derive: `Z = A ⊕ B` (same as half adder sum), `Y = A'·B` (borrow only when A=0 and B=1).

Point out: "The difference equation is identical to the sum equation — XOR. Only the borrow logic differs from the carry. The subtractor and adder are more similar than they look."

### Full Subtractor Build (15 min)

Have students fill in the 8-row full subtractor truth table on Part 3 of `practice-alu-guided-build.md` independently (3–4 min). Hint on the sheet reminds them: borrow out when A had to borrow.

Equations:
- `Z = A ⊕ B ⊕ Bin`
- `Bout = A'B + A'Bin + BBin`

If students struggle with Bout, guide: "Under what conditions does A have to borrow? When A is too small — when A=0. So the first two terms both start with A'."

Tab 3: "Full Subtractor (1-bit)" — students build and verify all 8 combinations.

### 2-in-1 MUX (15 min)

Ask: "I have an adder result and a subtractor result. I want one output that gives me either one depending on a control bit. When control is 0, I want the adder result. When control is 1, I want the subtractor result. How do I build that?"

Give students a minute to think before showing the truth table. Inputs: A (data 0), B (data 1), C (control). Output: Z.

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Equation: `Z = A·C' + B·C`

Ask students to read this: "when C=0, what does Z equal?" → A. "When C=1?" → B. The equation literally says: pass A when C=0, pass B when C=1.

Circuit: AND gate (A with C'), AND gate (B with C), OR gate combining both outputs. Three gates total.

Tab 4: "MUX (2-in-1, 1-bit)" — build and verify. Confirm: Z follows A when C=0, Z follows B when C=1.

### Wire the 1-bit Mini-ALU (18 min)

Tab 5: "Mini-ALU (1-bit, 2-op)"

Wiring diagram (draw on board and in the guided build sheet):
```
      A ──┬──▶ Full Adder ──▶ sum Z ──▶ MUX input A (data 0)
          │
      B ──┤
          │
          └──▶ Full Subtractor ──▶ diff Z ──▶ MUX input B (data 1)

Cin = 0 ──▶ Full Adder (hardwired)
Bin = 0 ──▶ Full Subtractor (hardwired)
Control ──▶ MUX control (C)
MUX output ──▶ ALU output Z
```

Key point: A and B go to *both* the adder and subtractor simultaneously. Both circuits are always computing. The MUX selects which result reaches the output.

Test cases (go through as a class):

| A | B | Control | Expected Z |
|---|---|---------|------------|
| 1 | 0 | 0 (ADD) | 1 |
| 1 | 0 | 1 (SUB) | 1 |
| 1 | 1 | 0 (ADD) | 0 (carry=1) |
| 1 | 1 | 1 (SUB) | 0 |
| 0 | 1 | 1 (SUB) | 1 (with borrow) |

Flip the control bit. Watch the output change. **This is the moment.** Students see a circuit that literally changes what it does based on an input bit.

Say: "You just built a circuit that performs two different arithmetic operations and selects between them in real time. The control bit tells the MUX which result to let through. This is the core idea behind every ALU ever designed."

### Watch For

- **Full subtractor Bout derivation:** Students often forget the A' in the first two terms. Guide: "borrow happens when A doesn't have enough — when A=0. So the terms where A has to borrow all start with A'."
- **Shared A and B inputs:** Students commonly wire A and B to only the adder or only the subtractor. Be explicit: "both circuits need to see A and B. Run wires from A to both inputs. Same for B."
- **Cin/Bin wired to 0 explicitly:** Students may leave them floating. Show how to place a constant-0 input in CircuitVerse.
- **Students who aren't caught up:** If students haven't finished the full adder from period 10, have them skip to the MUX (Part 4a) and come back to the subtractor during the next period.

---

## Period 12 — ANDer + LST + 4-in-1 MUX + Complete 1-bit ALU + Assignment

**Goal:** Complete the 1-bit ALU with all 4 operations. Students have a working proof-of-concept before the 4-bit assignment starts.

**Distribute:** `alu-assignment.md` at the end of the period; `alu-extension.md` for students working ahead.

### Timing

| Time | Activity |
|------|----------|
| 0–10 | ANDer (independent) |
| 10–25 | LST — guided discovery |
| 25–40 | 4-in-1 MUX construction |
| 40–50 | Complete 1-bit ALU — wire and verify all 4 operations |
| 50–60 | Assignment introduction + milestone overview |

### ANDer (10 min)

"Add bitwise AND to the ALU. For 1 bit, what does that circuit look like?"

Students work independently. Tab 6: "ANDer (1-bit)" — one AND gate, inputs A and B, output Z. Verify. Fast.

### LST — Guided Discovery (15 min)

"Less Than. We want Z=1 if A < B, else Z=0. Before I show you how to build it — think about which of the components we've already built might be useful here."

Give students 2 minutes to think, then guide with questions:
1. "Which component computes A − B?" → Full subtractor
2. "If A=0 and B=1, does the subtractor have to borrow?" → Yes, Bout=1
3. "If A=1 and B=0, does it borrow?" → No, Bout=0
4. "So what does Bout=1 tell you about the relationship between A and B?" → A was smaller than B — A < B
5. "So how do we build LST?" → Z = Bout of the full subtractor. That's it.

**Don't give away the answer before they work through the questions.** Most students get there by question 4. If someone is still stuck at question 5, give a direct hint: "If the subtractor had to borrow, it means A didn't have enough. What does that tell you?"

Tab 7: "LST (1-bit)" — wire a full subtractor with Bin=0. The ALU output Z = Bout.

Verify:
- A=0, B=1 → Z=1 (0 < 1 ✓)
- A=1, B=0 → Z=0 (1 < 0 ✗ → correct)
- A=1, B=1 → Z=0 (1 < 1 ✗ → correct)
- A=0, B=0 → Z=0 (0 < 0 ✗ → correct)

### 4-in-1 MUX (15 min)

"We have 4 operations. We need to select among 4 results with a 2-bit control C1 C0. We know how to build a 2-in-1 MUX. Can we build a 4-in-1 from three of them?"

Draw on the board:
```
MUX 1: inputs ADD, SUB → control C0 → output Out1
         (C0=0: ADD, C0=1: SUB)

MUX 2: inputs AND, LST → control C0 → output Out2
         (C0=0: AND, C0=1: LST)

MUX 3: inputs Out1, Out2 → control C1 → final output Z
         (C1=0: from MUX 1, C1=1: from MUX 2)
```

Control table:
| C1 | C0 | Operation |
|----|----|-----------|
| 0 | 0 | ADD |
| 0 | 1 | SUB |
| 1 | 0 | AND |
| 1 | 1 | LST |

This matches the assignment spec: control 00=ADD, 01=SUB, 10=AND, 11=LST.

Students build three 2-in-1 MUX instances and wire them as described. Update Tab 5 (or add to the project).

### Complete 1-bit ALU (10 min)

Wire all four operation outputs into the 4-in-1 MUX structure. Update the ALU tab.

Test all four operations:

| A | B | C1 C0 | Expected Z |
|---|---|-------|------------|
| 1 | 0 | 00 | 1 (ADD: 1+0=1) |
| 1 | 0 | 01 | 1 (SUB: 1-0=1) |
| 1 | 1 | 10 | 1 (AND: 1·1=1) |
| 0 | 1 | 11 | 1 (LST: 0<1 → true) |
| 1 | 0 | 11 | 0 (LST: 1<0 → false) |

### Assignment Introduction (10 min)

Distribute `alu-assignment.md`.

"You just built a 1-bit version of this entire ALU — half adder, full adder, subtractor, AND, LST, MUX, everything. The assignment is to build it for 4 bits. The architecture is identical. You scale each component."

Walk through the 8-tab structure:
- Tabs 1 and 3 are design reference tabs (1-bit full adder and 1-bit full subtractor) — similar to what you built in class
- Tabs 2 and 4 are the 4-bit versions — chain four 1-bit units with ripple carry/borrow
- Tab 5 is the ANDer — 4 AND gates, independent per bit
- Tab 6 is the LSTer — a 4-bit subtractor where Z1 = Bout of the MSB stage, Z2=Z3=Z4=0
- Tab 7 is the MUX reference — same 2-in-1 MUX from class
- Tab 8 is the ALU assembly — all components through four 4-in-1 MUXes (one per output bit)

Milestone targets:
- **End of period 13:** Tabs 1–4 built and verified
- **End of period 14:** Tabs 5–7 built and verified
- **End of period 15:** Tab 8 wired; design document structure drafted with at least two sections written

Hand out `alu-extension.md` to students who want to go further.

### Watch For

- **LST insight:** If a student truly cannot arrive at Z = Bout through the guided questions, give a very direct hint after question 4: "Bout=1 means A < B. So what should Z be when Bout=1?" That usually closes it.
- **4-in-1 MUX confusion:** The three-MUX structure is hard to visualise from description alone. Draw it clearly with labelled data inputs and control lines before students build. MUX 3 is the one students forget.
- **Students not finished with the mini-ALU:** Let them complete Parts 5–6 of the guided build at the start of this period before joining the ANDer/LST work.

---

## Period 13 — Work Period 1

**Milestone goal:** Tabs 1–4 complete and verified  
*Tab 1: Full Adder (1-bit) / Tab 2: 4-bit Adder / Tab 3: Full Subtractor (1-bit) / Tab 4: 4-bit Subtractor*

### Opening (5 min)

Remind students to start a **new CircuitVerse project** for the assignment — separate from the class learning project. Set the milestone expectation clearly.

Quick recommended order: Tab 1 (fast — same full adder from class) → Tab 2 (main challenge) → Tab 3 (fast — same full subtractor from class) → Tab 4.

### Common Issues to Watch For

**Ripple carry/borrow chain (Tabs 2 and 4):**
The most common error — students forget to connect Cout of adder N to Cin of adder N+1. Check that the carry/borrow chain is unbroken. In CircuitVerse, misrouted wires are easy to miss — have students zoom in and trace each connection.

**Using subcircuits:**
Students should instantiate their 1-bit full adder (Tab 1) as a subcircuit in Tab 2, not redraw the gates four times. If they're not sure how, demo subcircuit placement from the Circuits panel at the start of the period (2 min).

**First Cin = 0:**
The carry-in of the first (LSB) full adder is hardwired to 0. Students sometimes leave it floating.

**Test after building:**
Have students run the ADD test case: A=0011, B=0101 → expected sum 1000 (3+5=8). This is in `alu-assignment.md`. Running this one test case catches most wiring errors.

### Differentiation

- **Ahead of milestone:** Start the design document — Section 2 (Full Adder Design) is natural to write while the adder is fresh.
- **Behind milestone:** Focus on Tab 2 (4-bit adder) first — it carries the most marks of the first four tabs. Tab 1 is very fast (copy the class work). Tab 3 follows the same pattern as Tab 1.

---

## Period 14 — Work Period 2

**Milestone goal:** Tabs 5–7 complete and verified  
*Tab 5: ANDer (4-bit) / Tab 6: LSTer (4-bit) / Tab 7: MUX (2-in-1, 1-bit)*

### Opening (5 min)

Quick show-of-hands: who has Tabs 1–4 done? For anyone behind, set a personal target: "Get Tab 2 working before moving to Tab 5."

### Common Issues to Watch For

**ANDer (Tab 5):**
Four independent AND gates — one per bit position. No carry, no connections between bit positions. Should take 10–15 minutes. Students sometimes overthink this.

**LSTer (Tab 6):**
Students sometimes overcomplicate this. Clarify:
- Build a 4-bit subtractor (Tab 4 as subcircuit, or rebuild)
- Z1 = Bout of the **last** (MSB, bit 4) full subtractor stage
- Z2 = Z3 = Z4 = constant 0 (hardwired)
- The individual subtractor difference outputs Z1–Z4 are **not** the LSTer outputs

Test: A=0011 (3), B=0101 (5), expected LSTer output = 0001. A=0101 (5), B=0011 (3), expected = 0000.

**MUX reference (Tab 7):**
Same 2-in-1 MUX from class. Students can replicate it quickly. If they used Tab 4 of their class project as reference, this is trivial.

### Differentiation

- **Ahead:** Begin Tab 8 (ALU assembly), or write design document sections for components they've built.
- **Behind:** ANDer is the quickest mark — get Tab 5 done first. Then LSTer.

---

## Period 15 — Work Period 3

**Milestone goal:** Tab 8 wired; design document introduction and at least two component sections complete

### Opening (5 min)

Tab 8 is the assembly tab. Key reminders before students start:
- All four operation units (adder, subtractor, ANDer, LSTer) run simultaneously on A and B
- The output MUX selects which result reaches Z based on the 2-bit control
- The 4-in-1 MUX is 1 bit wide — four of them are needed, one per output bit, all sharing the same control signals
- Use the test cases in `alu-assignment.md` to verify each operation before submitting

### Common Issues to Watch For

**Four MUXes sharing control:**
Students sometimes build only one 4-in-1 MUX and wonder why only bit 1 works. Clarify: one MUX handles one output bit. Four output bits → four MUXes. All four MUXes use the same control lines C1 and C0.

**Bit-by-bit connections:**
The 4-bit adder produces four output bits (Z1, Z2, Z3, Z4). Wire Z1 of each operation unit (ADD Z1, SUB Z1, AND Z1, LST Z1) into the 4-in-1 MUX for output bit 1. Repeat for bits 2, 3, 4. Students sometimes try to connect 4-bit buses directly and get confused — walk them through the bit-by-bit approach.

**LSTer → MUX:**
The LSTer output is Z1=Bout (might be 0 or 1), Z2=Z3=Z4=0. When wiring the LSTer result into the MUX bank, the MUX for output bits 2, 3, and 4 receive a hardwired 0 from the LSTer. This is correct and expected.

**Design document:**
Students who haven't started the document should at minimum get the introduction and one component section drafted. The test case screenshots need to come from the final working ALU, so those can be added last.

### Differentiation

- **Ahead:** Run all test cases, take screenshots for the document, finish and polish the design document. Point to `alu-extension.md`.
- **Behind:** Focus on getting ADD operation through the MUX working — that's the clearest demonstration of the ALU functioning. Document what's working and be honest about what isn't.

---

## Period 16 — Demo Day + Submission

**Format:** Students demo their ALUs, then submit.

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Final submission instructions |
| 5–45 | Demo show-and-tell |
| 45–60 | Buffer: overflow demos, unit preview, or free build |

### Demo Structure

Each student demos to you (or to a peer pair — your call). 3–5 minutes per demo:

1. Show the 4-bit adder: set A and B, verify sum (use the ADD test case from the assignment)
2. Show the subtractor: verify difference
3. Show AND: enter two bit patterns, verify bitwise result
4. Show LST: one case where A < B (expect 0001), one where A ≥ B (expect 0000)
5. Optional: trigger the overflow edge case — what does their circuit do?

For peer demos: pair a strong student with one who is less confident. The strong student demos first; the less confident one asks one question about how it works.

### Submission

- Share the CircuitVerse project link (Save Online → copy URL)
- Share the Google Doc design document link (set to "anyone with link can view")
- Submit both via Google Classroom

### Buffer (45–60 min if time permits)

Options depending on class energy:
- Discuss the carry-lookahead adder as a teaser: "real CPUs don't use ripple carry because the delay grows with bit width — here's the idea of computing all carries simultaneously"
- Preview unit 4 or course wrap-up
- Free build in CircuitVerse (extend their ALU, add a display, experiment)
