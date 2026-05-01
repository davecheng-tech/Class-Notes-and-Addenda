# Guided Build: 1-Bit ALU in CircuitVerse

This sheet walks you through building a complete 1-bit, 4-operation ALU step by step, one component at a time. Each part has a truth table to fill in, equations to derive, and a CircuitVerse build to complete.

**Start a new CircuitVerse project for this activity.** This is your class learning project, separate from the assignment. Keep it. You'll use it as a reference when you build the 4-bit version.

---

## Part 1 — Half Adder

**CircuitVerse tab:** `Half Adder`

A half adder adds two single bits and produces a sum and a carry out.

### Truth Table

Fill in the output columns.

| A | B | Z (Sum) | Y (Carry Out) |
|---|---|---------|---------------|
| 0 | 0 | | |
| 0 | 1 | | |
| 1 | 0 | | |
| 1 | 1 | | |

### Equations

What pattern does Z follow? _______________

What pattern does Y follow? _______________

Z = _______________

Y = _______________

### Build

1. Create Tab 1. Double-click the tab name and rename it **Half Adder**.
2. Add two inputs labeled `A` and `B`.
3. Add two outputs labeled `Z` and `Y`.
4. Wire the gates that match your equations.

### Before Moving On

- [ ] All 4 input combinations tested and match your truth table
- [ ] Inputs labeled `A` and `B`; outputs labeled `Z` and `Y`
- [ ] Tab named **Half Adder**

---

## Part 2 — Full Adder

**CircuitVerse tab:** `Full Adder (1-bit)`

A full adder adds three bits: A, B, and a carry in (Cin) from a previous column.

### Truth Table

Fill in the output columns.

| A | B | Cin | Z (Sum) | Cout |
|---|---|-----|---------|------|
| 0 | 0 | 0 | | |
| 0 | 0 | 1 | | |
| 0 | 1 | 0 | | |
| 0 | 1 | 1 | | |
| 1 | 0 | 0 | | |
| 1 | 0 | 1 | | |
| 1 | 1 | 0 | | |
| 1 | 1 | 1 | | |

### Equations

Z = _______________

Cout = _______________

### Construction from Two Half Adders

You don't need to build this from scratch — you can chain two half adders:

```
Half Adder 1:  inputs A, B         → partial sum S1, partial carry C1
Half Adder 2:  inputs S1, Cin      → final sum Z, partial carry C2
Final carry:   Cout = C1 + C2      (one OR gate)
```

### Build

1. Create Tab 2. Rename it **Full Adder (1-bit)**.
2. Add inputs `A`, `B`, `Cin`. Add outputs `Z` and `Cout`.
3. Wire the two half adder structures and the OR gate for Cout.
4. Wire Cin to a constant 0 input for initial testing.

### Before Moving On

- [ ] All 8 input combinations tested and correct
- [ ] All inputs and outputs labeled
- [ ] Tab named **Full Adder (1-bit)**

---

## Part 3 — Full Subtractor

**CircuitVerse tab:** `Full Subtractor (1-bit)`

A full subtractor subtracts B and a borrow in (Bin) from A.

*Hint: Bout = 1 when A has to borrow, i.e., when A is too small to subtract.*

### Truth Table

Fill in the entire table.

| A | B | Bin | Z (Difference) | Bout |
|---|---|-----|----------------|------|
| 0 | 0 | 0 | | |
| 0 | 0 | 1 | | |
| 0 | 1 | 0 | | |
| 0 | 1 | 1 | | |
| 1 | 0 | 0 | | |
| 1 | 0 | 1 | | |
| 1 | 1 | 0 | | |
| 1 | 1 | 1 | | |

### Equations

Derive from the truth table using SOP, then simplify.

Z = _______________

Bout = _______________

*Notice anything about Z compared to the full adder's Z?*

### Build

