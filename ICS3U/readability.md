# Writing Clear, Readable Code

Why does code quality matter? Isn't it enough that something "just works"?

- **Humans read code more than machines execute it.** Readable code is faster to understand, easier to debug, and simpler to improve.
- **Clarity reduces bugs.** When names and structure reveal intent, logic errors stand out.
- **Good habits scale.** Small programs turn into bigger ones. Style choices that seem optional at 20 lines become essential at 200.

<br>

## Core Principles

To write good code, you have to be willing to write bad code first. Clear, readable code comes from revising and improving your first attempt, not from getting it perfect the first time.

We can try to break this down to several core principles:

1. **Communicate intent.** Names and structure should reveal *what* the code is doing, not just *how*.
2. **Remove “magic numbers.”** Prefer named constants/variables that explain meaning.
3. **Be consistent.** Indentation, brace style, and naming conventions reduce cognitive load.
4. **Prefer simple, linear logic.** Fewer branches; avoid deeply nested `if`s when a clearer structure exists.
5. **DRY (“Don’t Repeat Yourself”) within your current toolkit.** Eliminate copy‑paste by using loops and helper variables. (Later we’ll use methods.)
6. **Validate inputs.** Defensive checks make programs robust.
7. **Leave a tidy trail.** Readable code is self-documenting. That said, there is still a place for minimal, useful comments aid understanding.

<br>

### 1) Naming: Make Purpose Obvious

#### Bad
```java
int a = readInt("width? ");
int b = readInt("height? ");
int c = a * b;
System.out.println(c);
```

#### Better
```java
int width = readInt("Width? ");
int height = readInt("Height? ");
int area = width * height;
System.out.println("Area = " + area);
```

Why it’s better:
- Names describe the role: `width`, `height`, `area`.
- Output label explains the number printed.

**Guideline:** Use nouns for data (`totalMarks`), verbs for actions (`printMenu`, when we later write methods), and booleans that read like yes/no (`isPrime`, `hasWon`).


<br>

### 2) Eliminate Magic Numbers

> *A magic number is a raw literal with no explanation.*

#### Processing example (original)
```java
for (int row = 0; row < 3; row++) {
    for (int col = 0; col < 3; col++) {
        ellipse(50 + col * 100, 50 + row * 100, 40, 40);
    }
}
```

#### Improved
```java
int rows = 3;
int cols = 3;
int circleDiameter = 40;
int spacing = 100;
int margin = 50;

for (int row = 0; row < rows; row++) {
    for (int col = 0; col < cols; col++) {
        float x = margin + col * spacing;
        float y = margin + row * spacing;
        ellipse(x, y, circleDiameter, circleDiameter);
    }
}
```

In general, when a number has a meaning (e.g., margin, spacing, maximum attempts), give it a name.

<br>

### 3) Use Helper Variables to Explain Expressions

#### Before
```java
double bmi = weightKg / (heightM * heightM);
System.out.println(bmi);
```

#### After
```java
double heightSquared = heightM * heightM;
double bmi = weightKg / heightSquared;
System.out.println("BMI = " + bmi);
```

Helper variables act like “inline documentation” and provide convenient debug points.

<br>

### 4) Input Validation: Guard the Edges

#### Before
```java
int mark = readInt("Enter mark: ");
System.out.println("Recorded: " + mark);
```

#### After (robust)
```java
int mark = readInt("Enter mark (0–100): ");
while (mark < 0 || mark > 100) {
    System.out.println("Invalid mark.");
    mark = readInt("Enter mark (0–100): ");
}
System.out.println("Recorded: " + mark);
```

Validation protects the rest of your program from bad states.

<br>

### 5) Loop Patterns You Should Recognize

#### Counted loop (known repetitions)
```java
for (int i = 0; i < 10; i++) {
    // repeat 10 times 
}
```

#### Sentinel loop (unknown repetitions; stop on signal)
```java
int total = 0;
int n = readInt("Enter number (0 to stop): ");
while (n != 0) {
    total += n;
    n = readInt("Enter number (0 to stop): ");
}
System.out.println("Total = " + total);
```

#### Validation loop (repeat until input is valid)
```java
double price = readDouble("Price (>= 0): ");
while (price < 0) {
    System.out.println("Try again.");
    price = readDouble("Price (>= 0): ");
}
```

Recognizing common loop patterns can reduce cognitive load.

<br>

### 6) Conditionals: Prefer Clear, Direct Logic

#### Over‑nested
```java
if (age >= 0) {
    if (age < 13) {
        System.out.println("Child");
    } else {
        if (age < 18) {
            System.out.println("Teen");
        } else {
            System.out.println("Adult");
        }
    }
}
```

#### Flatter and clearer
```java
if (age < 0) {
    System.out.println("Invalid age");
} else if (age < 13) {
    System.out.println("Child");
} else if (age < 18) {
    System.out.println("Teen");
} else {
    System.out.println("Adult");
}
```

**Technique:** Reject invalid cases early, then handle the normal path.


<br>

### 7) Layout & Formatting

- **Indent with 2 or 4 spaces** consistently (VS Code can format on save).
- **Brace style:** pick one and stick to it.
- **Whitespace:** add blank lines between logical sections.
- **Line length:** prefer readable lines under ~100 chars.

