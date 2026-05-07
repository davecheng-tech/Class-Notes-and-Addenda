# ALU Extension Challenges

Optional extensions for students who finish the 4-bit ALU early. Each builds directly on what you've already made. Pick any one — or all of them! 

Note that each addition should have its own corresponding section in your documentation.

**Difficulty:** ★☆☆ quick &nbsp;|&nbsp; ★★☆ < one period &nbsp;|&nbsp; ★★★ > one period

---

## Zero Flag ★☆☆

Add a `ZF` output that goes 1 when the ALU result is 0000, and 0 otherwise. This is one of the standard flags real CPUs maintain after every operation.

**Hint:** What single gate type goes high only when all its inputs are 0? Apply it to your four output bits.

---

## XOR Operation ★☆☆

Add bitwise XOR as a fifth ALU operation. The gate work is trivial — the interesting part is extending the MUX to handle a fifth input.

**Hint:** You've already extended a 2-in-1 MUX to a 4-in-1. The same idea gets you to 5 operations with a third control bit. When C2=0, your existing 4-op ALU handles everything as before; when C2=1, output the XOR result.

---

## Bitwise OR ★☆☆

Add bitwise OR as an ALU operation — A OR B applied independently to each bit pair.

**Hint:** Same structure as the ANDer. Once the OR unit is built, extending the MUX is the same problem as XOR above.

---

## Equality Detector ★★☆

Add an `EQ` output that goes 1 when A = B, regardless of the current operation.

**Hint:** XOR each bit pair — XOR outputs 1 only when the two bits differ. Now combine four XOR results into a single signal. What gate gives you 1 only when all four are 0?

---

## Overflow and Underflow Indicators ★★☆

Your ALU already computes carry-out (ADD overflow) and borrow-out (SUB underflow) internally. Surface them as named output pins on the ALU tab so they're visible during operation.

The interesting design question: these signals are only meaningful for their respective operations. Can you gate them so `OVF` only lights up during ADD and `UNF` only lights up during SUB?

**Hint:** `OVF = Cout_add · C1' · C0'` and `UNF = Bout_sub · C1' · C0`. Then answer in your design document: what should a real CPU do when it detects overflow?

---

## Flags Register ★★☆

Real CPUs expose a set of status flags after every ALU operation. Build a flags output for your ALU with three bits:

| Flag | Meaning |
|------|---------|
| `ZF` | Result is zero |
| `NF` | Result is negative (MSB = 1) |
| `CF` | Carry/borrow out of MSB |

**Hint:** ZF is the Zero Flag above. NF is just Z[3]. CF is the carry-out of your adder (or borrow-out of your subtractor, depending on operation). Wire all three as a 3-bit output labelled `FLAGS`.

---

## Two's Complement Interpretation ★★☆

No new circuit required — this is a design and reasoning challenge.

When your subtractor produces OVF=1, Z is not garbage. It's the two's complement representation of the negative result. Work out the actual decimal value for three test cases where A < B, and confirm the pattern. Then write a short explanation (3–5 sentences) of why the circuit produces this automatically — you didn't design it to, but it does.

**Hint:** In 4-bit two's complement, the MSB has place value −8, not +8. Apply that to your Z output when OVF=1.

---

## Carry-Lookahead Adder ★★★

Your ripple carry adder has a delay problem: bit 4's sum can't be computed until carry has rippled through all four stages. A carry-lookahead adder computes all carries simultaneously.

For each bit position define **generate** `G_i = A_i · B_i` and **propagate** `P_i = A_i ⊕ B_i`. Then all carries can be computed in parallel:

```
C1 = G0 + P0·C0
C2 = G1 + P1·G0 + P1·P0·C0
C3 = G2 + P2·G1 + P2·P1·G0 + P2·P1·P0·C0
C4 = G3 + P3·G2 + P3·P2·G1 + P3·P2·P1·G0 + P3·P2·P1·P0·C0
```

Build it as a new tab. Verify it produces identical results to your ripple carry adder. Count the total gate usage for each and explain the tradeoff in your design document.

**Hint:** Each sum is still `Z_i = P_i ⊕ C_{i-1}`. The carry equations are the only new part — translate each line directly into gates.

---

## 8-Bit ALU ★★★

Scale your ALU to handle 8-bit inputs and produce an 8-bit result, supporting all four operations.

**Hint:** You need two 4-bit ALUs — a lower half (bits 0–3) and an upper half (bits 4–7). The carry-out of the lower adder feeds into the carry-in of the upper adder. Same for borrow. LST uses the Bout of the MSB stage of the upper half only. Both halves share the same C1 C0 control lines.
