# Practice: Logic Conversions

Use these problems to practice converting between truth tables, equations, and circuit diagrams. Build and verify your circuits in CircuitVerse.

For each circuit you build, toggle all input combinations and confirm the output matches the expected truth table.

---

## Part A — Truth Table → Circuit and Equation

For each truth table below: (1) derive the Boolean equation using the SOP method, and (2) build the circuit in CircuitVerse and verify it.

### A1. Car Starter (Manual Transmission)

A manual transmission car starts when the key is turned and the clutch pedal is pressed. The car can start in any gear as long as the clutch is engaged.

| A (Key) | B (Neutral) | C (Clutch) | Z (Starts) |
|---------|-------------|------------|------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

---

### A2. LCD Projector

A projector displays an image when a valid signal is connected (VGA or HDMI) and the lamp temperature is acceptable. When both VGA and HDMI are connected, it defaults to HDMI.

| A (VGA) | B (HDMI) | C (Good Temp) | Z (Projecting) |
|---------|----------|---------------|----------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

---

### A3. Unknown Circuit 1

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |


---

### A4. Unknown Circuit 2

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

---

### A5. Practice Test Circuit

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

---

## Part B — Equation → Circuit

For each equation, build the circuit in CircuitVerse. Then fill in the complete truth table.

### B1.
```
Z = (A + B)' + C
```

### B2.
```
Z = A · ((C + B) ⊕ A')
```

### B3.
```
Z = (A + B + C)' ⊕ D'
```

### B4.
```
Z = (A · B') + (B · C)
```

---

## Part C — Circuit → Equation

For each circuit described below, write the Boolean equation. Label intermediate gates with variables (D, E, F...) as you work.

### C1.

Inputs: A, B, C

1. A NOT gate on input A → output D
2. An AND gate with inputs D and B → output E
3. An OR gate with inputs E and C → output Z

Write the equation for Z in terms of A, B, C only (substitute D and E out).

---

### C2.

Inputs: A, B, C

1. A NOT gate on input C → output D
2. An AND gate with inputs A and B → output E
3. An AND gate with inputs B and D → output F
4. An OR gate with inputs E and F → output Z

Write the equation for Z in terms of A, B, C only.

---

### C3.

Inputs: A, B

1. An AND gate with inputs A and B → output D
2. A NOT gate on D → output E
3. A NOR gate with inputs A and B → output F
4. A NOT gate on F → output G
5. An AND gate with inputs E and G → output Z

Write the equation for Z, then simplify it using Boolean laws. How many gates are needed before and after simplification?

---

## Part D — Circuit → Truth Table

For each circuit described below, fill in the complete truth table. Add intermediate columns to show your work.

### D1.

```
Z = A'B + AB'
```

Build the truth table with intermediate columns for A', B', A'B, and AB'.

| A | B | A' | B' | A'B | AB' | Z |
|---|---|----|----|-----|-----|---|
| 0 | 0 | | | | | |
| 0 | 1 | | | | | |
| 1 | 0 | | | | | |
| 1 | 1 | | | | | |

What well-known gate does this equation describe?

---

### D2.

```
Z = (A · B) + (B · C) + (A · C)
```

Build the truth table with intermediate columns.

| A | B | C | AB | BC | AC | Z |
|---|---|---|----|----|----|---|
| 0 | 0 | 0 | | | | |
| 0 | 0 | 1 | | | | |
| 0 | 1 | 0 | | | | |
| 0 | 1 | 1 | | | | |
| 1 | 0 | 0 | | | | |
| 1 | 0 | 1 | | | | |
| 1 | 1 | 0 | | | | |
| 1 | 1 | 1 | | | | |

This circuit is called a **majority gate**: Z = 1 when the majority of inputs are 1. Confirm that the truth table matches that description.