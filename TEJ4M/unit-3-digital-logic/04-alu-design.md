# ALU Design

Every CPU contains an **Arithmetic Logic Unit (ALU)**: the component responsible for performing integer arithmetic (add, subtract, multiply, divide) and integer logic (comparisons, bitwise operations). The ALU is what makes a processor capable of computation.

Modern CPUs contain ALUs that support dozens of operations on 64-bit values. In this unit, you will design a simplified ALU:

- **4-bit inputs and outputs** (A and B)
- **2-bit control input** (selects one of four operations)
- **4 operations:** ADD, SUB, AND, LST (less than)

This note covers:

- Binary addition and subtraction at the gate level
- The half adder and full adder
- The half subtractor and full subtractor
- Chaining adders and subtractors for multi-bit arithmetic
- The bitwise ANDer
- The Less Than (LST) unit
- The Multiplexer (MUX)
- Connecting the components into a complete ALU

<br>

## 1. The ALU Structure

```
        A (4 bits)      B (4 bits)
             │               │
    ┌────────┴───────────────┴────────┐
    │   ADD unit    SUB unit          │
    │   AND unit    LST unit          │
    └────────────────┬────────────────┘
                     │
                  ┌──┴──┐
     Control ───▶ │ MUX │
    (2 bits)      └──┬──┘
                     │
                  Z (4 bits)
```

All four arithmetic/logic units compute their result simultaneously. The MUX selects which result becomes the output Z, based on the 2-bit control signal:

| Control | Operation |
|---------|-----------|
| 00 | ADD |
| 01 | SUB |
| 10 | AND |
| 11 | LST (less than) |

<br>

## 2. Binary Addition Review

Before building adder circuits, review how binary addition works by hand:

```
  0 + 0 = 0   (no carry)
  0 + 1 = 1   (no carry)
  1 + 0 = 1   (no carry)
  1 + 1 = 10  (sum = 0, carry = 1)
```

When two bits are added, there are two output bits: the **sum** and the **carry out**.

<br>

## 3. Half Adder

A **half adder** adds two single bits. It has two inputs (A, B) and two outputs (Z = sum, Y = carry out).

| A | B | Z (Sum) | Y (Carry Out) |
|---|---|---------|---------------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Reading the truth table:

- **Z (sum):** outputs 1 when inputs differ — this is **XOR**: `Z = A ⊕ B`
- **Y (carry):** outputs 1 only when both inputs are 1 — this is **AND**: `Y = A · B`

The half adder needs just two gates: one XOR and one AND.

> [!NOTE]
> It is called a "half" adder because it is incomplete. It can only add two bits — it cannot accept a carry in from a previous column. For multi-bit addition, every column after the rightmost one needs to handle a possible carry in.

<br>

## 4. Full Adder

A **full adder** adds three bits: A, B, and a carry in (Cin) from the previous column. It outputs a sum (Z) and a carry out (Cout).

| A | B | Cin | Z (Sum) | Cout |
|---|---|-----|---------|------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

The equations derived from this truth table are:

```
Z    = A ⊕ B ⊕ Cin
Cout = AB + ACin + BCin
```

A full adder can be built by connecting two half adders:

```
Half Adder 1: takes A and B
  → produces partial sum S1 = A ⊕ B
  → produces partial carry C1 = A · B

Half Adder 2: takes S1 and Cin
  → produces final sum Z = S1 ⊕ Cin = A ⊕ B ⊕ Cin
  → produces partial carry C2 = S1 · Cin

Final carry: Cout = C1 + C2
```

<br>

## 5. 4-Bit Ripple Carry Adder

To add two 4-bit numbers, chain four full adders together. The carry out of each adder feeds into the carry in of the next.

```
Bit position:    1 (LSB)       2            3            4 (MSB)
                ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
   A1, B1 ──▶   │ Full │     │ Full │     │ Full │     │ Full │
   Cin=0 ────▶  │ Add  │─C─▶ │ Add  │─C─▶ │ Add  │─C─▶ │ Add  │─▶ Overflow
                └──┬───┘     └──┬───┘     └──┬───┘     └──┬───┘
                   Z1           Z2           Z3           Z4
```

Inputs:
- A1, A2, A3, A4 — the four bits of number A (A1 = least significant)
- B1, B2, B3, B4 — the four bits of number B
- Cin of the first adder is always 0

Outputs:
- Z1–Z4: the 4-bit sum
- The carry out of the final adder is the **overflow** bit — it indicates the result exceeds 4 bits

> [!IMPORTANT]
> This design is called a **ripple carry adder** because the carry signal "ripples" from the least significant bit to the most significant bit. It is simple to build but has a delay — the final sum cannot be computed until all the carries have propagated. Real CPUs use carry-lookahead adders to compute all carries simultaneously.

<br>

## 6. Binary Subtraction Review

Binary subtraction works similarly to decimal subtraction, with borrowing:

```
  0 - 0 = 0
  1 - 0 = 1
  1 - 1 = 0
  0 - 1 = 1, borrow 1   (just like decimal: 10 - 1 = 1, borrow from next column)
```

<br>

## 7. Half Subtractor

A **half subtractor** subtracts bit B from bit A. Outputs: Z (difference), Y (borrow out).

| A | B | Z (Difference) | Y (Borrow Out) |
|---|---|----------------|----------------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

```
Z = A ⊕ B
Y = A' · B
```

