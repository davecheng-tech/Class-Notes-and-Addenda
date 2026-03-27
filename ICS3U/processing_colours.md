# A Note on Storing Colours in Java / Processing

In a basic sketch you might write colours inline:

```java
fill(255, 0, 0);
background(120, 197, 227);
```

If you're picking specific colours (e.g. with a [colour picker tool](https://redketchup.io/color-picker)) and want to reuse them, you can save them into variables. 

Colour values in Processing are stored as `int` — with the `color()` method packing your three R, G, B values into a single integer:

```java
int c1 = color(255, 0, 0);      // red
int c2 = color(120, 197, 227);  // cyan
```

Use them anywhere a colour value is expected:

```java
fill(c1);
background(c2);
```

Note that `color()` is a method inherited from `PApplet` that returns an `int`. The variable holding it is just an `int`.

Or, you could choose more descriptive variable names that actually identify the colours, e.g.:

```java
int brightCyan = color(120, 197, 227);  // cyan
fill(brightCyan);
```
