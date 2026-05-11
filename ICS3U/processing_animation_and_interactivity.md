# Processing Lesson: Animation & Interactivity

This reference document provides a complete guide to all skills required for the **Animation and Interactivity** assignment in ICS3U.  

## 1. The Processing Program Structure

Processing programs use the following general structure:

```java
import processing.core.PApplet;

/**
 * Template for programs with Processing graphics output.
 * @author Your Name
 */
public class Sketch extends PApplet {

    // ----------------------------------------------------
    // Declare global variables here
    // ----------------------------------------------------
    // Example:
    // int sunX = 100;
    // int speed = 3;


    public static void main(String[] args) {
        PApplet.main("Sketch");
    }

    @Override
    public void settings() {
        size(600, 600);  // Canvas size
    }

    @Override
    public void setup() {
        // Runs once at the start
    }

    @Override
    public void draw() {
        // Runs in a loop approx. 60 times per second
        background(120, 197, 227);  // Re-draw background to erase previous frame
        fill(242, 19, 224);
        circle(300, 300, 200);
    }

    // ----------------------------------------------------
    // Write additional helper methods below
    // ----------------------------------------------------
    // Example:
    // private void drawBall() { }
    // private void moveBall() { }

}
```
- `settings()` runs first, before the window is created.
- `setup()` runs once at the beginning, drawing elements.
- `draw()` runs ~60 times per second, repeatedly drawing elements.

### frameRate()

You can control the frame speed:

```java
public void setup() {
  frameRate(60);
}
```

### loop() and noLoop()

- `noLoop()` stops the animation.
- `loop()` restarts it.

## 2. Basic Animation

Animation happens when you change a variable a tiny bit each frame.  

Recall that `draw()` is a continuous loop. By defining the ball variables as global (i.e., outside of any method) they are not only accessible to all methods, but their values are not reset everytime `draw()` loops again. 

```java
float ballX = 100;
float ballY = 300;
float dx = 3;

public void draw() {
  background(255);

  ballX = ballX + dx;

  ellipse(ballX, ballY, 40, 40);
}
```

## 3. Edge Detection

Detect when the ball hits the borders. This clean bit of code checks both left and right extremities and negates the "speed" of the ball, thereby making it reverse direction.

```java
if (ballX > width || ballX < 0) {
  dx = -dx;
}
```

## 4. Mouse Input

### mouseX and mouseY

These built-in variables report the coordinates of the mouse when hovering over the sketch window. They are updated every `draw()` frame refresh.

```java
ellipse(mouseX, mouseY, 40, 40);
```

### mousePressed variable

Boolean value reporting `true` if any mouse button is pressed. Remains `true` as long as the button is held down.

```java
if (mousePressed) {
  fill(255, 0, 0);
} else {
  fill(0);
}
```

### mousePressed() event function
A predefined, built-in method that is called whenever the mouse button is pressed. This happens independently of the `draw()` loop.

```java
public void mousePressed() {
  System.out.println("Mouse clicked at: " + mouseX + ", " + mouseY);
}
```

## 5. Keyboard Input
Similar to `mousePressed()`, we have `keyPressed()` as a built-in method called whenever a key is pressed. Within this method, we can use the built-in variables `key` and `keyCode` to check what was pressed and respond accordingly.

### key and keyCode

```java
public void keyPressed() {
  if (key == 'a') {
    println("A pressed");
  }
  if (keyCode == UP) {
    println("Up arrow");
  }
}
```

## 6. Instructions On Screen
Use Processing's `text()` method to display text on-screen. Refer to the [documentation](https://processing.org/reference/text_.html) for additional methods to style your text.

```java
fill(0);
textSize(16);
text("Press A to change colour. Click to move ball.", 20, 20);
```

## 7. Useful Links

- Animation: https://happycoding.io/tutorials/processing/animation  
- Input: https://happycoding.io/tutorials/processing/input  



