# Refining Your Processing Sketch: Moving Toward Responsive & Clean Code

Now that you have your patterns *working*, the next phase is about making your code **cleaner, more flexible, and easier to understand**. This is what separates “it runs” code from “I understand how to control this” code.

This is **not** about making everything perfect. It’s about taking *one step* toward clarity.


## What You Likely Have Right Now

- Many numbers typed directly into `rect()`, `circle()`, and `line()`.
- Lots of repeated values like `200`, `40`, `20`, etc.
- Shapes positioned using absolute pixel numbers (e.g., `line(200, 0, 200, 200)`).

This works, but it makes your code harder to adjust later. If the canvas size changes, or if you wanted to move a design, you would need to rewrite many numbers.


## What We Want to Start Doing

- Replace *repeated numbers* with **variables** that state meaning and intent.
- Think **“draw relative to the section”** rather than using fixed coordinates.
- Use **expressions** instead of magic numbers.  
  For example:  
  Instead of hard-coding `200`, consider `width / 3` or `height / 2`.
- Use **variables** to describe colour changes, rather than hiding meaning in the math.  
  For example:  
  Instead of `fill(i * 12);` try something like `float shade = i * shadeStep; fill(shade);`  
  (where you choose and name a variable like `shadeStep` to make the intent of the expressioni clear).

You **do not** need to solve everything at once. Start with one design and take it through the following levels:

## Refactor Stages (Choose Your Stage)

| Stage | Goal | Example (conceptual) |
|:-----:|------|----------------------|
| **1** | Replace repeated numbers with a variable. | `float barWidth = 20;` instead of typing `20` many times. |
| **2** | Group numbers that describe the section into variables. | `float sectorW = width / 3; float sectorH = height / 2;` |
| **3** | Write your shapes **relative to the sector’s origin** rather than absolute coordinates. | `rect(xOrigin + n*barWidth, yOrigin, ...)` |
| **4** | Make your design adjust automatically when the canvas size changes. | No hard-coded values: all sizes derive from `width`, `height`, or variables that *derive* from them. |

Pick **one** of your patterns and try to improve it **one stage at a time**.

You do **not** need to make every design responsive — just one is enough for Level 4.

## Hints While Refactoring

- Look for a number that repeats **3+ times** and consider making it a variable.
- If two numbers are linked (e.g., changing one would require changing the other), they might be derived from `width` or `height`.
- If your pattern is drawn at `(200, 0)`, ask:  
  *What would change if I instead drew it starting at `(0,0)`?*  
  Once it works at `(0,0)`, shifting it to another sector is easy. Just add an offset for the origin.

Try practicing with the idea:

```java
float startX = 200;
float startY = 0;
```

Then draw your entire pattern *relative* to those. This is how we "move the canvas" without rewriting code.

## Why Do This?

- Because **code is never finished**. Not even for professional developers.  
- You will always revisit and improve things.  
- This step hones the skill of looking at your own work and making it clearer.

Your future self will thank you!