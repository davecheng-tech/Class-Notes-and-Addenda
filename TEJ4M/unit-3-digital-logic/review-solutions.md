# Unit 3: Digital Logic — Test Review (Answer Key)

---

## Section 1: Knowledge

**K1.**

a) **False.** XOR outputs 1 when inputs are *different*. (XNOR outputs 1 when they are the same.)

b) **True.** Both NAND and NOR are universal gates — any logic circuit can be built from either type alone.

c) **True.** This is the defining structure of a ripple carry adder — carries propagate bit by bit from LSB to MSB.

d) **True.** Moore's Law (1965) observed that transistor density doubles roughly every two years.

---

**K2.**

| Expression | Law Name |
|---|---|
| `A · A' = 0` | **Complement** |
| `A + AB = A` | **Absorption** |
| `(A · B)' = A' + B'` | **De Morgan's** |
| `A + A = A` | **Idempotent** |

---

**K3.**

a) Control `10` selects AND.

| Control | Operation |
|---------|-----------|
| 00 | ADD |
| 01 | SUB |
| 10 | AND |
| 11 | LST |

b) **Overflow.** (Specifically, the carry out of the most significant full adder.)

c) A half adder cannot accept a **carry in** from a previous bit position. It can only add two bits; it has no third input.

---

## Section 2: Communication

**C1.**

a) Working left to right:
- D = A' (NOT gate)
- E = D · B = A' · B (AND gate)
- Z = E + C = **A'·B + C**

b) Accept any reasonable scenario. Example:
- A = security system is active, B = motion detected, C = emergency button pressed
- *"The alarm sounds when motion is detected and the security system is not active, or when the emergency button is pressed."*

*Gate count: 1 NOT + 1 AND + 1 OR = 3 gates.*

---

**C2.**

Z = C · (A ⊕ B)

The engine starts when the key is turned AND exactly one of Park or Neutral is selected — but not both and not neither. Both gear positions being selected at once, or neither being selected, will prevent the engine from starting even if the key is turned.

---

**C3.**

a) Equation:

- "doorbell AND homeowner NOT home" → A · B'
- "intruder sensor triggered" → C
- "OR" connecting the two conditions

```
Z = A·B' + C
```

b) Truth table:

| A | B | C | A·B' | Z = A·B' + C |
|---|---|---|------|--------------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 |

*Note for the teacher: the intermediate column A·B' is good practice to include; accept answers that show correct Z values even if the intermediate column is not labelled.*

---

**C4.**

Looking at the rows where Z = 1: they are (A=0, B=1, C=1), (A=1, B=0, C=1), and (A=1, B=1, C=1). In every case, C = 1. And in every case where C = 1 and Z = 1, at least one of A or B is also 1.

**Expected answer:** The alarm goes off when the system is armed (C = 1) and at least one sensor — either the door sensor or the motion sensor — has been triggered.

*(The equation is Z = C · (A + B), but students are not required to derive it here.)*

---

## Section 3: Thinking

**T1.**

a) Rows where Z = 1: `011`, `101`, `110`, `111`

SOP equation:
```
Z = A'·B·C + A·B'·C + A·B·C' + A·B·C
```

Gate count (unsimplified):
- 3 NOT gates (A', B', C' — one per minterm that needs it)
- 4 three-input AND gates
- 1 four-input OR gate
- **Total: 8 gates**

b) Simplification:

Group the first two terms and last two terms — **Associative** (regrouping within a sum doesn't change the result):

```
Z = (A'·B·C + A·B'·C) + (A·B·C' + A·B·C)
```

Factor C from the first group, A·B from the second — **Distributive** (reverse):

```
Z = C·(A'·B + A·B') + A·B·(C' + C)
```

C' + C = 1 — **Complement**:

```
Z = C·(A'·B + A·B') + A·B·1
```

A·B·1 = A·B — **Identity**:

```
Z = C·(A'·B + A·B') + A·B
```

Recognize XOR — **XOR identity** (A'·B + A·B' = A ⊕ B):

```
Z = C·(A ⊕ B) + A·B
```

c) Gate count (simplified):
- 1 XOR gate (A ⊕ B)
- 1 AND gate (C with XOR result)
- 1 AND gate (A·B)
- 1 OR gate
- **Total: 4 gates** (saving 4 gates)

*Note: Z = AB + C(A⊕B) is the majority circuit — it outputs 1 whenever at least two of the three inputs are 1.*

---

**T2.**

```
Z = A·B'·C + A'·B·C + A·B·C
```

Gate count before: 2 NOT + 3 three-input AND + 1 OR = **6 gates**

**Step 1:** Factor C from all three terms (**Distributive**, reverse):
```
Z = C · (A·B' + A'·B + A·B)
```

**Step 2:** In the bracket, factor A from the first and third terms (**Distributive**, reverse):
```
Z = C · (A·(B' + B) + A'·B)
```

