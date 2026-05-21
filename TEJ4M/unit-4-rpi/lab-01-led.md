# Lab 1: LED Digital Output

**Day 5** — Wire a real LED circuit and run your blink script. This is the first time code you wrote produces something you can see and touch.

**Hardware:** RPi + CanaKit cobbler, breadboard, 1–2 LEDs, 220Ω resistor(s), M-F jumpers

---

## Circuit

<!-- Fritzing diagram goes here -->

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

## Extension: Second LED, Alternating Blink

Wire a second LED on **BCM 25** (check pinout for physical pin). Same circuit: cobbler pin → 220Ω → LED anode → cathode → blue rail.

Modify your script to alternate — LED A on while LED B is off, then swap. Your Day 3 Part B script already does this with `gpio_sim`; the only change is the import.

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

Extension credit: two LEDs alternating correctly.
