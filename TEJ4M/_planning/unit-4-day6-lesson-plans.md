# Unit 4: Day 6 Lesson Plan — GPIO Lab 2: Button

**Day 6 — May 25 (Mon):** Digital input, pull-down resistors, polling loop, debounce

This plan assumes:
- Students completed Day 5: LED circuit wired, blink script running on real hardware
- LED circuits are still wired (or students can rewire in 2 minutes from memory)
- SD cards stay in Pis — scripts from Day 5 still on the Pi in `~/gpio/`
- Pairs: same as Day 5
- Period length: **70 minutes**

**Student notes to have ready:**
- `unit-4-rpi/02-python-for-gpio.md` (distributed earlier)
- `unit-4-rpi/lab-02-button.md` ← needs to be posted before class

---

## Before Day 6 — Setup Checklist

- [ ] Button kits added to each pair's tray: 1× tactile button, 1× 10kΩ resistor (brown-black-orange), extra M-F jumpers
- [ ] Confirm 10kΩ resistors are in bins — they look similar to 330Ω (orange-orange-brown); colour-band IDs are in the lab note
- [ ] Post `lab-02-button.md` to Google Classroom before class
- [ ] Power on Pis early — confirm they connect to YCBYOD, pull the IP list
- [ ] Prep your own demo circuit (button + pull-down on BCM 25, LED still on BCM 18) — test it at home first

---

## Day 6 — GPIO Lab 2: Button

**Goal:** Students wire a pull-down button circuit, write a polling loop that reads it, and connect button input to LED output. By end of class, pressing the button physically lights the LED.

**Hardware per pair:** RPi (mains-powered), existing breadboard + LED circuit from Day 5, tactile button, 10kΩ resistor, 2× additional M-F jumpers

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Hook — from output to input |
| 5–20 | Concept: floating pins and pull-down resistors |
| 20–27 | Concept: debounce — why physical buttons are noisy |
| 27–37 | Demo: wire button circuit + read script (teacher on projector) |
| 37–62 | Pairs wire circuit — Part A (print state), then Part B (LED control) |
| 62–68 | Extension: toggle with debounce |
| 68–70 | Lab completion check + shutdown |

---

### Hook (5 min)

> "On Day 5, code caused a physical thing to happen — the LED blinked. Today we go the other direction: a physical thing happens, and code responds to it. You press a button, the Pi knows. That's all a sensor is — something physical changing a pin's voltage."

Leave it there. Don't over-explain. The payoff is when they press the button and the LED responds.

---

### Concept: Floating Pins and Pull-Down Resistors (15 min)

This is the most important concept of the day. Spend the time — students who skip this will have circuits that behave randomly and no mental model for why.

**Start with the problem.**

Draw this on the board or narrate:

> "A GPIO input pin reads the voltage at its connection. When nothing is wired to it, it's 'floating' — not connected to 3.3V or GND. A floating pin picks up stray electrical noise from the environment: nearby circuits, your hand, the power supply. The Pi reads it as HIGH, or LOW, or it flickers between them randomly. If you check the input, you get garbage."

Ask: "If we wire a button between the pin and 3.3V, what happens when the button is NOT pressed?" → The wire from 3.3V is disconnected, so the pin is still floating. Same problem.

**The fix: a pull-down resistor.**

Draw the circuit:

```
3.3V (pin 1)  ──── [button] ──── BCM 25 (pin 22)
                                       │
                                    10 kΩ
                                       │
                                     GND
```

> "The 10kΩ resistor connects the input pin to GND. When the button is open, the resistor 'pulls' the pin to 0V — it reads LOW, reliably, every time. When you press the button, 3.3V connects directly to the pin through a short wire. That's a much stronger signal than 10kΩ to GND, so the pin goes HIGH. Pressed = HIGH. Released = LOW."

