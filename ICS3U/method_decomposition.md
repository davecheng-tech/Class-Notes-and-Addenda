# Processing: Writing Clean Code and Method Decomposition

When programs grow in size, writing everything in one giant block of code becomes messy, repetitive, and hard to understand.  

Good programmers break large tasks into *smaller, meaningful methods* that do one job each. This is called **method decomposition**.

Consider the Processing program below. When run, it randomly selects one of three country flags to display: 

- Poland (two horizontal bars, white over red), 
- Ukraine (two horizontal bars, blue over yellow), or
- Canada (vertical red/white/red bars, simplified red maple leaf in the middle).

![flags](/.media/image-method_decomposition-01.png)

### Original Version

```java
import processing.core.PApplet;

public class Sketch extends PApplet {
    public static void main(String[] args) {
        PApplet.main("Sketch");
    }

    @Override
    public void settings() {
        size(600, 400);
    }

    @Override
    public void setup() {
        background(255);

        int choice = (int) random(3);

        if (choice == 0) {
            // Polish flag (white over red)
            fill(255);
            rect(0, 0, width, height / 2);
            fill(200, 0, 0);
            rect(0, height / 2, width, height / 2);

        } else if (choice == 1) {
            // Ukraine flag (blue over yellow)
            fill(0, 87, 183);
            rect(0, 0, width, height / 2);
            fill(255, 215, 0);
            rect(0, height / 2, width, height / 2);

        } else {
            // Canada flag
            fill(255, 0, 0);
            rect(0, 0, width / 4, height);
            rect(3 * width / 4, 0, width / 4, height);

            fill(255);
            rect(width / 4, 0, width / 2, height);

            // Simplified maple leaf shape
            fill(255, 0, 0);
            beginShape();
            vertex(width / 2, 80);
            vertex(width / 2 - 20, 160);
            vertex(width / 2 - 60, 160);
            vertex(width / 2 - 30, 220);
            vertex(width / 2 - 50, 320);
            vertex(width / 2,      260);
            vertex(width / 2 + 50, 320);
            vertex(width / 2 + 30, 220);
            vertex(width / 2 + 60, 160);
            vertex(width / 2 + 20, 160);
            endShape(CLOSE);
        }
    }
}
```

### What's Going On Here?

A few important observations:

- `int choice = (int) random(3);` picks a random integer 0, 1, or 2 (each equally likely).  
  - `choice == 0` → draw the Polish flag  
  - `choice == 1` → draw the Ukrainian flag  
  - `choice == 2` → draw the Canadian flag  

- All the drawing logic for **all three flags** is jammed into one big `if / else if / else` block inside `setup()`.

This kind of long, tangled block is often called **spaghetti code**:

- It's hard to scan and understand quickly.  
- If you want to change one flag, you have to hunt through the whole block.  
- There is repetition (e.g., repeated `fill()` and `rect()` patterns).  
- The maple leaf is hard-coded with a bunch of magic numbers inside `setup()`.

A natural next step is to split this logic into separate methods.

<br>

## First Refactor: One Method Per Flag

In the first refactor, we move each flag into its own method. We are not yet fixing the maple leaf; we're just organizing the code so each method has a clear responsibility.

