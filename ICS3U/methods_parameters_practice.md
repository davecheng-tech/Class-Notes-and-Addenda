# Practice Problems: Methods with Parameters

These problems combine **looping logic** with **method parameters**. Each method takes one or more values as input and produces output via `System.out.print()` or `System.out.println()`.

**Note:** You are **not** writing return statements yet — methods print their results directly to the console.

**Scaffolding approach:**
- **Problems 1–8:** Method header is provided; write the method body.
- **Problems 9–15:** Write the full method header and body.

Use a separate `.java` file for each problem in CodeHS Sandbox. Comment out method calls in `run()` until you are ready to test.

---

## Problem 1 — Count Up From a Starting Number

Write a method that prints numbers from a given starting point up to 10.

```java
public class Problem1 extends ConsoleProgram {
    public void run() {
        countUpFrom(7);
        System.out.println();
        countUpFrom(3);
    }

    private void countUpFrom(int start) {
        // TODO
    }
}
```

**Expected Output:**
```
7 8 9 10
3 4 5 6 7 8 9 10
```

---

## Problem 2 — Count Down From a Number

Write a method that prints numbers from a given starting point down to 1, then prints `Blastoff!`.

```java
public class Problem2 extends ConsoleProgram {
    public void run() {
        countDown(5);
        System.out.println();
        countDown(3);
    }

    private void countDown(int start) {
        // TODO
    }
}
```

**Expected Output:**
```
5 4 3 2 1
Blastoff!
3 2 1
Blastoff!
```

---

## Problem 3 — Print a Line of Dashes

Write a method that prints a line made of `-` characters, repeated `n` times.

```java
public class Problem3 extends ConsoleProgram {
    public void run() {
        printDashes(8);
        System.out.println("Middle");
        printDashes(12);
    }

    private void printDashes(int length) {
        // TODO
    }
}
```

**Expected Output:**
```
--------
Middle
------------
```

---

## Problem 4 — Print the Phrase Repeatedly

Write a method that prints a given phrase a specified number of times, each on a new line.

```java
public class Problem4 extends ConsoleProgram {
    public void run() {
        printPhrase("Hello", 3);
        System.out.println();
        printPhrase("Code", 2);
    }

    private void printPhrase(String phrase, int times) {
        // TODO
    }
}
```

**Expected Output:**
```
Hello
Hello
Hello

Code
Code
```

---

## Problem 5 — Left-Aligned Triangle of Stars

Write a method that prints a left-aligned triangle of `*` characters with a given height.

```java
public class Problem5 extends ConsoleProgram {
    public void run() {
        printTriangle(4);
    }

    private void printTriangle(int height) {
        // TODO
    }
}
```

**Expected Output:**
```
*
**
***
****
```

---

## Problem 6 — Rectangle of Characters

Write a method that prints a rectangle made of a given character with specified width and height.

```java
public class Problem6 extends ConsoleProgram {
    public void run() {
        printRectangle('#', 6, 3);
        System.out.println();
        printRectangle('+', 4, 2);
    }

    private void printRectangle(char symbol, int width, int height) {
        // TODO
    }
}
```

**Expected Output:**
```
######
######
######

++++
++++
```

---

## Problem 7 — Count From a to b

Write a method that prints all numbers from `start` to `end` inclusive, separated by spaces. If `start > end`, print them in reverse order.

```java
public class Problem7 extends ConsoleProgram {
    public void run() {
        printRange(3, 7);
        System.out.println();
        printRange(10, 6);
    }

    private void printRange(int start, int end) {
        // TODO
    }
}
```

**Expected Output:**
```
3 4 5 6 7
10 9 8 7 6
```

---

## Problem 8 — Multiplication Table (Single Number)

Write a method that prints the multiplication table for a given number from 1 to 10.

```java
public class Problem8 extends ConsoleProgram {
    public void run() {
        printMultTable(7);
        System.out.println();
        printMultTable(3);
    }

    private void printMultTable(int num) {
        // TODO
    }
}
```

