# Quick Reference: Methods with Parameters & Return Values

So far, we’ve mostly written code inside `run()` and used `println()` to show results.  

CodingBat questions introduce a new idea: **methods that take input (parameters) and give back a result (return value)**.

In these problems, you don’t use `println()` and you don’t read input. Your job is to use the values already given in the method and return a result.

## 1. Understanding the Method Header

Example:
```java
public boolean cigarParty(int cigars, boolean isWeekend) {
```

- `boolean` → **return type** (method must return true or false)
- `cigars` (int) and `isWeekend` (boolean) → **parameters** (inputs already provided)

**Important:** Do **not** re-declare these variables. Do **not** ask the user for them.

**They already contain values when the method runs.**

<br>

## 2. No Console I/O Here

Inside CodingBat methods:

| DO | DON'T |
|----|------|
| use the parameters directly | do **not** use `readInt()`, `readBoolean()`, etc. |
| write logic and conditions | do **not** `println()` the answer |
| **return** the result | do **not** re-assign or re-declare parameters |

<br>

## 3. Returning a Value

A method with return type `boolean` must return `true` or `false`.

```java
return true;
```
or
```java
return (some condition);
```

Once a `return` runs, the method ends.

<br>

## 4. General Strategy for CodingBat

1. Use the variables in the method header. **They are already set up for you**.
2. Write your logic using:
   - `if / else`
   - comparison operators (`<`, `<=`, `>=`)
   - logical operators (`&&`, `||`)
3. Decide what value should be **returned**.
4. Use the `return` command to send back the final result.

<br>


## 5. Example: Cigar Party Problem

This is one of the practice problems on logic, found [here](https://codingbat.com/prob/p159531):

> When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return true if the party with the given values is successful, or false otherwise.

With the starter code:

```java
public boolean cigarParty(int cigars, boolean isWeekend) {
  
}
```

To solve, we can clarify the conditions for a successful squirrel party:

- On a weekday → cigars must be between 40 and 60 (inclusive)
- On a weekend → lower bound only (40+), no upper limit

#### Solution

```java
public boolean cigarParty(int cigars, boolean isWeekend) {
    if (isWeekend) {
        return cigars >= 40;
    } else {
        return cigars >= 40 && cigars <= 60;
    }
}
```

#### Shorter Version
```java
public boolean cigarParty(int cigars, boolean isWeekend) {
    return (isWeekend && cigars >= 40) ||
           (!isWeekend && cigars >= 40 && cigars <= 60);
}
```

Either is fine. Correctness matters, not length.

#### Or An Even Shorter Version
```java
public boolean cigarParty(int cigars, boolean isWeekend) {
    return (isWeekend && cigars >= 40) || (cigars >= 40 && cigars <= 60);
}
```
All the logic is contained within a single `return` statement. Not the clearest code to read, but a working solution nonetheless.

<br>

## 6. Common Mistakes (Avoid These!)

| Mistake | Why It's Wrong | Correct Behaviour |
|--------|----------------|------------------|
| `int cigars = readInt();` | Parameters already contain values | Use `cigars` directly |
| `System.out.println(true);` | Printing is not returning | Use `return true;` |
| `int cigars = 0;` | Re-declares the variable and erases the given value | Use the original variable |
| Multiple `return` statements unreachable | Code after `return` never runs | Ensure `return` ends the method |

