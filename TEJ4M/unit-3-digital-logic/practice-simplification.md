# Practice: Boolean Algebra Simplification

Use these problems to practice simplifying Boolean expressions. For each simplification, name the law you apply at every step. Count the number of gates before and after.

Verify your simplified circuits in CircuitVerse by confirming both forms produce identical truth tables.

---

## Part A — Equation → Circuit

Build the following circuits in CircuitVerse. Each expression is given as an equation — translate it directly into a logic circuit, then count how many gates you used. This is circuit-building practice only; no simplification required here.

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

## Part B — Fill in the Steps

Each problem below shows you where the simplification starts and where it ends. Fill in all the steps in between and name the law at each one. Your path may use more or fewer steps than someone else's — that's fine, as long as every step is valid.

### B1.

```
Z = A·B + A·B'

  ⋮

  = A
```

---

### B2.

```
Z = (A·B)' · B

  ⋮

  = A'·B
```

---

### B3.

```
Z = (A + B) · (A + C)

  ⋮

  = A + B·C
```

---

### B4.

```
Z = A·B·C + A·B·C' + A·B'·C

  ⋮

  = A·(B + C)
```

---

## Part C — Simplification Practice

Simplify each expression. Name every law you use. Then count gates before and after.

### C1.
```
Z = A·B' + A·(B' + C) + B·(B' + C)
```

*Hint: expand all three terms using the Distributive Law. You will find a complement pair that cancels to 0 and a duplicate term to eliminate. Your fully simplified answer has three terms. If an online solver shows two terms, it is using the Consensus theorem — a law we have not covered. Three terms is the expected stopping point.*

---

### C2.
```
Z = [A·B·(C + B·D) + A'·B']·C
```

*Hint: start by expanding A·B·(C + B·D) — watch for a repeated variable that Idempotent can clean up. Then distribute the outer ·C across the whole bracket (Idempotent handles C·C). At that point, look for a four-variable product term that can be absorbed into a shorter one. Factor out a common variable last.*

---

### C3.
```
Z = A'·B·C + A'·B·C' + A·B·C' + A·B'·C' + A·B·C
```

*Hint: look for pairs of terms that share two variables and differ only in whether the third is complemented — those pairs collapse to a two-variable product using Distributive, Complement, and Identity. There are two such pairs. After handling them, you will have three terms; factor again.*

---

## Part D — Equation → Circuit → Simplify → Verify

For each problem:
1. Build the original circuit in CircuitVerse
2. Record its truth table
3. Simplify the equation algebraically (show all steps and name all laws)
4. Build the simplified circuit in CircuitVerse
5. Confirm the truth tables match
6. State how many gates you saved

### D1.

Start with this truth table (minterms at rows 011, 101, and 111):

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Write the SOP equation, then simplify it as far as you can. Draw both the original and simplified circuits in CircuitVerse before verifying the truth tables match.

---

### D2.

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