**Expected Output:**
```
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
7 × 4 = 28
7 × 5 = 35
7 × 6 = 42
7 × 7 = 49
7 × 8 = 56
7 × 9 = 63
7 × 10 = 70

3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15
3 × 6 = 18
3 × 7 = 21
3 × 8 = 24
3 × 9 = 27
3 × 10 = 30
```

---

## Problem 9 — Coordinate Grid

Write a method that prints coordinates `(row, col)` in a grid with specified rows and columns.

```java
public class Problem9 extends ConsoleProgram {
    public void run() {
        // printGrid(3, 5);
        // System.out.println();
        // printGrid(2, 4);
    }
}
```

**Expected Output (for `printGrid(3, 5)`):**
```
(1,1) (1,2) (1,3) (1,4) (1,5)
(2,1) (2,2) (2,3) (2,4) (2,5)
(3,1) (3,2) (3,3) (3,4) (3,5)
```

---

## Problem 10 — Checkerboard Pattern

Write a method that prints an alternating `X` and `O` checkerboard pattern with a specified size.

```java
public class Problem10 extends ConsoleProgram {
    public void run() {
        // printCheckerboard(4);
        // System.out.println();
        // printCheckerboard(6);
    }
}
```

**Expected Output (for `printCheckerboard(4)`):**
```
XOXO
OXOX
XOXO
OXOX
```

---

## Problem 11 — Right-Aligned Triangle

Write a method that prints a right-aligned triangle of `*` characters with a given height. Rows should be padded with spaces on the left.

```java
public class Problem11 extends ConsoleProgram {
    public void run() {
        // printRightTriangle(5);
    }
}
```

**Expected Output (for `printRightTriangle(5)`):**
```
    *
   **
  ***
 ****
*****
```

---

## Problem 12 — Hollow Rectangle

Write a method that prints a hollow rectangle using `*` on the border and spaces inside. The dimensions are specified by width and height.

```java
public class Problem12 extends ConsoleProgram {
    public void run() {
        // printHollowRect(6, 4);
        // System.out.println();
        // printHollowRect(5, 3);
    }
}
```

**Expected Output (for `printHollowRect(6, 4)`):**
```
******
*    *
*    *
******
```

---

## Problem 13 — Diagonal Line

Write a method that prints a diagonal line of `*` characters. A `*` appears only where `row == column`. The size is specified by a parameter.

```java
public class Problem13 extends ConsoleProgram {
    public void run() {
        // printDiagonal(4);
        // System.out.println();
        // printDiagonal(5);
    }
}
```

**Expected Output (for `printDiagonal(4)`):**
```
*
 *
  *
   *
```

---

## Problem 14 — Centered Pyramid

Write a method that prints a centered pyramid of `*` characters. Each row should be centered relative to the bottom row. The height is specified by a parameter.

```java
public class Problem14 extends ConsoleProgram {
    public void run() {
        // printPyramid(5);
    }
}
```

**Expected Output (for `printPyramid(5)`):**
```
    *
   ***
  *****
 *******
*********
```

---

## Problem 15 — Multiplication Table (Grid)

Write a method that prints an `n × n` multiplication table where `n` is specified by a parameter. Format the table so columns line up neatly.

```java
public class Problem15 extends ConsoleProgram {
    public void run() {
        // printMultGrid(4);
        // System.out.println();
        // printMultGrid(5);
    }
}
```

**Expected Output (for `printMultGrid(4)`):**
```
1  2  3  4
2  4  6  8
3  6  9  12
4  8  12 16
```

**Formatting Hint:** Use `System.out.printf("%3d ", value)` to right-align numbers in a 3-character width, or use `String.format()` to build the output string before printing.

---

## Reminders

1. **Test incrementally:** Uncomment one method call at a time and verify output before moving to the next problem.

2. **Use loops inside methods:** Every method (except perhaps simple variable assignments) will contain a `for` or `while` loop.

3. **Combine parameters:** Many problems use multiple parameters — ensure you understand how each one affects the output.

4. **Nested loops for grids:** Problems involving grids (like checkerboards and coordinate tables) require nested loops.

5. **Edge cases:** Consider what happens with edge cases (e.g., height = 1, width = 1). Your code should handle them gracefully.

6. **Spacing and formatting:** Pay careful attention to spaces and line breaks — the expected output is precise.
