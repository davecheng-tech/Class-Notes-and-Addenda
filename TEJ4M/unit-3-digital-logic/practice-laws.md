# Extra Practice: Boolean Laws

This sheet gives you focused practice on each law individually. Work through the section for whichever law you find difficult. Each section shows the law, then asks you to apply it.

---

## Identity Laws

```
A + 0 = A
A · 1 = A
```

ORing with 0 or ANDing with 1 does nothing — drop the constant and keep the expression.

Simplify each expression using only the identity laws:

1. `X + 0`
2. `Y · 1`
3. `(A + B) · 1`
4. `A·B + 0`
5. `(A' + B·C) · 1`

<details>
<summary>Answers</summary>

1. `X`
2. `Y`
3. `A + B`
4. `A·B`
5. `A' + B·C`

</details>

---

## Null / Domination Laws

```
A + 1 = 1
A · 0 = 0
```

A dominant constant collapses the whole expression — 1 dominates OR, 0 dominates AND.

Simplify each expression using only the null laws:

1. `X + 1`
2. `Y · 0`
3. `(A + B) + 1`
4. `A·B·C · 0`
5. `(A'·B + C·D) · 0`

<details>
<summary>Answers</summary>

1. `1`
2. `0`
3. `1`
4. `0`
5. `0`

</details>

---

## Idempotent Laws

```
A + A = A
A · A = A
```

A variable (or expression) combined with itself is just itself. The duplicate copy is redundant.

Simplify each expression using only the idempotent laws:

1. `X + X`
2. `Y · Y`
3. `A·B + A·B`
4. `(A + B) · (A + B)`
5. `A·B·C + A·B·C`

<details>
<summary>Answers</summary>

1. `X`
2. `Y`
3. `A·B`  *(treat A·B as a single unit — it is the "A" in the law)*
4. `A + B`  *(treat A+B as a single unit)*
5. `A·B·C`

</details>

---

## Complement Laws

```
A + A' = 1
A · A' = 0
```

A variable and its complement always resolve to a constant — OR gives 1, AND gives 0.

Simplify each expression using only the complement laws:

1. `X + X'`
2. `Y · Y'`
3. `A'·B + (A'·B)'`
4. `(A + B) · (A + B)'`
5. `A'·(A')'`

<details>
<summary>Answers</summary>

