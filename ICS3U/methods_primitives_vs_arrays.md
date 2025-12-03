# Understanding How Methods Handle Primitives vs Arrays

This note is designed to clarify one of the most confusing behaviours in Java for new programmers:

**Why modifying a primitive parameter does nothing, but modifying an array *does* change the original.**

Java always uses *pass‑by‑value*, but what gets copied depends on the type:

- **Primitives** → Java copies the *value*
- **Arrays/objects** → Java copies the *reference* (both variables point to the same array)

The two demonstrations below illustrate this difference.


## 1. Primitive Parameter - `int`

### Goal
Show that changing an `int` parameter inside a method does **not** change the original variable.

### Code

```java
public class PrimitiveDemo extends ConsoleProgram {
    public void run() {
        int number = 5;

        System.out.println("Before increaseNum: " + number);

        increaseNum(number, 3);

        System.out.println("After increaseNum:  " + number);
    }

    // Tries to add 'incr' to the parameter
    public void increaseNum(int myNumber, int incr) {
        myNumber = myNumber + incr;  // modifies only the local copy
        System.out.println("Inside increaseNum: " + myNumber);
    }
}
```

### What You Will See

```
Before increaseNum: 5
Inside increaseNum: 8
After increaseNum:  5
```

### Explanation
- `number` is a **primitive (int)**.
- Java copies the *value* `5` into `myNumber`.
- Changing `myNumber` does **not** change `number` in `run()`.

> For primitives, methods receive a *copy of the value*.  
> Changing the copy does nothing to the original variable.


<br>

## 2. Array Parameter - `int[]`

### Goal
Show that changing an element of an array inside a method **does** change the original array.

### Code

```java
public class ArrayDemo extends ConsoleProgram {
    public void run() {
        int[] numbers = {5, 10, 15};

        System.out.println("Before increaseFirst: " + numbers[0]);

        increaseFirst(numbers, 3);

        System.out.println("After increaseFirst:  " + numbers[0]);
    }

    // Adds 'incr' to the first element of the array
    public void increaseFirst(int[] myArray, int incr) {
        myArray[0] = myArray[0] + incr;  // modifies the shared array object
        System.out.println("Inside increaseFirst: " + myArray[0]);
    }
}
```

### What You Will See

```
Before increaseFirst: 5
Inside increaseFirst: 8
After increaseFirst:  8
```

### Explanation
- `numbers` is an **array**, which is not a primitive in Java.
- Java copies the *reference* to the array.
- Both `numbers` and `myArray` point to the **same array in memory**.
- Changing `myArray[0]` updates the underlying array, which `numbers` also sees.

> For arrays and objects, methods receive a *copy of the reference*.  
> Both variables point to the same array, so changes affect the original.

<br>

## 3. Side‑by‑Side Summary

```java
// PRIMITIVE
public void increaseNum(int myNumber, int incr) {
    myNumber = myNumber + incr;  // only local copy changes
}

// ARRAY
public void increaseFirst(int[] myArray, int incr) {
    myArray[0] = myArray[0] + incr;  // shared object changes
}
```

**Final takeaway:**  
- Primitives → changes do **not** persist  
- Arrays → changes **do** persist  

Understanding this behaviour is essential when designing helper methods that clean, transform, or update data stored in arrays.