The difference is XOR (same as the adder). The borrow occurs only when A=0 and B=1 — meaning we needed to borrow because the top bit was smaller.

<br>

## 8. Full Subtractor

A **full subtractor** subtracts B and a borrow in (Bin) from A.

| A | B | Bin | Z (Difference) | Bout (Borrow Out) |
|---|---|-----|----------------|-------------------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 |

```
Z    = A ⊕ B ⊕ Bin
Bout = A'B + A'Bin + BBin
```

Like the full adder, a full subtractor can be built from two half subtractors plus an OR gate for the borrow out.

Four full subtractors chained together (borrow out → borrow in) give a 4-bit subtractor. The first subtractor's borrow in is 0.

> [!NOTE]
> The 4-bit subtractor has the same chain structure as the 4-bit adder — just replace full adders with full subtractors. The borrow out of the final stage is the **underflow** bit.

<br>

## 9. Bitwise ANDer

The **ANDer** performs bitwise AND: each bit of A is AND'd with the corresponding bit of B, independently.

For 1 bit:

| A | B | Z |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

`Z = A · B`

For 4 bits: just do this four times, once per bit position. A1·B1, A2·B2, A3·B3, A4·B4. No connections between bit positions — all four AND gates are independent.

<br>

## 10. Less Than Unit (LST)

The **Less Than** unit outputs 1 if A < B, and 0 otherwise.

For 4-bit numbers:

- If A < B: output = `0001`
- If A ≥ B: output = `0000`

> [!TIP]
> The LST unit is built by modifying the subtractor. When you compute A − B, the borrow out of the most significant bit tells you whether the result was negative (i.e., whether A < B). If Bout of the final full subtractor is 1, then A < B, and the output should be 0001. Otherwise, the output is 0000.
>
> Concretely: Z1 = Bout of the 4-bit subtractor. Z2 = Z3 = Z4 = 0.

<br>

## 11. Multiplexer (MUX)

A **multiplexer** is a selector circuit: it takes multiple input data lines and, based on a control signal, routes exactly one of them to the output. Think of it as a programmable switch.

### 2-in-1-out MUX (1 bit)

Two data inputs (A and B), one control input (C), one output (Z):

- C = 0: output is A
- C = 1: output is B

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

```
Z = A·C' + B·C
```

The circuit: two AND gates (A with C', and B with C), feeding an OR gate.

### 4-in-1-out MUX (1 bit)

The ALU has four operations, so the output MUX needs four data inputs (ADD result, SUB result, AND result, LST result) and a 2-bit control signal (X, Y).

| XY | Selected input |
|----|---------------|
| 00 | ADD result |
| 01 | SUB result |
| 10 | AND result |
| 11 | LST result |

A 4-in-1-out MUX can be built from three 2-in-1-out MUXes:

```
MUX 1: selects between ADD and SUB (controlled by Y)
MUX 2: selects between AND and LST (controlled by Y)
MUX 3: selects between output of MUX 1 and MUX 2 (controlled by X)
```

> [!NOTE]
> This MUX is 1 bit wide. Because the ALU works with 4-bit values, you need one full 4-in-1-out MUX for each bit position. That is four separate 4-in-1-out MUXes (or equivalently, 12 two-input MUXes), all sharing the same control signals.

<br>

## 12. The Complete 4-Bit ALU

The ALU connects all four units to a MUX bank:

```
A (4-bit) ──┬──▶ 4-bit ADD  ──▶ ADD result (4 bits) ──┐
            ├──▶ 4-bit SUB  ──▶ SUB result (4 bits) ──┤
            ├──▶ 4-bit AND  ──▶ AND result (4 bits) ──┼──▶ 4-bit MUX ──▶ Z (4 bits)
            └──▶ 4-bit LST  ──▶ LST result (4 bits) ──┘        ▲
B (4-bit) ──┘                                            Control (2-bit)
```

All four units receive A and B simultaneously and compute their results. The MUX selects which result to pass to Z.

> [!IMPORTANT]
> In CircuitVerse, build each component on a separate circuit tab, then wire them together on the final ALU tab. This keeps the design modular and much easier to debug.

<br>

## 13. Overflow and Edge Cases

| Situation | What happens |
|---|---|
| ADD result > 15 (exceeds 4 bits) | Carry out of the MSB adder = 1 (overflow) |
| SUB result < 0 | Borrow out of the MSB subtractor = 1 (underflow) |
| LST when A == B | Output is 0000 (A is not less than B) |
| AND of two zero inputs | Output is 0000 |

<br>

## 14. Key Terms

| Term | Definition |
|---|---|
| **ALU** | Arithmetic Logic Unit; the part of a CPU that performs integer math and logic |
| **Half adder** | Adds two bits; no carry in |
| **Full adder** | Adds two bits plus a carry in; produces sum and carry out |
| **Ripple carry adder** | Chains full adders together; carry propagates bit by bit |
| **Overflow** | A carry out of the most significant bit, indicating a result too large for the bit width |
| **Half subtractor** | Subtracts two bits; no borrow in |
| **Full subtractor** | Subtracts two bits plus a borrow in; produces difference and borrow out |
| **Bitwise** | An operation applied independently to each corresponding pair of bits |
| **LST (Less Than)** | A comparison unit; outputs 1 if input A is less than input B |
| **Multiplexer (MUX)** | A selector: routes one of several input lines to the output based on a control signal |
| **Control signal** | Bits that command the ALU which operation to perform |
