# Practice: More Boolean Algebra Simplification

A second set of simplification problems. Work through in order — the problems increase in difficulty. For every simplification, name the law you apply at each step. Count the gates before and after.

Verify your simplified circuits in CircuitVerse by confirming both the original and simplified forms produce identical truth tables.

---

## Part C — Simplification Practice

Simplify each expression. Name every law at every step. Count the gates before and after.

### C1.

```
Z = A·B·C + A·B·C'
```

*Hint: Your simplified answer should use 1 gate.*

---

### C2.

```
Z = A'·B + A·B + A·C
```

*Hint: Your simplified answer should use 2 gates.*

---

### C3.

```
Z = A·B + A·C + A·B·C + A·B·C'
```

*Hint: Your simplified answer should use 2 gates.*

---

### C4.

```
Z = (A + B)' + A·B'
```

*Hint: Your simplified answer should use 1 gate.*

---

### C5.

```
Z = A'·B·C' + A'·B·C + A·B'·C' + A·B'·C
```

*Hint: Your simplified answer should use 1 gate — but it may not be the gate type you expect.*

---

## Part D — Truth Table → Circuit → Simplify → Verify

For each problem:

1. Write the SOP equation from the truth table — one product term (minterm) for every row where Z = 1
2. Build the original SOP circuit in CircuitVerse and record its truth table
3. Simplify the equation algebraically — name every law at every step
4. Build the simplified circuit in CircuitVerse
5. Confirm both circuits produce identical truth tables
6. State the gate count before and after, and how many gates you saved

### D1.

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

---

### D2.

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

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
| Distributive | `A(B+C) = AB + AC`, `A + BC = (A+B)(A+C)` |
| Absorption | `A + AB = A`, `A(A+B) = A` |
| De Morgan's | `(AB)' = A' + B'`, `(A+B)' = A'B'` |
| XOR Identity | `A'B + AB' = A ⊕ B` |