```java
// Good vertical spacing
System.out.println("Menu");
System.out.println("1) Coffee");
System.out.println("2) Tea");

int choice = readInt("Choose: ");
System.out.println();

if (choice == 1) {
  System.out.println("Coffee selected.");
} else if (choice == 2) {
  System.out.println("Tea selected.");
} else {
  System.out.println("Invalid.");
}
```


<br>

### 8) Comments: Useful but Minimal

- **What to comment:** the *why* of non‑obvious decisions, data formats, constraints.
- **What not to comment:** code that already states the obvious.

#### OK
```java
// Cap the speed at residential limit to simplify simulation
if (speed > 50) speed = 50;
```

#### Not helpful
```java
// add 1 to i
i = i + 1;
```

Prefer code that reads well without comments; add a brief note only where necessary.



### 9) Stepwise Improvement: A Refactoring Walkthrough

We’ll improve a student submission that draws rows of boxes in Processing.

#### Version A (works, but repeated)
```java
size(400, 200);

rect(20, 20, 40, 40);
rect(80, 20, 40, 40);
rect(140, 20, 40, 40);
rect(200, 20, 40, 40);
rect(260, 20, 40, 40);
```

**Issues:** Repetition, magic numbers, hard to scale.

#### Version B (loop introduced)
```java
size(400, 200);

for (int i = 0; i < 5; i++) {
  rect(20 + i * 60, 20, 40, 40);
}
```

**Better:** Loop eliminates repetition, but still some unexplained numbers.

#### Version C (named values; easier to change)
```java
size(400, 200);

int boxes = 5;
int boxSize = 40;
int spacing = 60;
int marginLeft = 20;
int marginTop = 20;

for (int i = 0; i < boxes; i++) {
  int x = marginLeft + i * spacing;
  int y = marginTop;
  rect(x, y, boxSize, boxSize);
}
```

**Result:** Clear, adjustable, and communicates intent.


<br>

### 10) Practical Patterns to Reuse

#### Totals and Counts
```java
int count = 0;
int sum = 0;

int n = readInt("Enter number (-1 to stop): ");
while (n != -1) {
  sum += n;
  count++;
  n = readInt("Enter number (-1 to stop): ");
}

System.out.println("Average = " + (count == 0 ? 0 : (double) sum / count));
```

#### Min/Max Tracking
```java
int n = readInt("First number: ");
int min = n;
int max = n;

n = readInt("Next number (0 to stop): ");
while (n != 0) {
  if (n < min) min = n;
  if (n > max) max = n;
  n = readInt("Next number (0 to stop): ");
}
System.out.println("Min=" + min + ", Max=" + max);
```


<br>

### 11) Debugging: Make Bugs Visible

- Print intermediate values with labels.
- Change one thing at a time.
- Use small test cases first.

```java
System.out.println("[DEBUG] i=" + i + ", j=" + j + ", sum=" + sum);
```

Delete or comment out debug prints before final submission.


<br>

### 12) Mini‑Rubric for “Good Code” in ICS3U

| Category | 0–1 | 2–3 | 4–5 |
|---|---|---|---|
| **Naming** | Vague names | Mostly clear; a few vague | Clear, consistent, purpose‑revealing |
| **Magic Numbers** | Many | Some remain | Eliminated or justified with constants/vars |
| **Structure** | Repetition; nested confusion | Some loops/validation | Clean patterns; DRY within current tools |
| **Formatting** | Inconsistent | Mostly consistent | Consistent, readable, professional |
| **Comments** | None or noisy | Useful in places | Brief, high‑value, explains *why* |


<br>

### 13) Quick Checklist (before you submit)

- [ ] Did I remove magic numbers by naming them?
- [ ] Do my variable names reveal purpose?
- [ ] Are loops and conditionals written in a standard, recognizable pattern?
- [ ] Is the output labelled and user‑friendly?
- [ ] Are the inputs validated?
- [ ] Is the code formatted consistently?
- [ ] Did I remove debug prints?


<br>

## Practice — Refactor & Improve

**1) Replace Magic Numbers (Processing)**  
Draw a 4×3 grid of circles with a custom margin and spacing. Use named variables so the layout can change by editing *one* line.

**2) Validate Score Input (ConsoleProgram)**  
Read a score out of 30. Keep asking until input is in range. Compute percent out of 100 with a clear label.

**3) Clean Conditionals**  
Rewrite a nested `if` that classifies BMI into “Underweight/Normal/Overweight/Obese” using early rejection for invalid input and a flat `if/else if/else` chain.

**4) DRY with Loops**  
A student printed 20 dashes by copy‑pasting `System.out.print("-");` 20 times. Replace it with a loop and a named constant for the count.

**5) Totals & Counts**  
Read daily step counts until the user enters `-1`. Print total, average, and the day with the max steps (track index). Use clear names and labels.


<br>

## Stretch (Preview of Later Topics)

- **Helper methods** (later in the course) let you name *chunks* of logic (e.g., `drawGrid`, `isValidMark`), further improving readability.
- **Enums and classes** (ICS4U) express richer meaning than raw ints and strings.

For now, master the basics above. They apply to every assignment you’ll write this semester.