1. Create Tab 3. Rename it **Full Subtractor (1-bit)**.
2. Add inputs `A`, `B`, `Bin`. Add outputs `Z` and `Bout`.
3. Build from your equations.

### Before Moving On

- [ ] All 8 input combinations tested and correct
- [ ] All inputs and outputs labeled
- [ ] Tab named **Full Subtractor (1-bit)**

---

## Part 4 — 2-in-1 MUX + 1-bit 2-op Mini-ALU

### 4a. 2-in-1 Multiplexer (MUX)

**CircuitVerse tab:** `MUX (2-in-1, 1-bit)`

A multiplexer selects one of its data inputs and passes it to the output based on a control signal. When C = 0, output follows A. When C = 1, output follows B.

### Truth Table

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | |
| 0 | 0 | 1 | |
| 0 | 1 | 0 | |
| 0 | 1 | 1 | |
| 1 | 0 | 0 | |
| 1 | 0 | 1 | |
| 1 | 1 | 0 | |
| 1 | 1 | 1 | |

### Equation

Z = _______________

### Build

1. Create Tab 4. Rename it **MUX (2-in-1, 1-bit)**.
2. Add inputs: `A` (data 0), `B` (data 1), `C` (control). Add output `Z`.
3. Circuit: AND gate for A·C', AND gate for B·C, OR gate combining both.

### Before Moving On

- [ ] When C=0, Z always matches A regardless of B
- [ ] When C=1, Z always matches B regardless of A
- [ ] Tab named **MUX (2-in-1, 1-bit)**

---

### 4b. 1-bit 2-op Mini-ALU (ADD / SUB)

**CircuitVerse tab:** `Mini-ALU (1-bit, 2-op)`

Wire the full adder, full subtractor, and MUX together into a circuit that adds or subtracts based on a control bit.

### Wiring Diagram

```
      A ──┬──▶ Full Adder ──▶ sum Z ──────────▶ MUX input A (data 0)
          │
      B ──┤
          │
          └──▶ Full Subtractor ──▶ diff Z ──▶ MUX input B (data 1)

Cin = 0 ──▶ Full Adder
Bin = 0 ──▶ Full Subtractor
Control ──▶ MUX control (C)
MUX output ──▶ ALU output Z
```

Both the adder and subtractor are always computing. The MUX chooses which result reaches the output.

### Build

1. Create Tab 5. Rename it **Mini-ALU (1-bit, 2-op)**.
2. Add inputs `A`, `B`, `Control`. Add output `Z`.
3. Wire A and B to both the full adder and full subtractor.
4. Hardwire Cin=0 and Bin=0.
5. Connect the adder Z → MUX input A, subtractor Z → MUX input B, Control → MUX control.

### Test Cases

Fill in Your ALU Z and verify:

| A | B | Control | Operation | Expected Z | Your ALU Z | Correct? |
|---|---|---------|-----------|------------|------------|----------|
| 1 | 0 | 0 | ADD | 1 | | |
| 1 | 0 | 1 | SUB | 1 | | |
| 1 | 1 | 0 | ADD | 0 (carry=1) | | |
| 1 | 1 | 1 | SUB | 0 | | |
| 0 | 1 | 1 | SUB | 1 (borrow) | | |

### Before Moving On

- [ ] All test cases verified
- [ ] Flipping the control bit changes which operation is active

---

## Part 5 — ANDer + LST (Less Than)

### 5a. ANDer

**CircuitVerse tab:** `ANDer (1-bit)`

Bitwise AND for one bit: `Z = A · B`

Build independently: one AND gate, inputs `A` and `B`, output `Z`. Verify all 4 combinations.

- [ ] Done

---

### 5b. LST (Less Than)

**CircuitVerse tab:** `LST (1-bit)`

Goal: Z = 1 if A < B, else Z = 0.

Before building, work through these questions:

**1.** Which component you've already built computes A − B?

> _______________

**2.** When A = 0 and B = 1, does the subtractor have to borrow? What is Bout?