Ask: "Why not use a 100Ω resistor instead of 10kΩ?" → When the button is pressed, current flows from 3.3V through the resistor to GND. Lower resistance = more current = more wasted power. 10kΩ gives 3.3V ÷ 10,000Ω = 0.33mA when pressed. That's negligible. 100Ω would give 33mA — hot, wasteful, and potentially stressing the 3.3V pin.

Ask: "Does the 10kΩ pull-down conflict with the button's 3.3V when pressed?" → No. The voltage at pin 25 when pressed is determined by the 3.3V source (via low-resistance wire), not the 10kΩ pull-down. The pin reads HIGH. The 10kΩ just bleeds a tiny current to GND — that's its job.

**Show the code for setup:**

```python
BUTTON_PIN = 25

GPIO.setup(BUTTON_PIN, GPIO.IN)     # input pin — no pull_up_down argument needed
                                     # because we have an external pull-down
```

Then reading it:

```python
state = GPIO.input(BUTTON_PIN)       # returns True (HIGH) or False (LOW)
```

> "That's it. `GPIO.input()` returns `True` if the pin is at 3.3V, `False` if it's at 0V. Pressed = 3.3V = `True`. Released = 0V = `False`. Everything else in the script is a conditional responding to that."

**Mention internal pull resistors (briefly — don't go deep):**

> "The RPi has built-in pull resistors you can enable in software: `GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)`. That would let us skip the 10kΩ in our kit. We're using the external resistor today because you can see it in the circuit — it makes the concept tangible. In the CPT, you can use either."

---

### Concept: Debounce — Why Physical Buttons Are Noisy (7 min)

This is a short concept section but an important one. Build intuition for it before the demo, so students recognise the behaviour when they see it.

> "When you press a physical button, the metal contacts don't make a clean single connection. They bounce — the contact makes and breaks, makes and breaks, several times in the first few milliseconds before settling. To your finger, it's one press. To the Pi, which can poll a pin thousands of times per second, it looks like multiple rapid presses."

Ask: "If you're just reading whether the button is held down right now — like 'is it currently pressed?' — does bounce matter?" → Not really. By the time you read it, the bouncing is done.

Ask: "If you're counting presses, or toggling a state on each press — like pressing once to turn an LED on, pressing again to turn it off — does bounce matter?" → Yes. One physical press might register as 3 or 5 transitions. The toggle fires multiple times and the result is unpredictable.

> "The simplest fix is a **delay after detecting a press**. If we add `time.sleep(0.2)` to our polling loop, we're only checking the pin 5 times per second. Contact bounce is usually over in 50ms — by the time we sample again, the pin has settled."

Write on the board:

```
bounce duration: ~5–50 ms
polling every 200 ms → bounce is invisible
polling every 1 ms → bounce looks like many presses
```

> "For Part A and B of this lab, bounce doesn't matter — we're polling state. For the extension (toggle), you'll see why it does."

---

### Demo: Wire Button Circuit + Read Script (10 min)

Do this on the projector. Students watch, then replicate.

**Wiring (narrate as you go):**

1. Leave the Day 5 LED circuit intact — BCM 18 → 220Ω → LED → blue rail (GND)
2. Place the tactile button spanning the breadboard centre channel
3. Jumper from **3V3 on the cobbler** to the row on one side of the button
4. On the other side of the button: jumper to **GPIO25 on the cobbler**
5. In the same row as the GPIO25 jumper: place one leg of the 10kΩ resistor
6. Other leg of 10kΩ to the **blue rail (GND)**

Ask after wiring: "What does the circuit look like right now — is BCM 25 HIGH or LOW?" → LOW. Button is open, 10kΩ is pulling it to GND. 0V = `False`.

**Script: Part A (state print):**

```python
import RPi.GPIO as GPIO
import time

BUTTON_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        print("Button:", state)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print("Done.")
```

Run it. Terminal prints `Button: False` repeatedly. Press the button. It prints `Button: True`. Release — back to `False`.

Ask: "What did we just do that every sensor in the CPT does?" → Read a pin state, check it in a loop, respond to it. IR line sensor, ultrasonic, photoresistor — same pattern.

**Script: Part B (button controls LED):**

Add the LED setup and output:

```python
import RPi.GPIO as GPIO
import time

BUTTON_PIN = 25
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        if GPIO.input(BUTTON_PIN):
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.05)

finally:
    GPIO.cleanup()
    print("Done.")
```

Run it. Press button — LED on. Release — LED off. Let it run for 10 seconds.

> "This is the entire structure of the CPT edge detection: read a sensor, if it's HIGH do something, if it's LOW do something else. The sensor on the robot is an IR line sensor instead of a button, but the code structure is identical."

---

### Pairs Wire Circuit + Run (25 min)

Distribute the button + 10kΩ kits. Students build their circuit and work through the lab.

**Before they touch a jumper:**

> "Find BCM 25 on the pinout reference. What physical pin is it?" → Physical pin 22. "Find 3.3V and a GND pin near it." → 3.3V on pin 1 or 17; GND on pin 20 is close to pin 22.

**Sequence to follow (in the lab note):**

1. **Part A:** Wire the button, run the print-state script, confirm `True`/`False` output changes on press
2. **Part B:** Add LED pin setup, change the loop to drive the LED from the button state

Circulate. Key checks:

1. Is the 10kΩ in the right place? One leg on the same breadboard row as BCM 25, other leg to GND — not bypassing the button, not to 3.3V
2. Are they using BCM 25 (physical pin 22) or some other pin?
3. 3.3V vs 5V: the button should connect to **3.3V (physical pin 1 or 17)**, not 5V (physical pin 2 or 4). The GPIO input threshold for the Pi is 1.8V — 5V won't damage it on a Pi 3B/4, but it's not correct practice and could stress a Pi 5 GPIO pin. Fix it before it becomes a habit.
4. Print output only — did they actually move to Part B?

**Common failures:**

| Symptom | Likely Cause |
|---------|-------------|
| Terminal prints `True` continuously even when not pressed | Button wired to 3.3V on both sides — no pull-down path. Check where the 10kΩ is going |
| Terminal prints `False` even when pressed | Button legs on same breadboard row (bridging the centre channel wrong). Rotate the button 90° |
| LED always on regardless of button | LED wired to 3.3V instead of BCM 18 — Day 5 regression |
| LED doesn't respond to button | `GPIO.setup(LED_PIN, GPIO.OUT)` missing, or BUTTON_PIN and LED_PIN swapped in the script |
| `Button: False` prints, nothing on press | Button not bridging the centre channel — one press row, one release row, but both legs on same side. Check orientation |
| Script crashes: `RuntimeError: This channel is already in use` | Previous session didn't cleanup. Add `GPIO.setwarnings(False)` before `setmode`, or re-image isn't needed — just run `GPIO.cleanup()` first: `python3 -c "import RPi.GPIO as GPIO; GPIO.cleanup()"` |

**Pair dynamics:** Both students should wire at least one connection. If one is always wiring and one is always typing, swap them mid-lab.

---

### Extension: Toggle with Debounce (6 min)

For pairs who finish Part B early.

> "Part B holds the LED on while the button is held. Now make it a toggle: first press turns the LED on, second press turns it off. The button press is an event, not a state."

Show this structure (do NOT write it for them — give the structure and let them fill it in):

```python
led_state = False

try:
    while True:
        if GPIO.input(BUTTON_PIN):          # press detected
            led_state = not led_state       # flip the state
            GPIO.output(LED_PIN, led_state)
            time.sleep(0.2)                 # wait out the bounce
        time.sleep(0.05)                    # main poll rate
```

Ask: "What does `led_state = not led_state` do?" → Flips the boolean: `True` → `False`, `False` → `True`.

Ask: "What happens if you remove the `time.sleep(0.2)` after detecting the press?" → The loop runs at 50ms intervals, and one physical press generates multiple `True` readings during the bounce window. The LED might toggle 3 times and end up where it started. Test it — remove the sleep and see what happens.

Ask: "Why does the main `time.sleep(0.05)` exist?" → Limits the CPU usage. A tight `while True:` with no sleep runs millions of iterations per second. 50ms polling is plenty fast for a button.

**Further extension:** Have the student wait for button **release** before resuming the loop — this is the most robust debounce:

```python
        if GPIO.input(BUTTON_PIN):
            led_state = not led_state
            GPIO.output(LED_PIN, led_state)
            while GPIO.input(BUTTON_PIN):   # wait for release
                time.sleep(0.01)
            time.sleep(0.05)                # settle after release
```

Ask: "What's the difference between the two approaches?" → First: fires on first detected press, locks out for 200ms regardless of what button is doing. Second: fires on first press, waits until button is actually released before it can fire again. Second is more correct for rapid pressing; first is simpler.

---

### Lab Completion Check + Shutdown (2 min)

Walk the room before the bell. For each pair, confirm:
1. Button pressed → LED on; button released → LED off (Part B working)
2. Ctrl+C → LED off (cleanup ran)

That's the completion mark. Part A (print-state) is a step toward Part B, not a separate deliverable.

---

### Watch For — Day 6

- **Students who skip Part A and go straight to Part B:** The print-state step confirms the circuit works before adding the LED layer. Students who skip it don't know if a failure is in the circuit or the code. Make them do Part A first.
- **10kΩ resistor orientation confusion:** The resistor goes from the BCM 25 row to GND — not from BCM 25 to 3.3V (that's a pull-up, which inverts the logic and confuses students). Confirm: which end of the resistor connects to GND?
- **Button placed parallel to the channel instead of spanning it:** Tactile buttons have 4 legs — they span the breadboard centre channel. Both legs on one side are internally connected; the button connects the two sides. Students sometimes place it along one rail, shorting the input, or entirely in one half with no connection possible. Check the orientation.
- **3.3V vs 5V:** GPIO input pins on Pi 3B/4 can tolerate 5V input briefly, but it's wrong practice. Pi 5 GPIO is more sensitive. Fix immediately. This habit will carry into the CPT.
- **Bounce visible during toggle extension:** Good. Don't fix it for them — ask them what they observe, and whether the 200ms sleep makes it better. This is the lab's teachable moment for debounce.
- **Students proud of the working button/LED and not moving to the code explanation:** Ask: "Walk me through the circuit — what happens to the voltage at BCM 25 when you press the button?" They should be able to explain LOW → HIGH, resistor to GND, etc. If they can't, spend 2 minutes on it. The CPT sensor circuit is identical.
- **Groups where Part B script has the conditional backwards:** `if GPIO.input(BUTTON_PIN) == False:` → LED on. This is an inverted pull-up pattern from an online tutorial. It works but means the LED is on when the button is NOT pressed. Ask: "Does the circuit match the code?" Check their 10kΩ placement — pull-up vs pull-down is almost always the root cause.

---

## Connector: Day 6 → Day 7

Day 7: GPIO Lab 3 — H-Bridge + Motors. Adds:
- New hardware: L293D (DIP-16 chip), 1× TT gearbox motor (loose on desktop — no chassis yet)
- New pins: direction (IN1/IN2) and enable (EN1) pins wired to the L293D
- New concept: H-bridge motor driver — why you can't drive a motor directly from a GPIO pin (current limits, back-EMF)
- The software pattern (GPIO.output, conditional) is exactly what they wrote today — the pins just drive a motor driver instead of an LED

Day 8: Lab 3 continues with a second motor and PWM speed control (`GPIO.PWM`, duty cycle). Both motors loose on the desktop — rolling chassis arrives at CPT time.

Keep button circuits intact if space allows on the breadboard — Extension B in Lab 3 connects the Lab 2 button to motor control. If breadboards are full, the button circuit can be removed; the skills are established.