**Step 3:** Apply **Complement** law, B' + B = 1:
```
Z = C · (A·1 + A'·B)
```

**Step 4:** Apply **Identity** law, A·1 = A:
```
Z = C · (A + A'·B)
```

**Step 5:** Apply **Distributive** (OR over AND) to expand A + A'·B:
```
A + A'·B = (A + A')(A + B)
```

Apply **Complement** law, A + A' = 1:
```
= 1 · (A + B) = A + B
```

**Step 6:** Substitute back, apply **Identity**:
```
Z = C · (A + B)
```

Gate count after: 1 OR (A+B) + 1 AND (with C) = **2 gates** (saving 4 gates)

---

**T3.**

```
Z = (A + B') · C
```

Work out each sub-expression column left to right:

| A | B | C | B' | A + B' | Z = (A + B')·C |
|---|---|---|----|--------|----------------|
| 0 | 0 | 0 | 1  | 1      | 0 |
| 0 | 0 | 1 | 1  | 1      | 1 |
| 0 | 1 | 0 | 0  | 0      | 0 |
| 0 | 1 | 1 | 0  | 0      | 0 |
| 1 | 0 | 0 | 1  | 1      | 0 |
| 1 | 0 | 1 | 1  | 1      | 1 |
| 1 | 1 | 0 | 0  | 1      | 0 |
| 1 | 1 | 1 | 0  | 1      | 1 |

Z = 1 for input combinations: `001`, `101`, `111`.

*Note: Z = 1 whenever C = 1 AND (A = 1 OR B = 0). The double-negative on B is a common point of error — students must remember that B' = 1 when B = 0.*

---

## Section 4: Application

**A1.**

Inputs: A = 1, B = 1.

a) Z (Sum) = **0**

b) Y (Carry Out) = **1**

c) Sum uses **XOR**: `Z = A ⊕ B`. Carry uses **AND**: `Y = A · B`.
(1 ⊕ 1 = 0; 1 · 1 = 1)

---

**A2.**

Inputs: A = 1, B = 1, Cin = 1.

a) Using the equations:

```
Z = A ⊕ B ⊕ Cin
  = 1 ⊕ 1 ⊕ 1
  = 0 ⊕ 1        (1 ⊕ 1 = 0 first)
  = 1

Cout = AB + ACin + BCin
     = (1·1) + (1·1) + (1·1)
     = 1 + 1 + 1
     = 1
```

**Z = 1, Cout = 1**

b) Binary check: 1 + 1 + 1 = 11₂ (sum = 1, carry = 1). ✓

---

**A3.**

```
  Carries:  1 1 1
    1 0 1 1    (11)
  + 0 1 1 0    ( 6)
  ─────────
    0 0 0 1   + carry out = 1
```

Column by column (right to left):
- Col 0: 1 + 0 = 1, carry 0
- Col 1: 1 + 1 = 0, carry 1
- Col 2: 0 + 1 + carry(1) = 0, carry 1
- Col 3: 1 + 0 + carry(1) = 0, carry 1

a) 4-bit result: **`0001`**

b) **Yes, there is overflow.** The carry out of the most significant (leftmost) adder is 1, signalling that the result exceeds 4 bits.

c) 1011₂ = 11, 0110₂ = 6. 11 + 6 = **17**. Four bits can only hold 0–15, so 17 overflows. The 4-bit result `0001` = 1, which is 17 − 16 = 1 — consistent with overflow behaviour.

---

**A4.**

a) Control `11` selects the **LST (Less Than)** operation.

b) A = `0101` = 5. B = `1001` = 9.

c) Since 5 < 9, the LST unit outputs **`0001`** (decimal 1).

d) The LST unit runs a 4-bit subtraction (A − B) internally. When the final full subtractor's borrow out is 1 (meaning A was smaller than B and had to borrow), the output is `0001`. The borrow-out bit feeds into the least significant output bit (Z1 = Bout); the other three output bits (Z2, Z3, Z4) are fixed at 0.

---

**A5.**

a) Z = A·C' + B·C with A = 1, B = 0, C = 1:

```
Z = 1·(1)' + 0·1
  = 1·0 + 0·1
  = 0 + 0
  = 0
```

**Z = 0**

b) When C = 0: Z = A·1 + B·0 = A. The output follows input A — A is selected.
When C = 1: Z = A·0 + B·1 = B. The output follows input B — B is selected.

c) In the ALU, the MUX's control input (C in the 2-in-1 form, or a 2-bit signal in the 4-in-1 form) is the **ALU control signal**. It selects which operation's result — ADD, SUB, AND, or LST — is routed to the final output Z.

---

## Diagram Note (for teacher)

**C1** requires a circuit diagram to be provided to students. The circuit is:

```
A ──[NOT]──┐
           ├──[AND]────────────[OR]── Z
B ─────────┘                │
                            │
C ───────────────────────── ┘
```

This gives `Z = A'·B + C`. Draw this in CircuitVerse and export as PNG to include with the printed/digital handout.

---
