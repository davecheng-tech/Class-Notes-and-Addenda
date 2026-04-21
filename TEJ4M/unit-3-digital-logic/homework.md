# Homework: Combinational Logic Conversions

Complete the following problems independently. For each one, derive the Boolean equation using the SOP method, then build and test the circuit in CircuitVerse.

Screenshot or export your CircuitVerse circuits with input labels, output labels, and all inputs toggled to a row where Z = 1 (as proof of testing).

---

## Section 1 — Truth Table → Circuit

For each truth table: derive the SOP equation, then build and verify the circuit in CircuitVerse.

### 1. Security System

A security alarm triggers when motion is detected at night OR when a door is opened while the system is armed.

| A (Motion) | B (Night) | C (Armed) | D (Door Open) | Z (Alarm) |
|------------|-----------|-----------|---------------|-----------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

---

### 2. Unknown Circuit A

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Once you have your equation, name the gate this is equivalent to.

---

### 3. Unknown Circuit B

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Once you have your equation, apply De Morgan's Law and identify the simpler equivalent gate.

---

### 4. Unknown Circuit C

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

---

## Section 2 — Equation → Circuit

For each equation, build the circuit in CircuitVerse and produce its complete truth table.

### 5.
```
Z = A · ((C + B) ⊕ A')
```

### 6.
```
Z = (A + B + C)' ⊕ D'
```

---

## Section 3 — Reflection

Answer both questions in a sentence or two each.

**Question 1:** When filling in input columns of a truth table, how do you ensure you cover every possible combination? Describe the pattern.

**Question 2:** Look at your answers to problems 2 and 3. What is the relationship between the two circuits? How are their equations related?
