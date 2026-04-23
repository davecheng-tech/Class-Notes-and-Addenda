# Homework: Combinational Logic Conversions

Complete the following problems independently. For Sections 1 and 2, derive the Boolean equation using the SOP method, then build and test the circuit in CircuitVerse. For Sections 3 and 4, build circuits or write equations as directed.

Screenshot or export your CircuitVerse circuits with input labels, output labels, and all inputs toggled to a row where Z = 1 (as proof of testing).

---

## Section 1 — Truth Table → Circuit

For each truth table: derive the SOP equation, then build and verify the circuit in CircuitVerse.

### 1. Security System

A security alarm triggers when motion is detected at night, OR when a door is opened while the system is armed.

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

### 2. Greenhouse Watering System

A greenhouse irrigation valve opens when the soil is dry **and** it is daytime **and** it is not currently raining. The valve also opens when the emergency override is triggered (soil is critically dry), again only if it is not raining. Rain always prevents watering regardless of other conditions.

| A (Soil Dry) | B (Daytime) | C (Raining) | D (Emergency Override) | Z (Water On) |
|--------------|-------------|-------------|------------------------|--------------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |

---

### 3. Smart Thermostat

A smart thermostat turns on the heat when the temperature is below the setpoint **and** at least one of the following is true: someone is home, or the scheduled heating time is active.

| A (Temp Below Setpoint) | B (Occupied) | C (Schedule Active) | Z (Heat On) |
|-------------------------|--------------|---------------------|-------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

---

## Section 2 — Unknown Circuits

For each truth table: derive the SOP equation, then build and verify the circuit in CircuitVerse. Some of these are equivalent to a single well-known gate. If you recognize one, name it.

### 4. Unknown Circuit A

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

### 5. Unknown Circuit B

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

Once you have your equation, name the gate this is equivalent to.

---

### 6. Unknown Circuit C

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

### 7. Unknown Circuit D

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

Once you have your equation, name the gate this is equivalent to.

---

## Section 3 — Equation → Circuit

For each equation, build the circuit in CircuitVerse and produce its complete truth table.

### 8.
```
Z = A · ((C + B) ⊕ A')
```

### 9.
```
Z = (A + B + C)' ⊕ D'
```

### 10.
```
Z = (A' · B) + (A · B') + C
```

---

## Section 4 — Circuit → Equation

For each circuit described below, write the Boolean equation for Z. Label intermediate signals with variables (D, E, F…) as you work, then substitute them out so your final answer is in terms of the original inputs only.

### 11.

Inputs: A, B, C

1. A NAND gate with inputs A and B → output D
2. An AND gate with inputs D and C → output Z

Write the equation for Z in terms of A, B, C only.

---

### 12.

Inputs: A, B, C, D

1. A NOT gate on input A → output E
2. An OR gate with inputs E and B → output F
3. An AND gate with inputs C and D → output G
4. An AND gate with inputs F and G → output Z

Write the equation for Z in terms of A, B, C, D only.

---

## Section 5 — Equation → Truth Table

For each equation, fill in the complete truth table. Add intermediate columns to show each step of your work.

### 13.

```
Z = A · B' + C
```

| A | B | C | B' | A · B' | Z |
|---|---|---|----|--------|---|
| 0 | 0 | 0 | | | |
| 0 | 0 | 1 | | | |
| 0 | 1 | 0 | | | |
| 0 | 1 | 1 | | | |
| 1 | 0 | 0 | | | |
| 1 | 0 | 1 | | | |
| 1 | 1 | 0 | | | |
| 1 | 1 | 1 | | | |

---

### 14.

```
Z = (A + B') · (B + C)
```

| A | B | C | B' | A + B' | B + C | Z |
|---|---|---|----|--------|-------|---|
| 0 | 0 | 0 | | | | |
| 0 | 0 | 1 | | | | |
| 0 | 1 | 0 | | | | |
| 0 | 1 | 1 | | | | |
| 1 | 0 | 0 | | | | |
| 1 | 0 | 1 | | | | |
| 1 | 1 | 0 | | | | |
| 1 | 1 | 1 | | | | |

---

## Section 6 — In Plain English

Answer each question in 2–3 sentences. No equations, no logic symbols, no technical terms. Write as you would speak to the person who owns the system, not to a computer science or technology class.

### 15. Automatic Car Door Lock

You've just installed an automatic door-locking system. Here is the complete truth table for the control circuit. **Z = 1 means the system sends a lock command. Z = 0 means it does nothing** (the current state is kept).

| A (Car Moving) | B (Door Unlocked) | C (Lock Button Pressed) | Z (Lock Command) |
|----------------|-------------------|-------------------------|------------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

**Explain to the car owner:** When will the locks engage on their own, and when won't they? Is there anything about the system's behaviour that might surprise them?

---

### 16. Office Ventilation System

You've just set up an automatic ventilation system for a small office. Here is the complete truth table for the control circuit.

| A (Hot Outside) | B (People in Office) | C (CO₂ Level High) | Z (Fan Runs) |
|-----------------|----------------------|---------------------|--------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

**Explain to the office manager:** When does the ventilation turn on? Make sure you mention any situation that might surprise them, e.g., something that doesn't work the way they might expect.
