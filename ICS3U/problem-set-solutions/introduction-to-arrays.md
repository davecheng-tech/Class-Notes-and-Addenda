# Introduction to Arrays: Practice Problems - Annotated Solutions

Each solution includes explanations where helpful.

## Problem 1 — First and Last

Using `.length - 1` ensures we always get the last element no matter how large the array becomes.

```java
public void run() {
    int[] cans = {12, 25, 31, 18, 40};

    System.out.println("First: " + cans[0]);
    System.out.println("Last: " + cans[cans.length - 1]);
}
```


## Problem 2 — Favourite Songs

The middle element should be computed as `length / 2` so it still works for different array sizes.

```java
public void run() {
    String[] songs = {"Dreams", "Everlong", "Numb", "Halo", "Believer"};

    int middle = songs.length / 2;
    System.out.println("Middle song: " + songs[middle]);
}
```


## Problem 3 — Menu Prices

The second-last element is always at index `length - 2`. This avoids hardcoding numeric positions.

```java
public void run() {
    double[] prices = {9.99, 12.49, 7.50, 6.99, 14.25, 10.00};

    System.out.println("Second-last price: " + prices[prices.length - 2]);
}
```


## Problem 4 — Replace a Value

When printing all array elements, we can use an index-based loop from `0` to `length - 1`.

```java
public void run() {
    int[] nums = {4, 8, 15, 16, 23, 42};

    nums[2] = 99;  // replace index 2

    for (int i = 0; i < nums.length; i++) {
        System.out.println("nums[" + i + "] = " + nums[i]);
    }
}
```


## Problem 5 — Swap

A swap always requires a **temporary variable** so the old value is not lost.

```java
public void run() {
    int[] values = {5, 10, 15, 20, 25};

    System.out.println("Before swap:");
    for (int i = 0; i < values.length; i++) {
        System.out.print(values[i] + " ");
    }
    System.out.println();

    // Swap first and last using a temporary variable
    int temp = values[0];
    values[0] = values[values.length - 1];
    values[values.length - 1] = temp;

    System.out.println("After swap:");
    for (int i = 0; i < values.length; i++) {
        System.out.print(values[i] + " ");
    }
}
```

## Problem 6 — Manual Copy

To copy arrays manually, create an empty array of the same size and copy elements **one index at a time**.

```java
public void run() {
    String[] original = {"Amy", "Ben", "Chen", "Dina"};
    String[] copy = new String[original.length];

    for (int i = 0; i < original.length; i++) {
        copy[i] = original[i];
    }

    System.out.println("Copied array:");
    for (int i = 0; i < copy.length; i++) {
        System.out.println(copy[i]);
    }
}
```

## Problem 7 — Index Expressions

We compute important positions instead of hardcoding them:
- first → `0`
- last → `length - 1`
- middle → `length / 2`

```java
public void run() {
    double[] data = {1.5, 3.2, 4.8, 7.6, 9.1};

    int last = data.length - 1;
    int middle = data.length / 2;

    System.out.println("First: " + data[0]);
    System.out.println("Last: " + data[last]);
    System.out.println("Middle: " + data[middle]);

    System.out.println("Expression element: " + data[data.length - 3]);
}
```

## Problem 8 — Store and Reorder User Input

Naming key indices helps readability:
- `last = length - 1`
- `middle = length / 2`

```java
public void run() {
    String[] names = new String[5];

    for (int i = 0; i < names.length; i++) {
        names[i] = readLine("Enter name #" + (i + 1) + ": ");
    }

    int last = names.length - 1;
    int middle = names.length / 2;

    System.out.println(names[2]);      // third entered
    System.out.println(names[0]);      // first entered
    System.out.println(names[last]);   // last entered
    System.out.println(names[1]);      // second entered
    System.out.println(names[middle]); // middle based on length
}
```

## Problem 9 — Neighbour Differences

The new array is always `length - 1` because differences exist *between* pairs of neighbours.

```java
public void run() {
    int[] values = {12, 5, 9, 20, 7};

    int[] diffs = new int[values.length - 1];

    for (int i = 0; i < diffs.length; i++) {
        diffs[i] = Math.abs(values[i] - values[i + 1]);
    }

    System.out.print("Original: ");
    for (int i = 0; i < values.length; i++) {
        System.out.print(values[i] + " ");
    }
    System.out.println();

    System.out.print("Diffs:    ");
    for (int i = 0; i < diffs.length; i++) {
        System.out.print(diffs[i] + " ");
    }
}
```

## Problem 10 — Formatted Score Table

We manually pad names using spaces by:
1. finding the longest name  
2. computing how many spaces each name needs  
3. printing using `print` + `println` only  

```java
public void run() {
    String[] players = {"Ana", "Ben", "Ming", "Hermione"};
    int[] scores = {14, 22, 18, 31};

    // Step 1: find the longest name
    int maxLen = 0;
    for (int i = 0; i < players.length; i++) {
        if (players[i].length() > maxLen) {
            maxLen = players[i].length();
        }
    }

    // Step 2: print padded table
    for (int i = 0; i < players.length; i++) {
        // Print name
        System.out.print(players[i]);

        // Add padding spaces
        int spacesNeeded = (maxLen - players[i].length()) + 2;
        for (int s = 0; s < spacesNeeded; s++) {
            System.out.print(" ");
        }

        // Print score
        System.out.println(": " + scores[i]);
    }
}
```

