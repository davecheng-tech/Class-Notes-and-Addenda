# Solutions: More Boolean Algebra Simplification

---

## Part C

### C1. `Z = A·B·C + A·B·C'` — **4 gates → 1 gate**

```
  = A·B·(C + C')    Distributive
  = A·B·1           Complement
  = A·B             Identity
```

---

### C2. `Z = A'·B + A·B + A·C` — **5 gates → 2 gates**

```
  = B·(A' + A) + A·C    Distributive
  = B·1 + A·C           Complement
  = B + A·C             Identity
```

---

### C3. `Z = A·B + A·C + A·B·C + A·B·C'` — **6 gates → 2 gates**

```
  = A·B + A·C + A·B·C'    Absorption  (A·B absorbs A·B·C)
  = A·B + A·C              Absorption  (A·B absorbs A·B·C')
  = A·(B + C)              Distributive
```

---

### C4. `Z = (A + B)' + A·B'` — **5 gates → 1 gate**

```
  = A'·B' + A·B'      De Morgan's  [(A+B)' = A'·B']
  = B'·(A' + A)        Distributive
  = B'·1               Complement
  = B'                 Identity
```

---

### C5. `Z = A'·B·C' + A'·B·C + A·B'·C' + A·B'·C` — **8 gates → 1 gate**

```
  = A'·B·(C' + C) + A·B'·C' + A·B'·C    Distributive  (pair terms 1 & 2)
  = A'·B·1 + A·B'·C' + A·B'·C            Complement
  = A'·B + A·B'·(C' + C)                  Distributive  (pair terms 3 & 4)
  = A'·B + A·B'·1                          Complement
  = A'·B + A·B'                            Identity
  = A ⊕ B                                  XOR Identity
```

---

## Part D

### D1.

Minterms: 011, 111

**SOP:** `Z = A'·B·C + A·B·C`

```
  = B·C·(A' + A)    Distributive
  = B·C·1           Complement
  = B·C             Identity
```

Before: NOT(A') + AND×2 + OR = **4 gates**
After: AND(B·C) = **1 gate** — saved 3

---

### D2.

Minterms: 010, 011, 101, 111

**SOP:** `Z = A'·B·C' + A'·B·C + A·B'·C + A·B·C`

```
  = A'·B·(C' + C) + A·B'·C + A·B·C    Distributive  (pair terms 1 & 2)
  = A'·B + A·B'·C + A·B·C              Complement + Identity
  = A'·B + A·C·(B' + B)                Distributive  (pair terms 3 & 4)
  = A'·B + A·C·1                        Complement
  = A'·B + A·C                          Identity
```

Before: NOT×3 + AND×4 + OR = **8 gates**
After: NOT(A') + AND×2 + OR = **4 gates** — saved 4
