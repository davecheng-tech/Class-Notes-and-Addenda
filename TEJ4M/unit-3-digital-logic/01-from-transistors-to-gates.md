# From Transistors to Gates

In Unit 2, you took apart what a CPU *does*: it executes instructions, manages memory, runs processes. You saw that the processor in your Chromebook speaks x86-64, that an iPhone speaks ARM64, and that these instruction sets are fundamentally different languages.

But that raises a deeper question: what is a CPU *made of*? What is actually happening inside the chip when an instruction executes?

The answer, at the bottom of everything, is this: **a CPU is a very large collection of switches**.

This note covers:

- How transistors work as electronic switches
- Why binary is a natural consequence of switches
- How the history of computing is really a history of making switches smaller
- How switches connect to form logic gates
- A review of the seven basic logic gates from TEJ3M

<br>

## 1. The Transistor: A Switch Made of Silicon

A **transistor** is a semiconductor device with three terminals. For our purposes, the key behaviour is simple: apply a small voltage to the control terminal, and the transistor switches from blocking current to conducting it. Remove the voltage, and it switches back.

Two states: `ON` and `OFF`, or `1` and `0`.

That is it. A transistor is a switch you can control electrically, with no moving parts, at speeds measured in billionths of a second.

Modern CPUs contain billions of these transistors etched onto a piece of silicon the size of a fingernail. The Apple M3 chip in a 2023 MacBook Pro contains approximately **37 billion transistors**. The Intel Celeron in your Chromebook contains about 1 billion. Every single one of them is, at its core, a switch.

> [!NOTE]
> The transistors in modern CPUs are called **MOSFETs** (Metal-Oxide-Semiconductor Field-Effect Transistors). The key dimension is the **gate length** — how physically small the transistor is. Apple's M3 chip uses a 3-nanometre process, meaning each transistor is roughly 3 nm across. A human hair is about 80,000 nm wide.

<br>

## 2. Why Binary?

Transistors are switches. Switches have two states: on or off. Two states map naturally to two digits: **1** and **0**.

This is not an arbitrary design choice, rather, it reflects real-world physics. An analog signal (e.g., audio from a microphone) exists on a continuous spectrum and is difficult to store, transmit, or process without accumulating noise and error. A digital signal that is either clearly HIGH or clearly LOW is far more robust. Even if the voltage drifts slightly, the circuit can still determine whether it is closer to 1 or 0.

Binary also has clean mathematical properties: you can add, subtract, compare, and perform logical operations on 1s and 0s using circuits. That is exactly what the CPU does millions of times per second.

> [!TIP]
> You already worked with binary numbers in this course. One bit is one transistor output. Eight bits is a byte. The 8-bit and 64-bit values you saw in Unit 2 are just different numbers of transistor outputs bundled together.

<br>

## 3. A Short History: Making Switches Smaller

The history of computing is largely a history of shrinking switches and packing more of them into less space.

| Era | Technology | Scale | Example |
|-----|-----------|-------|---------|
| 1940s | Vacuum tubes | Room-sized machines | ENIAC (1945): 18,000 vacuum tubes, 167 m², 150 kW |
| 1947 | First transistor | Small, reliable, low power | Invented at Bell Labs; replaced vacuum tubes |
| 1958 | Integrated circuit (IC) | Multiple transistors on one chip | Jack Kilby's first IC at Texas Instruments |
| 1971 | First microprocessor | Thousands of transistors | Intel 4004: 2,300 transistors, 4-bit |
| 1993 | Pentium | Millions of transistors | Intel Pentium: 3.1 million transistors, 32-bit |
| 2006 | Multi-core CPUs | Hundreds of millions | Intel Core 2 Duo: 291 million transistors |
| 2020s | Modern CPUs | Billions of transistors | Apple M3: 37 billion transistors, 3 nm process |

**Moore's Law** is the observation by Intel co-founder Gordon Moore in 1965 that the number of transistors on a chip doubles roughly every two years. This held roughly true for about 50 years. The physical limits of silicon are now being approached, which is one reason why chip designers have shifted from making individual transistors faster to adding more cores and specialized hardware units (like the GPU for graphics, and Apple's Neural Engine for machine learning).

<br>

## 4. From Switches to Logic Gates

A single transistor does one thing: switches on or off. But connect two transistors together and something more interesting happens.

Two transistors **in series** (one after the other): current only flows if *both* are on. Both must be 1 for the output to be 1. You have just built an **AND gate**.

Two transistors **in parallel** (side by side): current flows if *either* is on. Either being 1 is enough for the output to be 1. You have just built an **OR gate**.

A single transistor configured as an inverter flips the signal: when it is on, the output is pulled low; when it is off, the output is high. You have built a **NOT gate**.

