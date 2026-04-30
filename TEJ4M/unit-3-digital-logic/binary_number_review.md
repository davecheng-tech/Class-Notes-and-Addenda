# Review: Binary Numbers, Addition, and Subtraction

## Part 1 — What Is a Number System?

Every number system has a **base** (also called a *radix*). The base tells you how many unique digit symbols exist, and how much each position is worth.

| System | Base | Digits Used | Used In |
|--------|------|-------------|---------|
| Decimal | 10 | 0–9 | Everyday life |
| Binary | 2 | 0, 1 | Digital circuits, computers |
| Hexadecimal | 16 | 0–9, A–F | Memory addresses, colour codes |

In **decimal**, the value of a number is the sum of each digit multiplied by its positional power of 10:

```
5 3 7
│ │ └── 7 × 10⁰ =   7
│ └──── 3 × 10¹ =  30
└────── 5 × 10² = 500
                  ───
                  537
```

Binary works exactly the same way — but powers of **2** instead of 10.

---

## Part 2 — The Binary Number System

### 2.1 Positional Value in Binary

Each bit position represents a power of 2, increasing from right to left:

```
Bit position:   7    6    5    4    3    2    1    0
Place value:   128   64   32   16   8    4    2    1
```

A binary number is read by adding up the place values wherever a **1** appears.

**Example — convert 1011 binary to decimal:**

```
1 0 1 1
│ │ │ └── 1 × 2⁰ =  1
│ │ └──── 1 × 2¹ =  2
│ └────── 0 × 2² =  0
└──────── 1 × 2³ =  8
                   ──
                   11
```

So `1011₂ = 11₁₀`.

---

### 2.2 Counting in Binary

The pattern is mechanical: count up until you run out of digits, then carry left — exactly as in decimal when you go from 9 to 10.

| Decimal | Binary | How it works |
|---------|--------|--------------|
| 0 | 0000 | — |
| 1 | 0001 | — |
| 2 | 0010 | Ones column overflowed; carry to twos column |
| 3 | 0011 | — |
| 4 | 0100 | Twos column overflowed; carry to fours column |
| 5 | 0101 | — |
| 6 | 0110 | — |
| 7 | 0111 | — |
| 8 | 1000 | Everything overflowed; carry to eights column |
| 9 | 1001 | — |
| 10 | 1010 | — |
| 15 | 1111 | All four bits set |
| 16 | 10000 | Needs a fifth bit |

**Key fact:** With *n* bits you can represent 2ⁿ different values: 0 through 2ⁿ − 1.

| Bits | Max value | Range |
|------|-----------|-------|
| 1 | 1 | 0–1 |
| 2 | 3 | 0–3 |
| 4 | 15 | 0–15 |
| 8 | 255 | 0–255 |

---

### 2.3 Converting Decimal → Binary

**Method: repeated division by 2.** Divide the number by 2 repeatedly, recording the remainder each time. Read remainders bottom-to-top.

**Example — convert 13 to binary:**

```
13 ÷ 2 = 6  remainder 1   ← least significant bit (LSB)
 6 ÷ 2 = 3  remainder 0
 3 ÷ 2 = 1  remainder 1
 1 ÷ 2 = 0  remainder 1   ← most significant bit (MSB)

Read upward: 1 1 0 1
```

Check: `1101₂ = 8 + 4 + 0 + 1 = 13` ✓

**Example — convert 45 to binary:**

```
45 ÷ 2 = 22  remainder 1
22 ÷ 2 = 11  remainder 0
11 ÷ 2 =  5  remainder 1
 5 ÷ 2 =  2  remainder 1
 2 ÷ 2 =  1  remainder 0
 1 ÷ 2 =  0  remainder 1

Read upward: 1 0 1 1 0 1
```

So `45₁₀ = 101101₂`. Check: `32 + 0 + 8 + 4 + 0 + 1 = 45` ✓

---

## Part 3 — Binary Addition

### 3.1 The Four Basic Rules

Binary addition follows four simple rules. There are only two digits, so there are only four possible combinations:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

The fourth rule is the crucial one: **1 + 1 = 10 in binary** — that is, sum 0, carry 1. This is directly analogous to 9 + 1 = 10 in decimal.

---

