# Unit 4: Days 2–3 Lesson Plans — Python for GPIO

**Day 2 — May 19 (Tue):** Variables, loops, conditionals → independent practice  
**Day 3 — May 20 (Wed):** Functions (brief), imports, `try/finally`, full script → trace + write

These plans assume:
- Students completed Day 1 (analog vs digital, ADC/DAC, sample rate/bit depth)
- No Python assumed — plans build from zero
- Wide skill range: Java-experienced ICS students and total beginners in the same room
- Students work on Lubuntu Chromebooks (Acer C720) or macOS desktops — no Pi present yet

**Student note:** `unit-4-rpi/02-python-for-gpio.md`  
**Mock module:** `unit-4-rpi/gpio_sim.py` (post to Google Classroom before Day 2 starts)

---

## Before Day 2 — Setup Checklist

- [ ] Post `gpio_sim.py` to Google Classroom so students can download it (they won't use it until Day 3, but download it now while you remember)
- [ ] Confirm Python 3 is installed on the Chromebooks: open terminal, run `python3 --version`
- [ ] Confirm a usable text editor exists: gedit, mousepad, VS Code, or similar — anything with line numbers
- [ ] Confirm your projector machine can run `python3` from a terminal
- [ ] Create a working folder on the projector machine: `~/gpio_lessons/`. Place `gpio_sim.py` inside it.
- [ ] Open the terminal and the text editor side-by-side on the projector — you'll live-code throughout

---

## Day 2 — Variables, Loops, Conditionals

**Goal:** Students understand the three Python building blocks they will see in every GPIO script, and write their first independent Python code.

**Student note sections covered:** §1, §2.1–2.3, Day 2 Practice  
**Distribute:** Share the GitHub Pages link for `02-python-for-gpio.md`

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Frame the two days |
| 5–15 | Environment setup — get everyone running `python3` |
| 15–25 | §2.1 Variables — live demo |
| 25–40 | §2.2 Loops — `for` and `while True` |
| 40–50 | §2.3 Conditionals |
| 50–60 | Day 2 Practice — independent work (§ Day 2 Practice in the note) |

---

### Frame the Two Days (5 min)

Connect to Day 1:

> "Last class you saw how a continuous voltage gets converted into binary — the ADC. That conversion ends up as data in a computer. Today we start on the other side: writing the code that tells the computer what to do with that data. On Day 4 you'll SSH into an actual Raspberry Pi and run your code on real hardware. The next two days on laptops are to get comfortable with the language first."

Put the complete blink script from §6 of the note on the projector — don't explain it yet:

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
1. Open a file manager, create a folder called `gpio` in the home directory
2. Open a terminal (`Ctrl+Alt+T` or find it in the application menu)
3. `cd ~/gpio`
4. `python3 --version` — should print Python 3.x.x. If not, try `python --version` and use whichever works.
5. Open a text editor (gedit or mousepad). Save new files into the `gpio` folder.

**On macOS:**
1. Same flow. Terminal is in Applications → Utilities.

**Test together:** On the projector, create `hello.py` in `gpio_lessons/` containing `print("hello")`. Run it: `python3 hello.py`. Output: `hello`. Have students do the same.

> **Watch for:** Students who can't find the terminal — walk them through it. If a machine has no Python at all, pair that student with a neighbour for today.

---

### §2.1 Variables — Live Demo (10 min)

Tell students to open a new file called `day2.py` in their `gpio` folder. You do the same on the projector. Type along as you explain — students follow on their own machines. Run with `python3 day2.py` after each chunk.

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

Ask: "Why did I name it `LED_PIN` in all caps?" → Convention for a constant. Not enforced by Python, just readable.

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

### §2.2 Loops (15 min)

#### `for` loop

Add to `day2.py`:

```python
for i in range(3):
    print("blink", i)
```

Run it. Ask: "What did `range(3)` produce?" → The sequence 0, 1, 2. Three iterations.

Ask: "If I want five iterations?" → `range(5)`. Have students try it.

Point out indentation: "The `print` is inside the loop because it's indented. Python uses indentation — not curly braces — to define what's inside the loop. If you forget to indent, Python complains."

Demonstrate the error: un-indent the `print` and run. Show the error. Re-indent and fix. This makes the indentation rule concrete before it bites someone later.

#### `while True` — the GPIO main loop

```python
while True:
    print("running...")
```

Explain before running: "This loop runs forever. `True` is always true, so the condition never fails. This is the main loop pattern for every GPIO script — the Pi sits in this loop, checking sensors and responding to input, until you stop the script."

Ask: "How do you stop it?" → Ctrl+C. Demonstrate on the projector: run it, let it print a few lines, Ctrl+C. Students see the `^C` and the script stopping.

Have students run it, then Ctrl+C. Let them feel the infinite loop.

Change it to something GPIO-flavored:

```python
while True:
    print("PIN 18 → HIGH")
    print("PIN 18 → LOW")
```

> **Watch for:** Students who try Ctrl+Z instead of Ctrl+C. Ctrl+Z suspends the process — it keeps running in the background. Teach Ctrl+C explicitly and have everyone practice it.

---

### §2.3 Conditionals (10 min)

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

Run. Change `temperature` to 25, then 10. Students trace through each branch.

Ask: "Which branch runs when temperature is exactly 30?" → The `elif`. Work through it explicitly.

Now connect it to GPIO context:

```python
button_state = False

if button_state == True:
    print("button pressed — stop!")
else:
    print("no input — keep moving")
```

Run. Change `button_state = True`. Run.

Say: "In a real GPIO script, `button_state = False` would be replaced by `button_state = GPIO.input(BUTTON_PIN)` — the library reads the actual voltage on the pin and returns True or False. Your `if` statement stays identical. The only thing that changes is where the value comes from."

> **ICS Java note (say aloud):** "`elif` is just `else if` with the space removed. Parentheses around the condition are optional in Python."

---

### Day 2 Practice — Independent Work (10 min)

Direct students to the **Day 2 Practice** section in `02-python-for-gpio.md`. Everyone starts on Part A.

**Part A (everyone):** Blink simulator — write a `for` loop that prints `"LED ON"` / `"LED OFF"` five times, then add a conditional to detect the last iteration.

**Part B (extension):** Two-speed blink — two separate loops with different labels and a conditional inside the slow loop.

**Part C (reach ahead — ICS / FTC students):** Write a `blink(label, count)` function and use it to replace the two loops. This previews §3 (Functions) from tomorrow.

Circulate. For Part A, the common sticking point is the last-iteration conditional: `i == BLINK_COUNT - 1`. Students who don't know about zero-indexing will get this wrong — walk through it with them.

**Extension prompt if students finish Part C:** "Can you modify your function to accept a third parameter `delay` and print a pause indicator (`"  [pause]"`) between each blink? You won't need `time.sleep()` — just print the indicator."

Don't collect. Confirm Part A is working (correct output in the terminal) before the period ends.

---

### Watch For — Day 2

- **Indentation errors:** The most common Python mistake. If a student gets `IndentationError`, help them find the mis-indented line. Use a text editor with visible indentation or line numbers.
- **`=` vs `==`:** Students writing `if temperature = 30:` get a syntax error. Remind: `=` assigns, `==` compares.
- **`True` / `False` capitalisation:** Python is case-sensitive. `true` is not `True`. Students from Java are used to lowercase — flag it early.
- **`range(3)` off-by-one:** Students often expect `range(3)` to produce 1, 2, 3. Show the output explicitly.
- **Ctrl+C vs Ctrl+Z:** Ctrl+Z leaves a zombie process running. If a student's terminal seems stuck or their next script behaves oddly, they probably Ctrl+Z'd something. Have them close and reopen the terminal.
- **Students who fly through Part A quickly:** Direct them to Part B, then C. Part C (the function) is the genuine reach-ahead — it bridges to tomorrow's content. If they finish Part C, give the extension prompt above.
- **Students who are lost:** Don't try to catch them up on everything. If they can write `for i in range(5): print(i)` and change a variable, that's enough for today. The live-coding examples stay in `day2.py` as reference.

---

## Day 3 — Functions, Imports, `try/finally`, Full GPIO Script

**Goal:** Students understand the complete anatomy of a GPIO script and write one from scratch using `gpio_sim`.

**Student note sections covered:** §3 (Functions — reference), §4 (Imports), §5 (try/finally), §6 (Complete Script), §7 (Running on Laptop), §8 Part A and B

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Check-in — Day 2 practice |
| 5–15 | §4 Imports and modules |
| 15–28 | §5 `try / finally` — the cleanup problem |
| 28–47 | §6 Live-code the full blink script together |
| 47–53 | §8 Part A — trace (as a class) |
| 53–60 | §8 Part B — write your own (independent, + extensions) |

---

### Check-in — Day 2 Practice (5 min)

Ask two or three students to share what their Part A output looked like. Confirm:
- Loop ran 5 times (or 3 after the modification)
- Last blink printed `"Last blink!"`
- Everyone's `python3 practice.py` actually ran without errors

Ask: "Did anyone get to Part C — the function?" If yes, have them briefly describe what they wrote. Say: "We'll come back to functions — that's §3 in the note, and it's reference material for later. Today we focus on the pieces that go into every GPIO script."

Don't spend time going through wrong answers from yesterday — that's not what this 5 minutes is for. Move quickly.

---

### §4 Imports and Modules (10 min)

Open a new file `day3.py` on the projector. Students do the same.

```python
import time

time.sleep(2)
print("two seconds passed")
```

Run it. Students watch it pause.

Ask: "Why `time.` before `sleep`?" → `sleep` is defined inside the `time` module; the dot says where to look.

Say: "Without `import time`, that line would fail with `NameError: name 'time' is not defined`. The import is how you load the toolbox."

Now show the alias pattern:

```python
import time
import gpio_sim as GPIO

print(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
```

Run it. Students see:
```
11
[GPIO] setmode: BCM
[GPIO] setup: pin 18 → OUT
```

Ask: "Why `as GPIO`?" → Short name, easier to type. On a real Pi it would be `import RPi.GPIO as GPIO` — same alias, different source.

Say: "These two lines are the first two lines of every GPIO script you write. Get used to them."

> **Note to self:** This is when `gpio_sim.py` needs to be in the `gpio` folder. If students forgot to download it from Google Classroom, have them do it now before moving on.

---

### §5 `try / finally` — The Cleanup Problem (13 min)

This section earns its time. Students who skip the pattern will leave motors running in a lab.

**Set up the problem first.** Type on the projector (students follow):

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

Ask: "What state is pin 18 in when we pressed Ctrl+C?" → Unknown — probably HIGH, since that's the last line that ran before the interrupt.

Say: "On a real Pi that means the LED stays on. Or if pin 18 is driving a motor, the motor keeps spinning after your script ends. That's a problem."

Ask: "How do you guarantee cleanup code runs even on Ctrl+C?" → Let students suggest. Then show `try / finally`.

Modify the script on the projector:

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
    print("Cleaned up.")
```

Run it. Let it loop. Ctrl+C. Students see cleanup running.

Ask: "What changed?" → `cleanup()` ran. Pins are reset.

Say: "Every GPIO script you write wraps the main loop in `try / finally`. Non-negotiable. If you submit a lab script without it, I'll ask you to add it."

> **For experienced programmers:** "`except` also exists in Python — yes, you could use `except KeyboardInterrupt`. We're using `finally` because it catches everything: Ctrl+C, errors, normal exit. `finally` is the guaranteed path."

---

### §6 Live-Code the Full Blink Script (19 min)

Build the complete script together, line by line. Students type alongside. Delete everything in `day3.py` and start fresh. Type slowly — stop and ask questions before adding the next block.

```python
import gpio_sim as GPIO
import time
```

Ask: "Why do we need both?" → GPIO for pin control, time for `sleep`.

```python
LED_PIN = 18
```

Ask: "Why a constant instead of just writing 18 everywhere?" → If the pin changes, update one line. Otherwise you're hunting through the whole file.

```python
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
```

Ask: "What are the two options for `setmode`? Which do we always use?" → BCM or BOARD. Always BCM.  
Ask: "What does `GPIO.OUT` mean?" → This pin sends signals, it doesn't receive them.

```python
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
```

Ask: "Before we run this — what will the terminal output look like?" Let students predict. Then run together.

Add the `finally` block:

```python
finally:
    GPIO.cleanup()
    print("Done.")
```

Ctrl+C. Confirm cleanup runs.

Now put the Day 2 opening script back on the projector beside the one students just typed.

Say: "This is the exact script I showed you at the start of yesterday before you knew any Python. You can now read every line. On Day 4, the only change is this:" — point to `import gpio_sim as GPIO` — "that becomes `import RPi.GPIO as GPIO`. The rest runs unchanged on real hardware."

---

### §8 Part A — Trace (6 min, as a class)

Direct students to §8 Part A in the note. Read the script aloud together from the projector — or have a student read it.

Go through the questions as a class, calling on students:

1. "What does the LED do in the first second?" → blinks 3 times quickly (0.2s on, 0.2s off × 3 = 1.2s total)
2. "How long does the `for` loop take?" → 3 × (0.2 + 0.2) = 1.2 seconds
3. "What happens after the `for` loop?" → falls into `while True`, slow 1s blink
4. "Ctrl+C during the `for` loop — what prints?" → one of the GPIO output lines mid-loop, then `[GPIO] cleanup` and `"Done."`
5. "Ctrl+C during `while True` — same result?" → yes, `finally` runs either way
6. "What's the difference between the two loops' behaviour?" → `for` loop: fast startup blink. `while True`: slow steady blink. The `for` loop is intentional — it's a "ready" signal pattern common in hardware.

The goal is that students see `finally` running correctly from two different interrupt points. This concretely shows the guarantee.

---

### §8 Part B — Write Your Own (7 min, independent)

Direct students to §8 Part B. Everyone writes the two-LED alternating script:
- Constants: `LED_A = 18`, `LED_B = 23`, `DELAY = 0.3`
- Both pins set up as outputs
- `while True` loop alternating them
- `try / finally` with `GPIO.cleanup()`

**Extensions — for students who finish:**

**Part C:** Add a simulated button. Set up `BUTTON_PIN = 25` as an input. Read it with `GPIO.input(BUTTON_PIN)` inside the loop. If `True`, print `"Button pressed!"` and skip the alternation for that iteration. Test by editing `SIMULATED_INPUT` in `gpio_sim.py`.

**Part D:** Reorganise the script using functions. Write `def setup():`, `def main_loop():`, `def teardown():`, and call them from the bottom of the file. Add a `blink_n(pin, n, delay)` function that blinks a single pin n times — call it in `setup()` as a startup signal before the main loop begins. This is the CPT robot code structure — functions per behaviour, one setup, one main loop.

**FTC/advanced students:** If they've completed Part D, have them try adding a second `BLINK_RATE` variable and making the alternation speed controllable from one place. Then ask: "How would you add a third LED that blinks independently of the other two?" — no answer needed today, just the question.

Circulate. Key things to check:
1. Both pins set up before the loop?
2. `try / finally` present with cleanup inside `finally`?
3. Output alternates correctly?

---

### Preview Day 4 (end of Part B, informal)

As you circulate during Part B, say to individual students or the class:

> "Next class you SSH into a real Pi. You copy this script, change the import line, wire an LED to pin 18, and run it. The LED physically blinks. Everything else is what you wrote today."

---

### Watch For — Day 3

- **`finally` indentation:** `finally` must be at the same level as `try` — not inside the `while True` loop. This is the most common structural error. Python's error message for this is not always obvious. Check indentation visually.
- **`GPIO.cleanup()` inside the loop:** Some students put it inside `while True` instead of in `finally` — cleanup runs on every iteration. The simulator output will show repeated `[GPIO] cleanup` lines; use that as the diagnostic.
- **`gpio_sim.py` not in the same folder:** `ModuleNotFoundError: No module named 'gpio_sim'`. Fix: `ls` in the terminal to confirm both files are in the same directory.
- **Missing `GPIO.setup()` before the loop:** The simulator prints a warning (`WARNING: pin X is not set up as OUT`). Make it a teachable moment — don't just tell them to add the line, ask them why the warning appeared.
- **Part B script that runs but output doesn't alternate:** Check that `GPIO.output` is called for both pins each iteration — a common error is only calling it for one pin.
- **FTC/advanced students who skip the structure:** They may write working code that doesn't have named constants, or that skips `GPIO.setup`. The working output masks the structural issues. Check their scripts, not just their terminal.
- **Students asking "can I just use `import RPi.GPIO`?":** Encourage it — but they won't be able to run it until the Pi. They can write `import RPi.GPIO as GPIO` now and swap back to test.

---

## Connector: Day 3 → Day 4

Between Day 3 and Day 4, Pi setup must be confirmed ready (see `unit-4-overview.md` procurement checkpoints):
- SD cards imaged with Raspberry Pi OS Lite
- All Pis confirmed connecting to YCBYOD
- IPs identified via network scanner and listed for students
- SSH accessible: default user `pi`, password `raspberry`

On Day 4, students will:
1. SSH into their Pi
2. Get their script onto it (options: `nano` to retype, `scp` to transfer, or email to self and `wget`)
3. Change `import gpio_sim as GPIO` → `import RPi.GPIO as GPIO`
4. Run: `python3 blink.py`
5. Wire an actual LED and see it blink

The import swap is the moment that ties Days 2–3 to the hardware. Make it explicit on Day 4 — hold up the two versions side by side if you can.
