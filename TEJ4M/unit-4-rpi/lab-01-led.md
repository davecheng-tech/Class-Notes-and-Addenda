# Lab 1: LED Digital Output

**Day 5** — Wire a real LED circuit and run your blink script. This is the first time code you wrote produces something you can see and touch.

**Hardware:** RPi + CanaKit cobbler, breadboard, 1–2 LEDs, 220Ω resistor(s), M-F jumpers

---

## Circuit

![LED circuit diagram — GPIO 18 through 220Ω resistor to LED, cathode to 3V3 GND rail](./images/lab-01-led-circuit.png)

```
BCM 18 (cobbler pin)  →  220Ω resistor  →  LED anode (longer leg)
                                             LED cathode (shorter leg)  →  blue rail (GND)
```

**Before wiring anything:** look up BCM 18 on your pinout reference. Find it on the cobbler label. Confirm the physical pin number with your partner before you place a single jumper.

> [!NOTE]
> The CanaKit cobbler routes ground to the blue (−) rails on both sides of the breadboard. You do not need a separate jumper back to a GND pin on the Pi — connect your LED cathode directly to either blue rail. Both are GND.

---

## Wiring Steps

Pi should be running with no script active, or powered off. GPIO pins in their default (LOW) state before wiring is good practice.

1. Locate **BCM 18** on the cobbler. Run a jumper from that pin to a free row on the breadboard.
2. Place a **220Ω resistor**: one leg in the same row as the jumper, other leg in a new row.
3. Place the **LED**: anode (longer leg) in the same row as the resistor's second leg, cathode (shorter leg) in a new row.
4. Run a jumper from the cathode row to the **blue rail** (either side — both are GND).

Double-check with your partner:
- Resistor present between GPIO pin and LED? ✓
- LED anode toward the resistor, cathode toward ground? ✓
- BCM 18 confirmed on pinout reference, not guessed? ✓

---

## Run Your Script

Confirm the import in your script is the real library, not the simulator:

```
head -2 ~/gpio/blink.py
```

Should show `import RPi.GPIO as GPIO`. If it still says `gpio_sim`, open with nano and fix it.

Run:

```
python3 ~/gpio/blink.py
```

The LED blinks. Press **Ctrl+C** to stop — the LED should go off (cleanup ran).

**If nothing happens:** see the troubleshooting table below before touching the wiring.

---

## Troubleshooting

| Symptom | Likely cause |
|---------|-------------|
| Script runs, LED does nothing | Wrong pin, or LED in backwards — check pinout, then swap LED direction |
| LED stays on permanently, doesn't blink | LED wired to the red (3V3/5V) rail instead of a GPIO pin |
| `ModuleNotFoundError: No module named 'gpio_sim'` | Import wasn't changed — open with nano, fix the import line |
| `ModuleNotFoundError: No module named 'RPi'` | RPi.GPIO not installed — confirm you're SSH'd into the Pi, not on your laptop |
| `RuntimeError: No access to /dev/gpiomem` | Not running as `pi` — check with `whoami` |
| LED very dim | Check for double-resistor, or LED wired backwards (dim instead of off) |

> [!TIP]
> The most common mistake is a backwards LED. If the script runs cleanly and the LED does nothing, swap the LED direction first — 9 times out of 10 that fixes it.

---

## Extensions

### A — Second LED, Alternating Blink

Wire a second LED on **BCM 23** (check pinout for physical pin). Same circuit: cobbler pin → 220Ω → LED anode → cathode → blue rail.

Modify your script to alternate — LED A on while LED B is off, then swap. Your Day 3 Part B script already does this with `gpio_sim`; the only change is the import.

---

### B — Modular Blink Function

Refactor your script so that blinking is a reusable function:

```python
def blink(pin, times, delay=0.1):
    for _ in range(times):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
```

`delay` has a default value — `blink(LED_A, 3)` uses 0.1s; `blink(LED_A, 3, 0.5)` uses 0.5s.

Use this function in your main loop instead of writing out the HIGH/sleep/LOW sequence each time. Then add a startup sequence in your setup code — call `blink(LED_A, 2, 0.05)` before entering the main loop as a "ready" flash.

---

### C — Metronome: 4/4 Time (2 LEDs)

Wire a red LED on **BCM 18** and a green LED on **BCM 23**. Write a metronome: red flashes on beat 1, green flashes on beats 2, 3, and 4.

```python
BPM = 120
BEAT = 60 / BPM   # seconds per beat
FLASH = 0.05      # LED on-time per flash

RED = 18
GREEN = 23

def beat(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(FLASH)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(BEAT - FLASH)

try:
    while True:
        beat(RED)
        beat(GREEN)
        beat(GREEN)
        beat(GREEN)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print("Done.")
```

Try changing `BPM` — 60 is slow, 180 is fast. What happens if `BPM` is high enough that `BEAT - FLASH` goes negative?

---

### D — Metronome: 4/4 Time (4 LEDs)

Wire four LEDs — one per beat — on **BCM 18, 23, 24, 25**. Each LED flashes on its assigned beat.

```python
BPM = 120
BEAT = 60 / BPM
FLASH = 0.05

LEDS = [18, 23, 24, 25]

# setup
for pin in LEDS:
    GPIO.setup(pin, GPIO.OUT)

def beat(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(FLASH)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(BEAT - FLASH)

try:
    while True:
        for pin in LEDS:
            beat(pin)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print("Done.")
```

The `for pin in LEDS` loop replaces four separate `beat()` calls — adding a 5th beat means adding one pin to the list. Try changing the list order, or replacing one pin with `None` and skipping it with a conditional to create a rest on a particular beat.

---

## Optional: Suppress the Ctrl+C Traceback

With a bare `try / finally`, pressing Ctrl+C prints a traceback after `Done.` — the cleanup still runs correctly, but the output is noisy. Add `except KeyboardInterrupt: pass` between the two blocks:

```python
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print("Done.")
```

Exit now prints only `Done.` — no traceback. `finally` still runs guaranteed.

---

## Lab Completion

Walk around check before the bell:

1. LED blinks in sync with the script ✓
2. Ctrl+C → LED goes off (`GPIO.cleanup()` ran) ✓

Extension credit: demonstrate any of A–D that you completed.
