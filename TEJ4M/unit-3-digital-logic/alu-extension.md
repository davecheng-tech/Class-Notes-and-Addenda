# ALU Extension Challenges

These are optional extensions for students who complete the 4-bit ALU assignment and want to go further. Each challenge builds directly on what you've built — no new concepts are introduced from outside the unit.

Choose any one, or attempt more than one if you have time.

---

## Extension A — Add a Fifth Operation: Bitwise OR

Your ALU currently supports four operations selected by a 2-bit control. Extend it to support a fifth: **bitwise OR** (A OR B, applied independently to each bit pair).

### What to Build

1. **OR unit (4-bit):** Four independent OR gates, one per bit position. Inputs A1–A4 and B1–B4, outputs Z1–Z4. Add this as a new tab.

2. **Expanded MUX:** You now have five results and need to select among them. The simplest approach:
   - Add a third control bit C2
   - When C2 = 0: use the existing 4-op ALU output (selected by C1 and C0 as before)
   - When C2 = 1: output the OR result
   - This means adding one more 2-in-1 MUX per output bit, at the final stage of the MUX chain

3. **Updated ALU tab:** Wire everything together. Your control is now 3 bits: C2 C1 C0.

| C2 | C1 | C0 | Operation |
|----|----|-----|-----------|
| 0 | 0 | 0 | ADD |
| 0 | 0 | 1 | SUB |
| 0 | 1 | 0 | AND |
| 0 | 1 | 1 | LST |
| 1 | — | — | OR |

### Verification

Test: A = 1010, B = 0110, C2C1C0 = 100. Expected output: 1110.

---

## Extension B — Overflow and Underflow Indicators

The 4-bit ALU can produce results that don't fit in 4 bits:
- **ADD overflow:** A + B > 15. The carry out of the MSB adder goes high.
- **SUB underflow:** A − B < 0. The borrow out of the MSB subtractor goes high.

Currently, those signals exist inside your circuit but aren't exposed. Add two visible indicator outputs.

### What to Build

1. **Identify the signals:**
   - ADD overflow = Cout of the 4th (MSB) full adder in Tab 2
   - SUB underflow = Bout of the 4th (MSB) full subtractor in Tab 4
   - Make sure these outputs are labelled and accessible (add named output pins to those tabs if needed)

2. **Context-aware indicator:** In the ALU tab, add two output pins: `Overflow` and `Underflow`. Wire them so that:
   - Overflow shows the adder's Cout, but only matters when the ADD operation is selected (C1C0=00)
   - Underflow shows the subtractor's Bout, but only matters when SUB is selected (C1C0=01)

   You could implement this as: `Overflow = Cout_add · C1' · C0'` and `Underflow = Bout_sub · C1' · C0`.

3. **Trigger the edge cases** from `alu-assignment.md` (the overflow row with A=1111, B=0001) and confirm your indicators light up correctly.

### Design Question

Write a short answer (2–3 sentences) in your design document: why would a real CPU care about overflow and underflow? What might it do when it detects them?

---

## Extension C — Carry-Lookahead Adder

Your 4-bit adder uses ripple carry: the carry out of bit 1 feeds into bit 2, which feeds into bit 3, and so on. This means bit 4's sum can't be computed until the carry has rippled through all four stages — the circuit has delay proportional to the bit width.

A **carry-lookahead adder** computes all carries simultaneously by pre-calculating whether each stage will generate or propagate a carry.

### Background

For each bit position i, define:
- **Generate:** `G_i = A_i · B_i` — this stage produces a carry regardless of carry in
- **Propagate:** `P_i = A_i ⊕ B_i` — this stage passes a carry in to carry out

Using G and P, the carries at each bit can be expressed without waiting for the previous carry:

```
C1 = G0 + P0·C0
C2 = G1 + P1·G0 + P1·P0·C0
C3 = G2 + P2·G1 + P2·P1·G0 + P2·P1·P0·C0
C4 = G3 + P3·G2 + P3·P2·G1 + P3·P2·P1·G0 + P3·P2·P1·P0·C0
```

C0 is the initial carry in (0 for a standard adder). All four carries can now be computed in parallel from A, B, and C0 — no rippling.

### What to Build

1. **Research:** Confirm you understand why the equations above are correct. Write a 1-paragraph explanation in your design document.

2. **Build the carry-lookahead adder in CircuitVerse** as a new tab. For each bit:
   - Compute G_i and P_i from A_i and B_i
   - Compute C1, C2, C3, C4 using the equations above (one circuit per carry, all sharing A, B, C0)
   - Compute each sum: `Z_i = P_i ⊕ C_{i-1}`

3. **Verify** that your carry-lookahead adder produces the same results as your ripple carry adder on the ADD test cases.

4. **Compare:** Your carry-lookahead adder uses more gates than the ripple carry adder. Count the approximate gate total for each. In your design document, explain the tradeoff: more gates vs. less delay. Why does this matter for a real CPU?

### Note

This is a genuine circuit design challenge. The equations above are complete — the work is in translating them into gates and wiring them correctly in CircuitVerse. Budget at least one full work period.