1. `1`
2. `0`
3. `1`  *(treat A'·B as the variable — it ORed with its complement is 1)*
4. `0`  *(treat A+B as the variable — it ANDed with its complement is 0)*
5. `0`  *(`(A')' = A` by double negation, so this is `A'·A = 0`)*

</details>

---

## Double Negation

```
(A')' = A
```

Two NOTs cancel. Any time you see a NOT applied twice, remove both.

Simplify each expression using only double negation:

1. `(X')'`
2. `((A + B)')'`
3. `((A·B)')'`
4. `(((A')')')`
5. `((A' + B)')'`

<details>
<summary>Answers</summary>

1. `X`
2. `A + B`
3. `A·B`
4. `A'`  *(cancel the inner two NOTs first: `((A')') = A`, then one NOT remains: `(A)' = A'`)*
5. `A' + B`

</details>

---

## Commutative Laws

```
A + B = B + A
A · B = B · A
```

The order of operands in OR or AND doesn't matter. Reorder freely.

Rewrite each expression using commutativity (there is more than one correct answer — any valid reordering counts):

1. Rewrite `B + A` with A first
2. Rewrite `B · A` with A first
3. Rewrite `C + A·B` with the AND term first
4. Rewrite `(B + C) · A` with A first
5. Show that `A·B + C·D` equals `D·C + B·A` using commutativity

<details>
<summary>Answers</summary>

1. `A + B`
2. `A · B`
3. `A·B + C`
4. `A · (B + C)`
5. Apply commutativity to the whole sum: `C·D + A·B`, then to each product: `D·C + B·A`

</details>

---

## Associative Laws

```
(A + B) + C = A + (B + C)
(A · B) · C = A · (B · C)
```

When the same operation is chained, grouping doesn't matter. Re-parenthesize freely.

Rewrite each expression by changing the grouping:

1. Rewrite `(A + B) + C` with C grouped with B instead
2. Rewrite `A · (B · C)` with A grouped with B instead
3. Rewrite `((A + B) + C) + D` without any parentheses
4. Show that `(A · B) · (C · D)` equals `A · (B · C · D)` using associativity
5. Rewrite `A + (B + (C + D))` as a left-to-right chain

<details>
<summary>Answers</summary>

1. `A + (B + C)`
2. `(A · B) · C`
3. `A + B + C + D`
4. `(A·B)·(C·D) = A·(B·(C·D)) = A·(B·C·D)` — regroup right side step by step
5. `((A + B) + C) + D`

</details>

---

## Distributive Laws

```
A · (B + C) = AB + AC     ← AND distributes over OR
A + (B · C) = (A+B)(A+C)  ← OR distributes over AND
```

Use distributive to expand (multiply out) or factor (pull out a common term).

**Expand** each expression:

1. `A · (B + C)`
2. `X · (Y + Z + W)`
3. `A · (B + C + D)`

**Factor** each expression:

4. `AB + AC`
5. `XY + XZ + XW`
6. `A'B + A'C`

<details>
<summary>Answers</summary>

1. `AB + AC`
2. `XY + XZ + XW`
3. `AB + AC + AD`
4. `A · (B + C)`
5. `X · (Y + Z + W)`
6. `A' · (B + C)`  *(A' is the common factor)*

</details>

---

## Absorption Laws

```
A + AB = A
A · (A + B) = A
```

A shorter term absorbs any longer term that contains it as a factor.

Simplify each expression using only absorption:

1. `A + AB`
2. `A · (A + B)`
3. `X + XY + XZ`
4. `A' + A'·B`
5. `(A + B) + (A + B)·C`

<details>
<summary>Answers</summary>

1. `A`
2. `A`
3. `X`  *(apply absorption twice: X absorbs XY, then X absorbs XZ)*
4. `A'`  *(A' plays the role of "A" in the law)*
5. `A + B`  *(treat A+B as the "A" in the law)*

</details>

---

## De Morgan's Laws

```
(A · B)' = A' + B'
(A + B)' = A' · B'
```

NOT distributes inward and the operation flips: AND becomes OR, OR becomes AND.

Apply De Morgan's laws:

1. Simplify `(A · B)'`
2. Simplify `(A + B)'`
3. Simplify `(A · B · C)'`
4. Simplify `(A + B + C)'`
5. Apply De Morgan's in reverse: rewrite `A' + B'` as a single NOT expression
6. Apply De Morgan's in reverse: rewrite `A'·B'` as a single NOT expression

<details>
<summary>Answers</summary>

1. `A' + B'`
2. `A'·B'`
3. `A' + B' + C'`  *(extend the law: NOT over an AND of any number of inputs flips to OR)*
4. `A'·B'·C'`  *(extend the law: NOT over an OR of any number of inputs flips to AND)*
5. `(A·B)'`
6. `(A+B)'`

</details>

---

## XOR Identity

```
A'B + AB' = A ⊕ B
```

Two AND terms where one variable is complemented in each — and they differ only by which variable is complemented — are XOR in disguise.

1. Simplify `A'B + AB'`
2. Simplify `P'Q + PQ'`
3. Expand `A ⊕ B` into sum-of-products form
4. Simplify `C·(A'B + AB')`
5. Is `AB' + A'B` the same as `A ⊕ B`? Explain.

<details>
<summary>Answers</summary>

1. `A ⊕ B`
2. `P ⊕ Q`
3. `A'B + AB'`
4. `C · (A ⊕ B)`  *(factor C from both terms first, then recognize XOR)*
5. Yes — by commutativity of OR the two terms are just swapped, which doesn't change the result. `AB' + A'B = A'B + AB' = A ⊕ B`

</details>
