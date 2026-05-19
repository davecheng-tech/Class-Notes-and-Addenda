# Unit 4: Days 2–3 Lesson Plans — Python for GPIO

**Day 2 — May 19 (Tue):** Variables, loops, conditionals  
**Day 3 — May 20 (Wed):** Imports, `try/finally`, full GPIO script structure

These plans assume:
- Students completed Day 1 (analog vs digital, ADC/DAC, sample rate/bit depth)
- No Python assumed — plans build from zero
- Wide skill range: Java-experienced ICS students and total beginners in the same room
- Students work on Lubuntu Chromebooks (Acer C720) or macOS desktops — no Pi present yet

**Student note:** `unit-4-rpi/02-python-for-gpio.md`  
**Mock module:** `unit-4-rpi/gpio_sim.py` (post to Google Classroom before Day 2 starts)

---

## Before Day 2 — Setup Checklist

- [ ] Post `gpio_sim.py` to Google Classroom so students can download it
- [ ] Confirm Python 3 is installed on the Chromebooks: open terminal, run `python3 --version`
- [ ] Confirm a usable text editor exists: gedit, mousepad, VS Code, or similar — anything with line numbers
- [ ] Confirm your projector machine can run `python3` from a terminal
- [ ] Create a working folder on the projector machine: `~/gpio_lessons/`. Place `gpio_sim.py` inside it.
- [ ] Open the terminal and the text editor side-by-side on the projector — you'll live-code throughout

---

## Day 2 — Variables, Loops, Conditionals

**Goal:** Students understand the three Python building blocks they will see in every GPIO script. By the end of the period they can trace and write a simple loop with conditionals.

**Distribute:** `02-python-for-gpio.md` (or share the GitHub Pages link)

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Frame the two days |
| 5–15 | Environment setup — get everyone running `python3` |
| 15–25 | Variables — live demo |
| 25–40 | Loops — `while True` and `for` |
| 40–52 | Conditionals |
| 52–60 | Part A — read and trace (independent) |

---

### Frame the Two Days (5 min)

Connect to Day 1:

> "Last class you saw how a continuous voltage gets converted into binary — the ADC. That conversion ends up as data in a computer. Today we start on the other side: writing the code that tells the computer what to do with that data. On Day 4 you'll SSH into an actual Raspberry Pi and run your code on real hardware. The next two days on laptops are to get comfortable with the language first."

Put the complete blink script from §5 of the note on the projector — don't explain it yet:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)

finally:
    GPIO.cleanup()
    print("Done.")
```

Ask: "Without knowing Python at all — what do you think this script does?" Take two or three guesses. Validate reasonable ones. Don't explain — just let them see the destination.

Say: "By tomorrow, you'll be able to read every line of this and write something similar from scratch. Today we build the pieces."

---

### Environment Setup (10 min)

This will take longer than expected for some students — do it early.

**On Lubuntu Chromebooks:**
1. Students open a file manager, create a folder called `gpio` in their home directory
2. Download `gpio_sim.py` from Google Classroom into that folder
3. Open a terminal (usually `Ctrl+Alt+T` or find it in the application menu)
4. `cd ~/gpio` to navigate to the folder
5. `python3 --version` — should print Python 3.x.x. If not, alert you.
6. Open a text editor. In Lubuntu this is likely gedit or mousepad. Navigate to the `gpio` folder.

**On macOS:**
1. Same flow. Terminal is in Applications → Utilities. Text editor is VS Code or whatever is installed.

**Test together:** On the projector, create `hello.py` in the `gpio_lessons` folder containing `print("hello")`. Run it: `python3 hello.py`. Output: `hello`. Have students do the same.

> **Watch for:** Students who can't find the terminal, or whose `python3` command fails. On some Chromebook Lubuntu images, Python 3 is `python` not `python3` — check both. If a machine truly has no Python, pair that student with a neighbour.

---

### Variables — Live Demo (10 min)

Tell students to open a new file called `day2.py` in their `gpio` folder. You do the same on the projector. Type along as you explain — students follow on their own machines.

Type and run (using `python3 day2.py`) after each chunk:

```python
LED_PIN = 18
DELAY = 0.5
is_running = True
message = "ready"