> _______________

**3.** When A = 1 and B = 0, does the subtractor have to borrow? What is Bout?

> _______________

**4.** What does Bout = 1 tell you about the relationship between A and B?

> _______________

**5.** So how do you build a Less Than circuit using the subtractor?

> Z = _______________

### Build

1. Create a tab. Rename it **LST (1-bit)**.
2. Add inputs `A` and `B`. Add output `Z`.
3. Wire a full subtractor with Bin = 0. Connect the correct output to Z.

### Verification

| A | B | Expected Z | Correct? |
|---|---|------------|----------|
| 0 | 1 | 1 (0 < 1 → true) | |
| 1 | 0 | 0 (1 < 0 → false) | |
| 1 | 1 | 0 (1 < 1 → false) | |
| 0 | 0 | 0 (0 < 0 → false) | |

- [ ] All 4 verification cases correct

---

## Part 6 — 4-in-1 MUX + Complete 1-bit ALU

### 6a. 4-in-1 MUX Structure

A 4-in-1 MUX selects among four inputs using a 2-bit control (C1, C0). Build it from three 2-in-1 MUXes:

```
MUX 1: inputs ADD result, SUB result  → control C0 → output Out1
        C0=0 → ADD,  C0=1 → SUB

MUX 2: inputs AND result, LST result  → control C0 → output Out2
        C0=0 → AND,  C0=1 → LST

MUX 3: inputs Out1, Out2              → control C1 → final output Z
        C1=0 → from MUX 1,  C1=1 → from MUX 2
```

Control table:

| C1 | C0 | Operation selected |
|----|----|--------------------|
| 0 | 0 | ADD |
| 0 | 1 | SUB |
| 1 | 0 | AND |
| 1 | 1 | LST |

> **Challenge:** You derived the 2-in-1 MUX equation as `Z = A·C' + B·C` — each data input is gated by the control minterm that selects it. Can you extend that pattern to write the equation for a 4-in-1 MUX with inputs A, B, C, D and 2-bit control C1, C0?
>
> If you can write it, try to build a single MUX tab from basic gates (AND, OR, NOT) and use it in place of the three-MUX cascade. Verify it against the control table.

---

### 6b. Complete 1-bit 4-op ALU

Update your Mini-ALU tab (or build on a new tab) to connect all four operations through the 4-in-1 MUX.

### Final Verification

Test all four operations:

| A | B | C1 | C0 | Operation | Expected Z | Correct? |
|---|---|----|----|-----------|------------|----------|
| 1 | 0 | 0 | 0 | ADD | 1 | |
| 1 | 0 | 0 | 1 | SUB | 1 | |
| 1 | 1 | 1 | 0 | AND | 1 | |
| 0 | 1 | 1 | 1 | LST (0 < 1) | 1 | |
| 1 | 0 | 1 | 1 | LST (1 < 0?) | 0 | |

- [ ] All four operations verified with at least one test case each
- [ ] Changing C1 and C0 selects the correct operation

---

## Component Reference

Use this during the assignment. All equations are for single-bit versions; the 4-bit versions chain four 1-bit units with ripple carry/borrow.

| Component | Key equation(s) |
|-----------|-----------------|
| Half Adder | Z = A ⊕ B, &nbsp; Y = A·B |
| Full Adder | Z = A ⊕ B ⊕ Cin, &nbsp; Cout = AB + ACin + BCin |
| Full Subtractor | Z = A ⊕ B ⊕ Bin, &nbsp; Bout = A'B + A'Bin + BBin |
| MUX (2-in-1) | Z = A·C' + B·C |
| ANDer | Z = A·B |
| LST | Z = Bout of full subtractor (Bin = 0) |
| 4-in-1 MUX | Three 2-in-1 MUXes: MUX1(ADD,SUB,C0) → MUX3; MUX2(AND,LST,C0) → MUX3; MUX3 controlled by C1 |
