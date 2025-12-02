# When Should You Use a Ternary Operator?

The ternary operator  
`condition ? valueIfTrue : valueIfFalse`  
is a compact way to choose between two values.

It is useful, but only in the right situations. The goal of programming is **clarity**, not “writing fewer lines.” A shorter line of code is not automatically better. If a ternary makes your code harder to read, it is the wrong tool.

## 1. GOOD USES OF TERNARY OPERATORS

Ternaries are good when the **entire decision is simple, local, and easy to read in one breath**. They work best when you are choosing a value—not running multiple statements.

### Example A: Choosing a default value

```java
int score = scores[i];
int adjusted = (score < 0) ? 0 : score;
```

### Example B: Quick value selection inside array traversal

```java
for (int i = 0; i < nums.length; i++) {
    int sign = (nums[i] >= 0) ? 1 : -1;
    total += sign;
}
```

## 2. BAD USES OF TERNARY OPERATORS

Ternaries are **not** good when they hide logic, nest decisions, or create mental gymnastics.

### Example C: Hiding multi-step logic

```java
int result = (nums[i] % 2 == 0) ? nums[i] * 2 : nums[i] * nums[i] - 3;
```

Better:

```java
int result;
if (nums[i] % 2 == 0) {
    result = nums[i] * 2;
} else {
    result = nums[i] * nums[i] - 3;
}
```

### Example D: Nesting ternaries

```java
int category = (nums[i] < 0) ? -1 :
               (nums[i] == 0) ? 0 : 1;
```

Better:

```java
int category;
if (nums[i] < 0) {
    category = -1;
} else if (nums[i] == 0) {
    category = 0;
} else {
    category = 1;
}
```

### Example E: Ternary inside another operation

```java
sum += (nums[i] > 10) ? nums[i] * 3 : nums[i] / 2;
```

Better:

```java
int value;
if (nums[i] > 10) {
    value = nums[i] * 3;
} else {
    value = nums[i] / 2;
}
sum += value;
```

## 3. RULE OF THUMB

A ternary is acceptable when:

1. The decision is **simple**.  
2. The purpose is **immediately clear**.  
3. It returns a **value**, not multiple steps.  
4. A beginner can read it without slowing down.

When in doubt, use an if/else.

## 4. GOOD VS. BAD IN A LOOP

### Good

```java
for (int i = 0; i < temps.length; i++) {
    int safe = (temps[i] < 0) ? 0 : temps[i];
    corrected[i] = safe;
}
```

### Bad

```java
corrected[i] = (temps[i] < 0) ? 0 :
               (temps[i] > 100) ? temps[i] - 10 :
               (temps[i] == 42) ? 999 : temps[i];
```