print(LED_PIN)
print(DELAY)
print(is_running)
print(message)
```

Ask: "What type is `LED_PIN`? What type is `DELAY`? How did Python know?" → Python infers from the value. No declaration needed.

Ask: "Why did I name it `LED_PIN` in all caps?" → Convention for a constant — a value you don't change. Not enforced by Python, just readable.

Add and run:
```python
speed = 50
print(speed)
speed = 75
print(speed)
```

Ask: "What happened to the old value?" → Overwritten. The variable now holds 75.

> **ICS Java note (say aloud):** "If you're coming from Java: same idea, different syntax. In Java you'd write `int LED_PIN = 18;` — Python drops the type and the semicolon. Everything else works the same."

---

### Loops (15 min)

#### `for` loop

Add to `day2.py`:

```python
for i in range(3):
    print("blink", i)
```

Run it. Ask: "What did `range(3)` produce?" → The sequence 0, 1, 2. Three iterations.

Ask: "If I want five iterations?" → `range(5)`. Have students try it.

Point out indentation: "The `print` is inside the loop because it's indented. Python uses indentation — not curly braces — to define what's inside the loop. If you forget to indent, Python complains."

Demonstrate the error: un-indent the `print` and run. Show the error message. Re-indent and fix. This makes the indentation rule concrete before it bites someone later.

#### `while True` — the GPIO main loop

```python
while True:
    print("running...")
```

Do NOT run this on student machines yet — explain it first.

Say: "This loop runs forever. `True` is always true, so the condition never fails. This is the main loop pattern for every GPIO script you'll write — the Pi sits in this loop, checking sensors and responding to input, until you stop the script."

Ask: "How do you stop it?" → Ctrl+C. Demonstrate on the projector: run it, let it print a few lines, Ctrl+C. Students see the `^C` and the script stopping.

Now have students run it, then Ctrl+C. Let them feel the infinite loop.

Change it to something GPIO-flavored:

```python
while True:
    print("PIN 18 → HIGH")
    print("PIN 18 → LOW")
```

Say: "This is what a blink loop looks like before we add the real GPIO library. Two lines. Infinite. We'll add the real calls shortly."

> **Watch for:** Students who try to Ctrl+Z instead of Ctrl+C. Ctrl+Z suspends the process (it's still running in the background). Teach Ctrl+C explicitly.

---

### Conditionals (12 min)

Add to `day2.py`:

```python
temperature = 35

if temperature > 30:
    print("too hot")
elif temperature > 20:
    print("comfortable")
else:
    print("too cold")
```

Run. Change `temperature` to 25. Run. Change to 10. Run. Students trace through each branch.

Ask: "Which branch runs when temperature is exactly 30?" → The `elif` — "greater than 20, and not greater than 30." Work through it explicitly.

Now connect it to GPIO:

```python
button_state = False     # simulating: button not pressed

if button_state == True:
    print("button pressed — stop!")
else:
    print("no input — keep moving")
```

Run. Change `button_state = True`. Run. 

Say: "In a real GPIO script, instead of `button_state = False`, that line would be `button_state = GPIO.input(BUTTON_PIN)` — the GPIO library reads the actual voltage on the pin and gives back True or False. Your `if` statement is identical. The only thing that changes is where the value comes from."

This is the conceptual bridge. Make sure students hear it.

> **ICS Java note (say aloud):** "`elif` is just `else if` with a space removed. Parentheses around the condition are optional in Python — you'll see both with and without, both are valid."

---

### Part A — Read and Trace (8 min, independent)

Students work through Part A of the practice section in `02-python-for-gpio.md` independently. This is the motor control script trace — five questions.

Circulate. The goal is not speed — it's making sure students can read a script and predict its behaviour. Check that students can answer question 1 and 3 correctly. Questions 4 and 5 are the stretch ones.

Don't collect — go over answers quickly with the class in the last 2 minutes if time allows, or do it at the start of Day 3.

---

### Watch For — Day 2

- **Indentation errors:** The most common Python mistake. If a student gets a `IndentationError`, help them find the mis-indented line. Use a text editor with visible indentation or line numbers.
- **`=` vs `==` confusion:** Students writing `if temperature = 30:` will get a syntax error. Remind: `=` assigns, `==` compares.
- **`True` / `False` capitalisation:** Python is case-sensitive. `true` is not the same as `True`. Students coming from Java are used to lowercase — catch this early.
- **Students who are ahead (ICS/FTC):** They'll finish the variables and loops section in 5 minutes. Direct them to Part B or C of the practice section early.
- **Students who are lost:** Focus them on one thing: `print("hello")` runs. `for i in range(3): print(i)` runs. Don't try to catch them up on everything — make sure they have the infinite loop and the conditional, since those are the two pieces that appear in every lab.
- **The `gpio_sim.py` file:** Some students will forget to download it, or put it in the wrong folder. They'll get a `ModuleNotFoundError` when they try to import it. Fix: make sure `gpio_sim.py` is in the same directory as their `.py` file.

---

## Day 3 — Imports, `try/finally`, Full GPIO Script

**Goal:** Students write a complete GPIO script from scratch, using `gpio_sim` as the hardware layer. They understand every line before Day 4 puts real hardware in front of them.

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Recap Day 2 — go over Part A answers |
| 5–15 | Imports and modules |
| 15–30 | `try / finally` — the cleanup problem |
| 30–50 | Live-code the full blink script together |
| 50–58 | Part B — write your own script (independent) |
| 58–60 | Preview Day 4 |

---

### Recap Day 2 (5 min)

Go through Part A answers quickly. Key answers to confirm:
1. Loop runs 3 times (via `range(3)`)
3. During the delay, MOTOR_FWD is HIGH and MOTOR_REV is LOW — motor is running forward
4. Without `finally`, interrupting the script mid-run leaves the motor pin HIGH — motor keeps spinning
5. `while True` makes it run forever instead of 3 times

Ask: "Any questions before we move forward?" Keep this tight — don't let one question consume the recap.

---

### Imports and Modules (10 min)

Say: "Python ships with a lot of built-in functionality, but it's not all loaded automatically. Extra features live in modules — separate files of code that you pull in with `import`."

On the projector, open a new file `day3.py`:

```python
import time

