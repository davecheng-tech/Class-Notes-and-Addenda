# Becoming More Stylish in Code (Yes, *You*)

Your code already works. That’s great.  
Now we level up: we make the code **clear**.

Clear code shows your thinking. It communicates **intent** — meaning:
someone should be able to read your code and *understand what you were trying to do* without asking you.

We are now moving from:

> “It runs.”  

to  

> “I know why this works.”

This is programming maturity.


## The Big Idea: *Code Should Explain Itself*

We improve clarity by:

- Replacing **magic numbers** with named variables
- Choosing variable names based on **meaning**, not convenience
- Drawing shapes relative to the space they belong to (for Processing)
- Using calculations instead of typing hard-coded values everywhere

It is completely okay if this means **more lines of code**.
More lines ≠ worse. Clearer meaning always wins.


## Magic Numbers vs. Meaning

### In Processing Graphics

#### ❌ “It runs, but… what is 200?”
```java
rect(200, 300, 200, 150);
```

#### ✅ “A house drawn where I can adjust size + position easily”
```java
float houseX = width * 0.33f;
float houseY = height * 0.50f;
float houseW = width * 0.30f;
float houseH = height * 0.25f;

rect(houseX, houseY, houseW, houseH);
```

### In Regular Java Code

#### ❌ Magic number tax rate
```java
double total = price * 1.13;
```

#### ✅ Named constant communicates *intent*
```java
final double TAX_RATE = 1.13;
double total = price * TAX_RATE;
```
Note that the convention for constants is an `ALL_CAPS` variable name.


## Repetition Is a Signal

If you type the same number 3+ times, that number wants a name.

### ❌ Repeated numbers everywhere
```java
line(0, 200, 200, 200);
line(0, 220, 200, 220);
line(0, 240, 200, 240);
```

### ✅ Use variables to show intent
```java
float yStart = 200;
float spacing = 20;

for (float y = yStart; y <= yStart + 40; y += spacing) {
  line(0, y, 200, y);
}
```

## Drawing Relative to Space (Processing Trick)

Instead of drawing something in one frozen location forever:

1. Draw your pattern like it starts at (0,0)
2. Then **shift** (translate) it where you want

### Example
```java
float sectorW = width / 3;
float sectorH = height / 2;

float sx = sectorW;  // sector (1,2): second column, top row
float sy = 0;

// Draw everything relative to (sx, sy)
rect(sx + 20, sy + 40, sectorW * 0.5f, sectorH * 0.5f);
```

## What Improving Style Looks Like (Choose Your Stage)

| Stage | What Changes | Skill You’re Practicing | Example |
|------|-------------|------------------------|---------|
| 1 | Replace repeated values with variables | Reducing magic numbers | `float stripeW = 20;` |
| 2 | Group related layout values | Describing meaning | `float sectorW = width / 3;` |
| 3 | Draw relative to an origin | Code that can *move* | `rect(sx + x, sy + y, ...)` |
| 4 | Use width/height to resize automatically | Truly responsive graphics | No hard-coded numbers |


## Why This Actually Matters
Because real code gets changed. *Always*.

Clear code is:
- easier to fix
- easier to reuse
- easier for others to learn from
- a sign that **you understand your own solution**

Your future self (and your teammates in Grade 11/12) will thank you. Aim to write code that looks like you care about it.

Not fancy, not perfect. Just *thoughtful*.
