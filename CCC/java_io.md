# A Note on Java Input / Output for CCC

This note is for students who want to use Java for the CCC and learned the language in our ICS3U Computer Science Grade 11 classes.

You might have seen `ConsoleProgram` or `ARC` in Grade 11. These are helper libraries that simplify certain tasks for learning, particularly user input.

For the CCC, **these methods do not exist**.

If you choose Java, you must write **native Java**, i.e., without these helper libraries.

This document shows you how to bridge that gap properly using plain or "native" Java.

## 1. What You Are Used To (from ICS3U)

Many of you are used to files that look like this:

```java
public class Main extends ConsoleProgram {
    public void run() {
        int x = readInt("");
        System.out.println(x);
    }
}
```

Why this worked:
- `readInt()` was provided for you
- input setup was hidden
- Java was simplified for learning

For CCC, this code will not compile. You'll see an error about the missing `readInt()` method.

## 2. What Changes for Native Java (used for CCC)

### Required Native Java Boilerplate (basic)

Every CCC Java program should start like this:

```java
public class Main {
    public static void main(String[] args) {
        // your code goes here
    }
}
```

You must have:
- a class named `Main`
- a `public static void main(String[] args)` method

Nothing runs without this.

### Required Native Java Boilerplate for User Input (these examples)

If your CCC Java program requires getting user input (very likely), then this should be the starting template:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // your code goes here
    }
}
```

Note these additions:
- the `import java.util.Scanner;` at the top 
- a line creating a `Scanner` variable (object) named `sc`

## 3. Example: Reading a Single Integer

### Problem

Read one integer and print its value when doubled.

### ICS3U Solution (ConsoleProgram)

```java
public class Main extends ConsoleProgram {
    public void run() {
        int x = readInt("");
        System.out.println(x * 2);
    }
}
```

### Native Java Solution (Scanner)

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        System.out.println(x * 2);
    }
}
```

What changed:

- `readInt("")` became `sc.nextInt()`
- input setup is now visible


## 4. Example: Reading Multiple Integers (on Multiple Lines)

### Problem

Read three integers and print their sum.

### ICS3U Solution (ConsoleProgram)

```java
public class Main extends ConsoleProgram {
    public void run() {
        int a = readInt("");
        int b = readInt("");
        int c = readInt("");

        System.out.println(a + b + c);
    }
}
```

### Native Java Solution (Scanner)

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(a + b + c);
    }
}
```

Key idea:

- Each call to `nextInt()` reads the next number in order.
- It **does not matter** whether they are on separate lines or one line.


## 5. Example: Mixing Integers and Symbols

### Problem

Build a simple calculator.

Input format:

- first integer
- second integer
- operator (`+`, `-`, `*`, `/`)

Example input:

```
8
3
*
```

### Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        String op = sc.next();

        if (op.equals("+")) {
            System.out.println(a + b);
        } else if (op.equals("-")) {
            System.out.println(a - b);
        } else if (op.equals("*")) {
            System.out.println(a * b);
        } else if (op.equals("/")) {
            System.out.println(a / b);
        }
    }
}
```

New concept:

- `sc.next()` reads the next token as a String.
- Even a single character like `+` is read as a String.
- We compare strings using `.equals()`.


## 6. Example: Reading an Entire Line of Text

In this example, we move beyond numbers.

### Problem

Read one full line of text and print its length.

Example input:

```
Hello World
```

### Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String line = sc.nextLine();
        System.out.println(line.length());
    }
}
```

Important difference:

- `next()` reads one token.
- `nextLine()` reads the entire line including spaces.

`Scanner` reads input as tokens separated by whitespace (spaces, tabs, or line breaks). `nextInt()` and `next()` stop reading when they hit whitespace.

## 7. Example: Mixing nextInt() and nextLine()

Mixing integer tokens and entire lines of text requires delicate handling.

### Problem

First read an integer N. Then read N lines of text.

Example input:

```
3
apple
banana
carrot
```

### Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();  // clear the leftover newline

        for (int i = 0; i < N; i++) {
            String word = sc.nextLine();
            System.out.println(word.toUpperCase());
        }
    }
}
```

Why the extra `nextLine()`?

Because:

- `nextInt()` reads the number
- it does NOT consume the trailing **newline** character (the line break)
- that newline character is still sitting in the input buffer
- the first `nextLine()` consume that leftover line break

More precisely:

- A newline is **not a token** but instead a **line break character**.
- `Scanner` uses whitespace as a delimiter when reading tokens.
- `nextInt()` stops reading at the delimiter but does not remove the rest of the line.

If you forget that extra `nextLine()`, your first string will be read as an empty line.

## 8. Example: Basic String Parsing

Now combine reading a line with analyzing characters.

### Problem

Read a string and count how many uppercase letters it contains.

Example input:

```
AbCdeFG
```

### Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (Character.isUpperCase(ch)) {
                count++;
            }
        }

        System.out.println(count);
    }
}
```

## 9. A Note on Performance (Scanner vs BufferedReader)

For CCC Junior, `Scanner` is completely sufficient.

You may hear that `BufferedReader` is "faster." That is true in theory, but performance only matters when reading very large inputs (typically hundreds of thousands of values).

At the CCC Junior level, input sizes are modest and algorithm design matters far more than input speed.

If you are comfortable with `Scanner`, use it. Only consider `BufferedReader` in Senior-level problems where input size is extremely large.