time.sleep(2)
print("two seconds passed")
```

Run it. Students watch it pause. 

Ask: "What does `time.sleep(2)` do?" → Pauses for 2 seconds. "Why do we write `time.` before `sleep`?" → Because `sleep` is defined inside the `time` module; the dot tells Python where to look.

Say: "Without `import time`, that line would fail with a `NameError` — Python doesn't know what `time` is. The import is how you load the toolbox."

Now show the alias pattern:

```python
import time
import gpio_sim as GPIO     # using our simulator instead of RPi.GPIO

print(GPIO.BCM)             # a constant defined in gpio_sim
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
```

Run it. Students see:
```
11
[GPIO] setmode: BCM
[GPIO] setup: pin 18 → OUT
```

Ask: "Why did I write `as GPIO`?" → Short name. Easier to type. On a real Pi it would be `import RPi.GPIO as GPIO` — same alias, different source.

Say explicitly: "These two lines — `import gpio_sim as GPIO` and `import time` — are the first two lines of every GPIO script you write. Get used to them."

---

### `try / finally` — The Cleanup Problem (15 min)

This section earns its time. The pattern is not obvious, and students who skip it will leave motors running in a lab.

**Set up the problem first.**

Type a loop on the projector:

```python
import gpio_sim as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.5)
```

Run it. Let it print several HIGH/LOW lines. Then Ctrl+C.

Ask: "What state is pin 18 in when we pressed Ctrl+C?" → We don't know. Probably HIGH — it was last set HIGH inside the loop, and the script was interrupted before it could set it LOW.

Say: "On a real Pi, that means the LED stays on. Or worse: if pin 18 is driving a motor, the motor keeps spinning after your script ends. That's a problem."

Ask: "What's the solution?" → Run cleanup code when the script ends. But how do you guarantee code runs on Ctrl+C?

Say: "`try / finally` is Python's answer. The `finally` block runs no matter how the `try` block ends — normal exit, error, or Ctrl+C."

Add `try / finally` to the script live on the projector:

```python
import gpio_sim as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)

finally:
    GPIO.cleanup()
    print("Cleaned up. Script ended safely.")
```

Run it. Let it loop. Ctrl+C. Students see:
```
[GPIO] output: pin 18 → HIGH
[GPIO] output: pin 18 → LOW
...
^C
[GPIO] cleanup
Cleaned up. Script ended safely.
```

Ask: "What's different now?" → `cleanup()` ran. The pins are reset. The motor stops. The LED goes off.

Say: "From here on, every GPIO script you write wraps the main loop in `try / finally`. It is not optional. If you submit a lab script without it, I'll ask you to add it before I mark it."

> **For experienced programmers (say this aloud):** "If you know try/except from other languages — yes, there's also `except` in Python. We're not using it here. `finally` is all we need: it catches everything, including keyboard interrupts. Adding `except KeyboardInterrupt: pass` would suppress the `^C` indicator in the terminal — some scripts do that, it's a style choice."

---

### Live-Code the Full Blink Script Together (20 min)

This is the culminating section of Day 3. Build the complete script together, line by line, with students typing alongside on their machines.

Delete everything in `day3.py` and start fresh. Type slowly — pause after each section and explain before moving on.

```python
import gpio_sim as GPIO
import time
```

Ask: "Why `as GPIO`? Why `time`?" → Quick recap. Two seconds only.

```python
LED_PIN = 18
```

Ask: "Why store the pin number in a constant instead of just writing 18 everywhere?" → If the pin changes, you update one line. If you write 18 fifteen times, you have to find all fifteen.

```python
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
```

Ask: "What does `setmode` do? What are the two options?" → BCM or BOARD pin numbering. Always BCM.  
Ask: "What does `GPIO.OUT` mean?" → We're sending signals out, not reading them in.

```python
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
```

Ask: "What will the terminal show when this runs?" → Students predict before running. Then run together.

Confirm output and then add the finally block:

```python
finally:
    GPIO.cleanup()
    print("Done.")