```java
import processing.core.PApplet;

public class Sketch extends PApplet {
    public static void main(String[] args) {
        PApplet.main("Sketch");
    }

    @Override
    public void settings() {
        size(600, 400);
    }

    @Override
    public void setup() {
        background(255);

        int choice = (int) random(3);

        if (choice == 0) {
            drawPolandFlag();
        } else if (choice == 1) {
            drawUkraineFlag();
        } else {
            drawCanadaFlag();
        }
    }

    /**
     * Draws the Polish flag (white over red).
     */
    private void drawPolandFlag() {
        fill(255);
        rect(0, 0, width, height / 2);
        fill(200, 0, 0);
        rect(0, height / 2, width, height / 2);
    }

    /**
     * Draws the Ukrainian flag (blue over yellow).
     */
    private void drawUkraineFlag() {
        fill(0, 87, 183);
        rect(0, 0, width, height / 2);
        fill(255, 215, 0);
        rect(0, height / 2, width, height / 2);
    }

    /**
     * Draws the Canadian flag with a simple leaf shape.
     */
    private void drawCanadaFlag() {
        // Red side bars
        fill(255, 0, 0);
        rect(0, 0, width / 4, height);
        rect(3 * width / 4, 0, width / 4, height);

        // White centre
        fill(255);
        rect(width / 4, 0, width / 2, height);

        // Simplified maple leaf shape
        fill(255, 0, 0);
        beginShape();
        vertex(width / 2, 80);
        vertex(width / 2 - 20, 160);
        vertex(width / 2 - 60, 160);
        vertex(width / 2 - 30, 220);
        vertex(width / 2 - 50, 320);
        vertex(width / 2,      260);
        vertex(width / 2 + 50, 320);
        vertex(width / 2 + 30, 220);
        vertex(width / 2 + 60, 160);
        vertex(width / 2 + 20, 160);
        endShape(CLOSE);
    }
}
```

### Why This Is Better (But Not Perfect)

This version is already easier to work with:

- `setup()` is much shorter and easier to read.  
- Because of the above, the logic of 3 random choices is easy to see.
- Each flag is drawn in its own clearly named method.  
- If you want to adjust just the Ukrainian flag, you can jump straight to `drawUkraineFlag()`.

However:

