# Solutions: Boolean Algebra Simplification

---

## Part A — Gate Counts

**A1.** `Z = ((A · B) · C) + (A · C)`
AND(A·B) + AND((A·B)·C) + AND(A·C) + OR = **4 gates**

**A2.** `Z = ((A + B')')'`
NOT(B') + OR(A+B') + NOT((A+B')') + NOT(outer) = **4 gates**

**A3.** `Z = (A + B) · C + (A · C)`
OR(A+B) + AND((A+B)·C) + AND(A·C) + OR = **4 gates**

---

## Part B — Fill in the Steps

### B1. `Z = A·B + A·B'` → `Z = A`

```
  = A·(B + B')    Distributive
  = A·1           Complement
  = A             Identity
```

---

### B2. `Z = (A·B)' · B` → `Z = A'·B`

```
  = (A' + B') · B    De Morgan's
  = A'·B + B'·B      Distributive
  = A'·B + 0         Complement
  = A'·B             Identity
```

---

### B3. `Z = (A + B) · (A + C)` → `Z = A + B·C`

```
  = A + B·C    Distributive  (OR distributes over AND, applied right-to-left)
```

---

### B4. `Z = A·B·C + A·B·C' + A·B'·C` → `Z = A·(B + C)`

Before: NOT×2 + AND×3 + OR = **6 gates**
After: OR + AND = **2 gates** — saved 4

```
  = A·B·(C + C') + A·B'·C    Distributive
  = A·B·1 + A·B'·C           Complement
  = A·B + A·B'·C             Identity
  = A·(B + B'·C)             Distributive
  = A·(B + B')(B + C)         Distributive  (OR over AND)
  = A·1·(B + C)              Complement
  = A·(B + C)                Identity
```

---

## Part C — Simplification

### C1. `Z = A·B' + A·(B' + C) + B·(B' + C)` — **6 gates → 5 gates**

```
  = A·B' + A·B' + A·C + B·B' + B·C    Distributive  (expand terms 2 and 3)
  = A·B' + A·B' + A·C + 0 + B·C       Complement  (B·B' = 0)
  = A·B' + A·C + B·C                   Idempotent + Identity
```

*Note: further simplification to A·B' + B·C requires the Consensus theorem, which is out of scope. Three terms is the stopping point.*

---

### C2. `Z = [A·B·(C + B·D) + A'·B']·C` — **8 gates → 6 gates**

```
  = [A·B·C + A·B·B·D + A'·B']·C       Distributive
  = [A·B·C + A·B·D + A'·B']·C         Idempotent  (B·B = B)
  = A·B·C·C + A·B·D·C + A'·B'·C       Distributive  (distribute ·C)
  = A·B·C + A·B·C·D + A'·B'·C         Idempotent  (C·C = C)
  = A·B·C + A'·B'·C                    Absorption  (A·B·C absorbs A·B·C·D)
  = C·(A·B + A'·B')                    Distributive
```

*Note: A·B + A'·B' is XNOR. Without the XNOR identity this is the stopping point.*

---

### C3. `Z = A'·B·C + A'·B·C' + A·B·C' + A·B'·C' + A·B·C` — **9 gates → 3 gates**

```
  Pair terms 1 & 2  (share A'·B):
    A'·B·(C + C') = A'·B     [Distributive, Complement, Identity]

  Pair terms 3 & 5  (share A·B):
    A·B·(C' + C) = A·B       [Distributive, Complement, Identity]

  Z = A'·B + A·B + A·B'·C'

  = B·(A' + A) + A·B'·C'     Distributive
  = B + A·B'·C'              Complement + Identity

  Simplify A·B'·C' within the OR:
  B + A·B'·C' = (B + A·C')(B + B')    Distributive  (treat A·C' as one unit)
              = (B + A·C')·1           Complement
              = B + A·C'              Identity
```

Final: `Z = B + A·C'`

After: NOT(C') + AND(A·C') + OR = **3 gates** — saved 6

---

## Part D

### D1.

Minterms: 011 (A=0,B=1,C=1), 101 (A=1,B=0,C=1), 111 (A=1,B=1,C=1)

**SOP:** `Z = A'·B·C + A·B'·C + A·B·C`

Before: NOT×2 + AND×3 + OR = **6 gates**
After: OR(A+B) + AND(C·(A+B)) = **2 gates** — saved 4

```
  = C·(A'·B + A·B' + A·B)    Distributive  (factor C)
  = C·(A'·B + A·(B' + B))    Distributive  (factor A from last two)
  = C·(A'·B + A·1)            Complement
  = C·(A'·B + A)              Identity
  = C·(A + A')·(A + B)        Distributive  (OR over AND: A + A'B = (A+A')(A+B))
  = C·1·(A + B)               Complement
  = C·(A + B)                 Identity
```

---

### D2. `Z = A'·B'·C' + A'·B'·C + A·B'·C + A·B·C`

Before: NOT×3 + AND×4 + OR = **8 gates**
After: NOT×2 + AND×2 + OR = **5 gates** — saved 3

```
  = A'·B'·(C' + C) + A·B'·C + A·B·C    Distributive  (pair terms 1 & 2)
  = A'·B' + A·B'·C + A·B·C              Complement + Identity
  = A'·B' + A·C·(B' + B)                Distributive  (pair terms 3 & 4)
  = A'·B' + A·C·1                        Complement
  = A'·B' + A·C                          Identity
```
