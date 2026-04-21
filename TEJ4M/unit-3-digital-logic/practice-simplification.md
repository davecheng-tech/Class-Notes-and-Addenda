# Practice: Boolean Algebra Simplification

Use these problems to practice simplifying Boolean expressions. For each simplification, name the law you apply at every step. Count the number of gates before and after.

Verify your simplified circuits in CircuitVerse by confirming both forms produce identical truth tables.

---

## Part A — Equation → Circuit (Before Simplification)

Build the following circuits in CircuitVerse before attempting to simplify them. This gives you a reference to verify your simplified version against.

### A1.
```
Z = ((A · B) · C) + (A · C)
```

Draw the circuit. How many gates does it use?

---

### A2.
```
Z = NOT(NOT(A + NOT(B)))
```

Written in Boolean notation:
```
Z = ((A + B')')'
```

Draw the circuit. How many gates does it use?

---

### A3.
```
Z = (A + B) · C + (A · C)
```

Draw the circuit. How many gates does it use?

---

## Part B — Simplification Practice

Simplify each expression. Name every law you use. Then count gates before and after.

### B1.
```
Z = A·B' + A·(B' + C) + B·(B' + C)
```

*Hint: start by expanding, then look for absorption.*

---

### B2.
```
Z = [A·B·(C + B·D) + A'·B']·C
```

*Hint: consider what happens when you apply De Morgan's to the A'B' term.*

---

### B3.
```
Z = A'·B·C + A'·B·C' + A·B·C' + A·B'·C' + A·B·C
```

*Hint: count the gates in the SOP form first. Look for factoring opportunities.*

---

## Part C — Equation → Circuit → Simplify → Verify

For each problem:
1. Build the original circuit in CircuitVerse
2. Record its truth table
3. Simplify the equation algebraically (show all steps and name all laws)
4. Build the simplified circuit in CircuitVerse
5. Confirm the truth tables match
6. State how many gates you saved

### C1.

Start with the truth table from practice problem A5 (the one with minterms at rows 001, 110):

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Write the SOP equation, then simplify it as far as you can.

---

### C2.

Start with:
```
Z = A'·B'·C' + A'·B'·C + A·B'·C + A·B·C
```

Simplify this expression. How many gates does the final simplified circuit use?

---

## Reference: Boolean Laws

| Law | Expression |
|-----|-----------|
| Identity | `A + 0 = A`, `A · 1 = A` |
| Null | `A + 1 = 1`, `A · 0 = 0` |
| Idempotent | `A + A = A`, `A · A = A` |
| Complement | `A + A' = 1`, `A · A' = 0` |
| Double Negation | `(A')' = A` |
| Commutative | `A + B = B + A`, `AB = BA` |
| Associative | `(A+B)+C = A+(B+C)` |
| Distributive | `A(B+C) = AB + AC` |
| Absorption | `A + AB = A`, `A(A+B) = A` |
| De Morgan's | `(AB)' = A' + B'`, `(A+B)' = A'B'` |
| XOR Identity | `A'B + AB' = A ⊕ B` |