- The Poland and Ukraine methods are almost identical. There is a lot of *repeated code*.
- The Canada method still has spaghetti: stripes and maple leaf drawing are all tangled together.  
- The maple leaf is still a lump of [magic numbers](https://davecheng-tech.github.io/Class-Notes-and-Addenda/ICS3U/style#magic-numbers-vs-meaning) inside a long method.

We can do better.

<br>

## Second Refactor: Reusable Methods and Clean Structure

Now that the code is split into one method per flag, we can clean it up further by removing repetition and improving structure. The goal is to write code that is **modular**, **readable**, and **easy to update** later.

In this version, we:

- Create a **general-purpose method** to draw any two‑colour horizontal flag (useful for Poland, Ukraine, and many more).
- Break the Canadian flag into **two separate methods**:
  - one for drawing the red/white/red background stripes  
  - one for drawing the maple leaf (now in its own method with parameters for position, so it can be reused or moved easily)
- Demonstrate **method composition**, i.e., larger tasks calling smaller helper methods.

We also include Javadocs to properly document each method’s purpose.

```java
import processing.core.PApplet;

public class Sketch extends PApplet {
    public static void main(String[] args) {
        PApplet.main("Sketch");
    }

    @Override
    public void settings() {
        size(600, 400);
    }

    @Override
    public void setup() {
        background(255);

        int choice = (int) random(3);

        if (choice == 0) {
            // Poland: white over red
            drawBicolorHorizontalFlag(255, 255, 255, 200, 0, 0);
        } else if (choice == 1) {
            // Ukraine: blue over yellow
            drawBicolorHorizontalFlag(0, 87, 183, 255, 215, 0);
        } else {
            drawCanadaFlag();
        }
    }

    /**
     * Draws a simple horizontal two-colour flag that fills the entire window.
     *
     * @param topR    red component of the top colour (0–255)
     * @param topG    green component of the top colour (0–255)
     * @param topB    blue component of the top colour (0–255)
     * @param bottomR red component of the bottom colour (0–255)
     * @param bottomG green component of the bottom colour (0–255)
     * @param bottomB blue component of the bottom colour (0–255)
     */
    private void drawBicolorHorizontalFlag(int topR, int topG, int topB,
                                           int bottomR, int bottomG, int bottomB) {
        // Top half
        fill(topR, topG, topB);
        rect(0, 0, width, height / 2);

        // Bottom half
        fill(bottomR, bottomG, bottomB);
        rect(0, height / 2, width, height / 2);
    }

    /**
     * Draws the Canadian flag with red side bars and a centred maple leaf.
     * This method delegates to helper methods for the stripes and the leaf.
     */
    private void drawCanadaFlag() {
        drawCanadaStripes();
        drawMapleLeaf();
    }

    /**
     * Draws the red and white background stripes for the Canadian flag.
     * Red vertical bars are placed on the left and right; the centre is white.
     */
    private void drawCanadaStripes() {
        // Red side bars
        fill(255, 0, 0);
        rect(0, 0, width / 4, height);
        rect(3 * width / 4, 0, width / 4, height);

        // White centre
        fill(255);
        rect(width / 4, 0, width / 2, height);
    }

    /**
     * Draws a stylized maple leaf shape of fixed size and position.
     */
    private void drawMapleLeaf() {
        fill(255, 0, 0);
        beginShape();
        vertex(width / 2, 80);
        vertex(width / 2 - 20, 160);
        vertex(width / 2 - 60, 160);
        vertex(width / 2 - 30, 220);
        vertex(width / 2 - 50, 320);
        vertex(width / 2,      260);
        vertex(width / 2 + 50, 320);
        vertex(width / 2 + 30, 220);
        vertex(width / 2 + 60, 160);
        vertex(width / 2 + 20, 160);
        endShape(CLOSE);
    }
}
```

### Why This Version Is Better

This version is far more modular and maintainable:

- **Clear method decomposition**  
  - Each method does one well‑defined job.
  - `setup()` simply chooses a flag and calls a method — clean and readable.

- **Reduced repetition**  
  - Poland and Ukraine are now handled by the same general-purpose `drawBicolorHorizontalFlag(...)`.

- **Method composition**  
  - `drawCanadaFlag()` calls `drawCanadaStripes()` and `drawMapleLeaf(...)`.
  - The maple leaf is now *completely isolated*, making it easy to replace or upgrade.

- **Better maintainability**  
  - Want another horizontal two-colour flag? Just reuse `drawBicolorHorizontalFlag(...)`.
  - Want a more realistic leaf? Just focus on rewriting `drawMapleLeaf()`.

This is the goal of clean code: **short, focused, reusable methods** that are easy to understand and modify.

<br>

## Final Refactor: Dropping In a Better Maple Leaf

At this point, the program has been refactored into small, focused methods:

- `drawBicolorHorizontalFlag(...)` handles any two‑colour horizontal flag.
- `drawCanadaFlag()` is responsible only for “tell the helpers what to do”.
- `drawCanadaStripes()` draws the red–white–red background.
- `drawMapleLeaf(...)` draws the leaf at a fixed position and size.

Because the earlier refactor separated concerns so cleanly, it becomes very easy to **swap in a more accurate maple leaf shape** without touching any of the surrounding logic. The random choice code, the Canadian stripes, and the overall layout stay the same; only the *implementation detail* of `drawMapleLeaf(...)` changes.

Here is the final version with a proper maple leaf design using coordinates traced off an existing flag image. The method can place the flag anywhere on the canvas and uses a scale factor to adjust size:

![flags](/.media/image-method_decomposition-02.png)

And the code, changes on L57, now:

```
drawMapleLeaf(width / 2, height / 2, 0.35f);
```

and the method definition on L75 onward:


```java
import processing.core.PApplet;

public class Sketch extends PApplet {
    public static void main(String[] args) {
        PApplet.main("Sketch");
    }

    @Override
    public void settings() {
        size(600, 400);
    }

    @Override
    public void setup() {
        background(255);

        int choice = (int) random(3);

        if (choice == 0) {
            // Poland: white over red
            drawBicolorHorizontalFlag(255, 255, 255, 200, 0, 0);
        } else if (choice == 1) {
            // Ukraine: blue over yellow
            drawBicolorHorizontalFlag(0, 87, 183, 255, 215, 0);
        } else {
            drawCanadaFlag();
        }
    }

    /**
     * Draws a simple horizontal two-colour flag that fills the entire window.
     *
     * @param topR    red component of the top colour (0–255)
     * @param topG    green component of the top colour (0–255)
     * @param topB    blue component of the top colour (0–255)
     * @param bottomR red component of the bottom colour (0–255)
     * @param bottomG green component of the bottom colour (0–255)
     * @param bottomB blue component of the bottom colour (0–255)
     */
    private void drawBicolorHorizontalFlag(int topR, int topG, int topB,
                                           int bottomR, int bottomG, int bottomB) {
        // Top half
        fill(topR, topG, topB);
        rect(0, 0, width, height / 2);

        // Bottom half
        fill(bottomR, bottomG, bottomB);
        rect(0, height / 2, width, height / 2);
    }

    /**
     * Draws the Canadian flag with red side bars and a centred maple leaf.
     * This method delegates to helper methods for the stripes and the leaf.
     */
    private void drawCanadaFlag() {
        drawCanadaStripes();
        drawMapleLeaf(width / 2, height / 2, 0.35f);
    }

    /**
     * Draws the red and white background stripes for the Canadian flag.
     * Red vertical bars are placed on the left and right; the centre is white.
     */
    private void drawCanadaStripes() {
        // Red side bars
        fill(255, 0, 0);
        rect(0, 0, width / 4, height);
        rect(3 * width / 4, 0, width / 4, height);

        // White centre
        fill(255);
        rect(width / 4, 0, width / 2, height);
    }

    /**
     * Draws an accurate maple leaf centered at (cx, cy),
     * using a scale factor relative to the original traced coordinates.
     *
     * @param cx    center x-position
     * @param cy    center y-position
     * @param s     scale factor (1.0 = original size)
     */
    private void drawMapleLeaf(float cx, float cy, float s) {
        // This is the centre of mass of the original traced points
        final float CEN_X = 300;
        final float CEN_Y = 330;

        fill(255, 0, 0);

        beginShape();

        // Trace vertices relative to centre of maple leaf
        vertex(cx + (302 - CEN_X) * s, cy + (6   - CEN_Y) * s);
        vertex(cx + (362 - CEN_X) * s, cy + (111 - CEN_Y) * s);
        vertex(cx + (420 - CEN_X) * s, cy + (87  - CEN_Y) * s);
        vertex(cx + (387 - CEN_X) * s, cy + (267 - CEN_Y) * s);
        vertex(cx + (474 - CEN_X) * s, cy + (180 - CEN_Y) * s);
        vertex(cx + (488 - CEN_X) * s, cy + (227 - CEN_Y) * s);
        vertex(cx + (580 - CEN_X) * s, cy + (207 - CEN_Y) * s);
        vertex(cx + (552 - CEN_X) * s, cy + (311 - CEN_Y) * s);
        vertex(cx + (590 - CEN_X) * s, cy + (332 - CEN_Y) * s);
        vertex(cx + (444 - CEN_X) * s, cy + (457 - CEN_Y) * s);
        vertex(cx + (461 - CEN_X) * s, cy + (511 - CEN_Y) * s);
        vertex(cx + (312 - CEN_X) * s, cy + (496 - CEN_Y) * s);
        vertex(cx + (312 - CEN_X) * s, cy + (656 - CEN_Y) * s);
        vertex(cx + (290 - CEN_X) * s, cy + (657 - CEN_Y) * s);
        vertex(cx + (294 - CEN_X) * s, cy + (495 - CEN_Y) * s);
        vertex(cx + (148 - CEN_X) * s, cy + (513 - CEN_Y) * s);
        vertex(cx + (162 - CEN_X) * s, cy + (462 - CEN_Y) * s);
        vertex(cx + (15  - CEN_X) * s, cy + (331 - CEN_Y) * s);
        vertex(cx + (54  - CEN_X) * s, cy + (315 - CEN_Y) * s);
        vertex(cx + (27  - CEN_X) * s, cy + (206 - CEN_Y) * s);
        vertex(cx + (116 - CEN_X) * s, cy + (226 - CEN_Y) * s);
        vertex(cx + (132 - CEN_X) * s, cy + (177 - CEN_Y) * s);
        vertex(cx + (216 - CEN_X) * s, cy + (265 - CEN_Y) * s);
        vertex(cx + (191 - CEN_X) * s, cy + (87  - CEN_Y) * s);
        vertex(cx + (246 - CEN_X) * s, cy + (114 - CEN_Y) * s);

        endShape(CLOSE);
    }
}
```

In other words, **good method decomposition made this upgrade almost trivial**: instead of rewriting the whole program, we only had to improve one well‑named helper method and leave the rest of the design untouched.