### 3.2 Multi-Bit Addition — Worked Examples

Work right to left, exactly as in long addition. A carry from one column is added into the next column.

---

**Example 1 — no carries: 0101 + 0010**

```
  0 1 0 1    (5)
+ 0 0 1 0    (2)
─────────
  0 1 1 1    (7)
```

Column by column from right: 1+0=1, 0+1=1, 1+0=1, 0+0=0. No carries. Result: 7. ✓

---

**Example 2 — one carry: 0011 + 0001**

```
    1 1 <--- (carries)
  0 0 1 1    (3)
+ 0 0 0 1    (1)
─────────
  0 1 0 0    (4)
```

Step through:
- Col 0 (rightmost): 1 + 1 = 0, carry 1
- Col 1: 1 + 0 + carry(1) = 0, carry 1
- Col 2: 0 + 0 + carry(1) = 1, carry 0
- Col 3: 0 + 0 = 0

Result: `0100₂ = 4` ✓

---

**Example 3 — multiple carries: 0111 + 0001**

```
  1 1 1 <--- (carries)
  0 1 1 1    (7)
+ 0 0 0 1    (1)
─────────
  1 0 0 0    (8)
```

Step through:
- Col 0: 1 + 1 = 0, carry 1
- Col 1: 1 + 0 + carry(1) = 0, carry 1
- Col 2: 1 + 0 + carry(1) = 0, carry 1
- Col 3: 0 + 0 + carry(1) = 1

Result: `1000₂ = 8` ✓

---

**Example 4 — larger values: 1011 + 0110**

```
  1 1 1 <----- (carries)  
    1 0 1 1    (11)
+   0 1 1 0    ( 6)
───────────
  1 0 0 0 1  — wait, that overflows 4 bits!
```

Let's be precise:
- Col 0: 1 + 0 = 1
- Col 1: 1 + 1 = 0, carry 1
- Col 2: 0 + 1 + carry(1) = 0, carry 1
- Col 3: 1 + 0 + carry(1) = 0, carry 1