```

Ctrl+C and confirm cleanup runs. Full script:

```python
import gpio_sim as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)

finally:
    GPIO.cleanup()
    print("Done.")
```

Now go back to the script you showed at the start of Day 2. Put it side by side.

Say: "This is the same script you saw at the beginning of yesterday. You can now read every line of it. On Day 4, the only thing that changes is this line:" 

Point to `import gpio_sim as GPIO`.

Say: "On the Pi, that becomes `import RPi.GPIO as GPIO`. Every other line is identical. The script runs on real hardware."

---

### Part B — Write Your Own Script (8 min, independent)

Students write the two-LED alternating script from Part B of the practice section. This is:
- Two constants: `LED_A = 18`, `LED_B = 23`
- Both set up as outputs
- `while True` loop alternating them
- `try / finally` with cleanup

Circulate. Check:
1. Are both pins set up before the loop?
2. Is `try / finally` present?
3. Does the output alternate correctly when they run it?

For students who finish: point them to Part C (add a simulated button input) or Part D (reorganise into functions).

---

### Preview Day 4 (2 min)

Say: "Tomorrow — or the day after depending on hardware — you'll SSH into a real Raspberry Pi. You'll copy your script onto it, change the import line, and run it. An actual LED will blink. Everything else is identical to what you wrote today."

Point out the physical setup: "The Pi runs Linux — you did that in Unit 2. Same SSH workflow. Same terminal. Same `python3 yourscript.py`. The only new thing is the physical circuit."

---

### Watch For — Day 3

- **`try` / `finally` indentation:** The `while True` loop is indented inside `try`. The `finally` is at the same level as `try` — not inside it. Students often indent `finally` inside the loop. Python will error; help them find the indentation level.
- **`GPIO.cleanup()` in the wrong place:** Some students put it inside the `while True` loop instead of in `finally`. This means cleanup runs every iteration. Catch this early — the effect is subtle (it works, but the pins are reset 2× per second).
- **Missing `GPIO.setup()` before the loop:** Students sometimes write `setmode` but forget `setup`. The simulator will print a warning (`WARNING: pin 18 is not set up as OUT`). Use it as a teaching moment.
- **`gpio_sim.py` not in the same folder:** If they moved their script to a different folder without moving `gpio_sim.py`, they'll get `ModuleNotFoundError: No module named 'gpio_sim'`. Fix: check that both files are in the same directory using `ls` in the terminal.
- **Students who want to skip ahead:** Some will ask "can we just write the real GPIO import?" Encourage it — but explain they won't be able to run it until Day 4. They can write `import RPi.GPIO as GPIO` and leave a comment about swapping it, or test with the simulator now and swap on the Pi.
- **FTC/advanced students finishing Part B in 5 minutes:** Have Part C and D ready. Part D (organise into functions) is genuinely useful practice for the CPT code structure — point it out explicitly to students who are ready.
- **Students who did not finish Part A:** Have them focus on the complete blink script first. Reading it, tracing it, then modifying it is more valuable than trying to write from scratch.

---

## Connector: Day 3 → Day 4

Between Day 3 and Day 4, the Pi setup needs to be confirmed ready (see `unit-4-overview.md` procurement checkpoints):
- SD cards imaged with Raspberry Pi OS Lite
- All Pis confirmed connecting to YCBYOD
- IPs identified and listed
- Default SSH credentials set (`pi` / `raspberry`)

On Day 4, students will:
1. SSH into their Pi (per `03-rpi-setup.md` once that is written)
2. Transfer their Day 3 script using `scp` or retyping in `nano`
3. Change `import gpio_sim as GPIO` → `import RPi.GPIO as GPIO`
4. Run it with `python3 blink.py`
5. See the LED blink

The single-import swap is the moment that ties Days 2–3 to the hardware. Make it explicit on Day 4.
