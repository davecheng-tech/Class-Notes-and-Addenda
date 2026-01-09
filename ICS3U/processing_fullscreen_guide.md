# Running a Pixel Art Game Fullscreen

If you use `fullScreen()` and draw your game directly to the screen, Processing must redraw millions of pixels every frame.

- 1080p screens redraw about 2 million pixels per frame
- 4K screens redraw about 8 million pixels per frame

Even simple retro games will lag, even if your image files are very small.

This happens because the screen is large, not because your assets are large.


## The core idea

Your game should run at a small internal resolution, like an old console. Processing then stretches the final image to fit the screen. 

Think of it as:

> Draw the game on a small hidden canvas, then zoom it to fullscreen.

Consider this example:

```java
/**
 * This template runs the game at a small internal resolution
 * and scales it up to fullscreen for display.
 */

// ------------------------------
// GAME (LOGICAL) RESOLUTION
// ------------------------------
int LOGICAL_W = 320;
int LOGICAL_H = 180;

// Off-screen game canvas
PGraphics pg;

// Example game variables
PImage player;
int playerX = 40;
int playerY = 60;

// ------------------------------
// SETTINGS
// ------------------------------
void settings() {
    // Fullscreen display only, use P2D i.e. 2D OpenGL renderer
    fullScreen(P2D);
}

// ------------------------------
// SETUP
// ------------------------------
void setup() {
    // Create the small game canvas
    pg = createGraphics(LOGICAL_W, LOGICAL_H, P2D);

    // Disable smoothing for pixel art
    pg.noSmooth();
    noSmooth();

    // Load assets (example)
    player = loadImage("player.png");
}

// ------------------------------
// DRAW LOOP
// ------------------------------
void draw() {

    // ----- DRAW GAME TO SMALL CANVAS -----
    pg.beginDraw();
    pg.background(0);

    // Example drawing
    pg.image(player, playerX, playerY);
    pg.rect(10, 10, 20, 20);

    pg.endDraw();

    // ----- DISPLAY GAME FULLSCREEN -----
    image(pg, 0, 0, width, height);
}

// ------------------------------
// INPUT (EXAMPLE)
// ------------------------------
void keyPressed() {
    if (key == 'a') playerX -= 2;
    if (key == 'd') playerX += 2;
    if (key == 'w') playerY -= 2;
    if (key == 's') playerY += 2;
}


```

## What is `pg`?

`pg` is a small hidden canvas where the game is drawn.

- It is not an image file
- It is not a sprite
- It is a drawing surface you control

Processing calls this a `PGraphics`.

You do not need to understand classes or objects to use it.
You can think of it as another screen.


## Required pattern

### 1. Create a fullscreen window

```java
PGraphics pg;

void settings() {
  fullScreen(P2D);
}
```

`fullScreen()` controls the display size only.


### 2. Create the small game canvas

```java
void setup() {
  pg = createGraphics(320, 180, P2D);
  pg.noSmooth();
  noSmooth();
}
```

- 320 x 180 is the game resolution
- All game drawing happens at this size
- `noSmooth()` keeps pixel art sharp


### 3. Draw everything to the small canvas

```java
void draw() {
  pg.beginDraw();
  pg.background(0);

  // ALL GAME DRAWING GOES HERE
  pg.image(player, x, y);
  pg.rect(50, 50, 10, 10);

  pg.endDraw();

  // Show the game fullscreen
  image(pg, 0, 0, width, height);
}
```

Rules:
- Use `pg.` for all drawing
- Do not draw directly to the screen
- Processing stretches the result automatically


## What not to do

Do not run pixel-art games like this:

```java
fullScreen();
image(sprite, x, y, width * 10, height * 10);
```

This causes lag on high-resolution screens.