The carry out of col 3 is 1 — this is an **overflow** (the result, 17, doesn't fit in 4 bits). The 4-bit result is `0001`, which is wrong if we only have 4 bits. The carry-out bit signals the overflow. This is important for your ALU project.

---

### 3.3 Three-Input Addition (with Carry-In)

When you chain adder circuits, each stage receives three inputs: A, B, and a **carry-in** (Cin) from the previous stage.

The rules expand to:

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0   |
| 0 | 0 |  1  |  1  |  0   |
| 0 | 1 |  0  |  1  |  0   |
| 0 | 1 |  1  |  0  |  1   |
| 1 | 0 |  0  |  1  |  0   |
| 1 | 0 |  1  |  0  |  1   |
| 1 | 1 |  0  |  0  |  1   |
| 1 | 1 |  1  |  1  |  1   |

**Pattern to notice:** Sum = 1 whenever an **odd number** of inputs are 1 (this is the XOR parity rule). Cout = 1 whenever **two or more** inputs are 1.

---

## Part 4 — Binary Subtraction

### 4.1 Borrow Method (Direct Subtraction)

Binary subtraction mirrors decimal long subtraction. When the top digit is smaller than the bottom digit, you **borrow** from the next column.

Borrow rules:
- 0 − 0 = 0
- 1 − 0 = 1
- 1 − 1 = 0
- 0 − 1 = 1 (borrow from left; the borrowed 1 is worth 2 in this column)

---

**Example 1 — no borrow: 1101 − 0100**

```
  1 1 0 1    (13)
- 0 1 0 0    ( 4)
─────────
  1 0 0 1    ( 9)
```

Column by column: 1−0=1, 0−0=0, 1−1=0, 1−0=1. Result: 9 ✓

---

**Example 2 — with borrow: 1010 − 0011**

```
  1 0 1 0    (10)
- 0 0 1 1    ( 3)
─────────
```

- Col 0: 0 − 1 → borrow. Becomes 10₂ (=2) − 1 = 1. Mark borrow into col 1.
- Col 1: 1 − 1 − borrow(1) = 1 − 1 − 1 = −1 → borrow again. Becomes 11₂ (=3) − 1 − 1 = 1. Borrow into col 2.
- Col 2: 0 − 0 − borrow(1) → borrow again. Becomes 10₂ (=2) − 0 − 1 = 1. Borrow into col 3.
- Col 3: 1 − 0 − borrow(1) = 0

Result: `0111₂ = 7` ✓

---

### 4.2 Two's Complement — How Computers Actually Subtract

Real digital systems almost never use borrow-method subtraction directly. Instead, they use a technique called **two's complement**, which converts subtraction into addition. This is why the same adder circuit can handle both operations.

#### Step 1 — One's Complement (Invert All Bits)

Flip every bit: 0 becomes 1, 1 becomes 0.

```
Original:         1010  (10)
One's complement: 0101
```

#### Step 2 — Two's Complement (Add 1)

```
One's complement: 0101
+ 1:              0001
                  ────
Two's complement: 0110  (6... but it represents −10)
```

Check: `10 + (−10) = 0`. In 4-bit arithmetic:

```
  1 0 1 0   (+10)
+ 0 1 1 0   (−10, as two's complement)
─────────
1 0 0 0 0
```

The carry-out overflows the 4-bit result, leaving `0000`. Correct — 10 − 10 = 0. ✓

#### Performing Subtraction via Two's Complement

To compute **A − B**:
1. Take the two's complement of B
2. Add it to A
3. Discard the carry-out (if any)

**Example — compute 1101 − 0101 (13 − 5):**

Step 1: Two's complement of 0101:
```
Invert: 1010
Add 1:  1011   (this is −5 in two's complement)
```

Step 2: Add:
```
  1 1 0 1    (13)
+ 1 0 1 1    (−5)
─────────
1 1 0 0 0
```

Step 3: Discard the carry-out. Result: `1000₂ = 8`. And 13 − 5 = 8. ✓

---

### 4.3 Why This Matters for Your ALU

Your ALU project uses a **full subtractor** circuit. Internally it computes the difference and a **borrow-out** (Bout) — analogous to the carry-out in addition. When Bout = 1, it means the minuend was too small (A < B), and the circuit had to borrow. This is how the **Less Than (LST)** operation works in your 4-bit ALU.

---

## Part 5 — Quick Reference

### Binary ↔ Decimal Table (0–15)

| Dec | Bin | Dec | Bin |
|-----|-----|-----|-----|
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | 10 | 1010 |
| 3 | 0011 | 11 | 1011 |
| 4 | 0100 | 12 | 1100 |
| 5 | 0101 | 13 | 1101 |
| 6 | 0110 | 14 | 1110 |
| 7 | 0111 | 15 | 1111 |

### Powers of 2

| Power | Value |
|-------|-------|
| 2⁰ | 1 |
| 2¹ | 2 |
| 2² | 4 |
| 2³ | 8 |
| 2⁴ | 16 |
| 2⁵ | 32 |
| 2⁶ | 64 |
| 2⁷ | 128 |

### Binary Addition at a Glance

```
0 + 0 = 0         (no carry)
0 + 1 = 1         (no carry)
1 + 0 = 1         (no carry)
1 + 1 = 0         (carry 1)
1 + 1 + 1 = 1     (carry 1)
```

### Binary Subtraction at a Glance

```
0 − 0 = 0         (no borrow)
1 − 0 = 1         (no borrow)
1 − 1 = 0         (no borrow)
0 − 1 = 1         (borrow 1 from next column)
```

---

## Part 6 — Practice Problems

Work these out by hand before moving on to CircuitVerse.

**Addition:**
1. `0011 + 0100` = ?
2. `0101 + 0101` = ?
3. `0110 + 0111` = ?
4. `1001 + 0110` = ?

**Subtraction (borrow method):**
5. `1010 − 0011` = ?
6. `1111 − 0110` = ?
7. `1000 − 0001` = ?

**Decimal → Binary:**
8. 9 in binary = ?
9. 14 in binary = ?
10. 7 in binary = ?

**Binary → Decimal:**
11. `1001` = ?
12. `1110` = ?
13. `0111` = ?

---

*Answers: 1) 0111=7  2) 1010=10  3) 1101=13  4) 1111=15  5) 0111=7  6) 1001=9  7) 0111=7  8) 1001  9) 1110  10) 0111  11) 9  12) 14  13) 7*