Every logic gate in a CPU (and therefore every instruction, every calculation, every pixel on your screen) is ultimately a small arrangement of transistors doing exactly this.

```
Two transistors in series:       Two transistors in parallel:
                                     
   ┌──[T1]──[T2]──┐                  ┌──[T1]──┐
IN ┤              ├ OUT           IN ┤──[T2]──├ OUT
   └──────────────┘                  └────────┘

   AND: both must be ON          OR: either can be ON
```

> [!NOTE]
> Real CMOS gates use complementary pairs of transistors (PMOS and NMOS) for better efficiency, so the actual transistor count per gate is typically 4–6. But the logical behaviour is exactly what the AND/OR description above predicts.

<br>

## 5. Review: The Seven Basic Logic Gates

In TEJ3M, you should have built and explained all seven basic logic gates in CircuitVerse. This section is a compact reference.

For each gate, we have a plain English description, truth table, and Boolean expression. The notation used throughout this unit:

- `A'` means NOT A
- `AB` or `A · B` means A AND B
- `A + B` means A OR B
- `A ⊕ B` means A XOR B

---

### AND

Output is 1 only when **all** inputs are 1. Think: both conditions must be true.

| A | B | Z |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

`Z = A · B`

*Everyday example: a car starts only when the key is in AND the brake is pressed.*

---

### OR

Output is 1 when **at least one** input is 1. Think: either condition is enough.

| A | B | Z |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

`Z = A + B`

*Everyday example: a hotel room light turns on if you use the switch by the door OR the switch by the bed.*

---

### NOT

A single-input gate. Output is always the **opposite** of the input. Also called an inverter.

| A | Z |
|---|---|
| 0 | 1 |
| 1 | 0 |

`Z = A'`

*Everyday example: a normally-closed alarm sensor in which the output is 1 (alarm) when the input is 0 (circuit broken).*

---

### XOR (Exclusive OR)

Output is 1 when inputs are **different**. Output is 0 when inputs are the same.

| A | B | Z |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

`Z = A ⊕ B`

*Everyday example: a hallway light controlled by two switches in which flipping either switch toggles the light, but flipping both returns it to the original state.*

---

### NAND

Output is 0 only when **all** inputs are 1. The opposite of AND.

| A | B | Z |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

`Z = (A · B)'`

NAND is a **universal gate**: any logic circuit can be built using only NAND gates. It is also the most naturally efficient gate to manufacture in CMOS silicon.

---

### NOR

Output is 1 only when **all** inputs are 0. The opposite of OR.

| A | B | Z |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

`Z = (A + B)'`

NOR is also a **universal gate**: like NAND, any logic circuit can be built using only NOR gates.

---

### XNOR (Exclusive NOR)

Output is 1 when inputs are **the same**. The opposite of XOR. Also called an equivalence gate.

| A | B | Z |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

`Z = (A ⊕ B)'`

*Everyday example: a sensor that triggers an alarm when two values don't match, e.g., the commanded state of a valve and its actual state.*

---

> [!TIP]
> A useful pattern: every gate has a complementary pair.
> - AND <> NAND
> - OR <> NOR  
> - XOR <> XNOR
>
> The NAND, NOR, and XNOR truth tables are exactly the NOT of AND, OR, and XOR respectively. Just flip every output bit.

<br>

## 6. Where This Unit Goes Next

You now have all the ingredients: switches > binary > gates. But a single gate can only do one simple thing. The question this unit answers is: **how do you combine gates to build something useful?**

A 4-bit adder requires about 18 gates. A single 4-function ALU requires around 80. The processor in your Chromebook executes instructions by routing signals through billions of these gate arrangements, all switching billions of times per second.

The next lesson introduces **combinational logic**: how to design circuits that compute any logical relationship you can express as a truth table, and how to move between truth tables, Boolean equations, and circuit diagrams.

<br>

## 7. Key Terms

| Term | Definition |
|---|---|
| **Transistor** | A semiconductor switch controlled by voltage; the basic building block of digital logic |
| **MOSFET** | The type of transistor used in modern digital ICs; switches via a gate voltage |
| **Binary** | A number system with two digits (0 and 1); maps directly to the on/off states of a transistor |
| **Logic gate** | A circuit built from transistors that performs one Boolean operation |
| **Universal gate** | A gate type (NAND or NOR) from which any other gate can be constructed |
| **Integrated circuit (IC)** | A chip containing many transistors and gates fabricated together on silicon |
| **Moore's Law** | The historical observation that transistor density doubles roughly every two years |
| **CMOS** | Complementary Metal-Oxide-Semiconductor; the dominant technology for building digital ICs today |
