# CPT Reference — 2024–25 Team 2

Lower skill level than team 1 based on code structure. No student names on files.
Hardware: Pi (model unknown), L293D-style H-bridge, 4× GL5528 photoresistors (RC timing), HC-SR04 ultrasonic, start/stop button, indicator LED.

---

## Progression

Files are numbered iterations rather than modules — `gpio.py` through `gpio5.py` plus purpose-named files for specific tests. No modular separation at any point until `BattleCodetest.py` at the very end.

| File | What it is |
|------|-----------|
| `gpio.py` | First LED output test |
| `gpio2.py` | Button controls LED — no cleanup |
| `gpio3.py` | RC timing light sensor — clean, has `try/finally` |
| `gpio4.py` | Motor direction test — 2 pins |
| `gpio42M.py` | 4-motor + RC sensor + button integration — early draft of BattleCode |
| `gpio5.py` | Same as gpio42M but with sensor debugging prints, no motor movement |
| `gpiocleaner.py` | Attempted one-shot cleanup script — **doesn't work** (see below) |
| `gpiosensor.py` | HC-SR04 ultrasonic, likely copied from tutorial |
| `gpiouss.py` | Improved HC-SR04 with timeout handling — quality jump, possibly AI-assisted |
| `button2motor.py` | Button controls single motor pin — no cleanup |
| `test4sensor.py` | RC timing print loop for sensor calibration (pins 6 and 22) |
| `BattleCode.py` | Final autonomous code — monolithic, 4 sensors, per-sensor thresholds |
| `BattleCodetest.py` | Refactored BattleCode — named constants, movement functions, MAX_COUNT cap |

---

## Persistent Bugs

**`GPIO.cleanup` without parentheses** — appears in `gpio.py`, `gpio4.py`, `gpio42M.py`, `gpio5.py`, `gpiocleaner.py`. A reference to the function, not a call. Cleanup never ran in most of their test scripts.

`gpiocleaner.py` is the clearest symptom: they were stuck with motors or pins in a bad state, wrote a dedicated one-shot script to fix it, and it also doesn't work for the same reason. Didn't notice because there's no error — Python is happy to evaluate a function reference and do nothing with it.

**`except KeyboardInterrupt or startup == False:`** — in both `gpio42M.py` and `BattleCode.py`. Python's `except` takes an exception class. `KeyboardInterrupt or startup == False` evaluates to `KeyboardInterrupt` (truthy object wins the `or`), so this accidentally works — but the `startup == False` condition is never evaluated. The intent was to also catch the case where the button stops the robot, but that's not how `except` works.

---

## What They Did Well

**Four photoresistors with per-corner logic.** `BattleCode.py` has front-left, front-right, back-left, back-right sensors and distinct motor sequences for each. Front-left sees white → back up, rotate right, move forward. This is real directional edge recovery — more sophisticated than team 1's single sensor + random turn.

**Per-sensor calibration.** Each sensor has its own hardcoded threshold:
```python
frontRightSensorBlackReading = 35000
frontLeftSensorBlackReading = 70000
backRightSensorBlackReading = 40000
backLeftSensorBlackReading = 20000
```
These aren't guesses — `test4sensor.py` shows they ran calibration reads per pin and recorded the values. The different numbers per sensor reflect real variance between photoresistors and their individual mounting positions.

**`gpiouss.py` ultrasonic timeout.** Returns `None` if the echo never arrives (40ms timeout per phase). Better than team 1's implementation which would block forever on a missed pulse. Quality jumps significantly here — likely from a more sophisticated tutorial or AI assistance.

**`BattleCodetest.py` — late-stage refactor.** Named constants for all 14 pins, named movement functions (`move_forward`, `turn_left`, etc.), `MAX_COUNT = 1000000` cap on RC loop (prevents infinite hang), `stop_motors()` in `finally`. The `GPIO.cleanup` parens bug is also fixed. This is likely AI-assisted but represents a genuine improvement — the student understood what needed fixing even if they needed help doing it.

**`buffer` state flag.** Prevents the button from re-triggering startup immediately after a stop. Small but shows they thought through the button debounce problem at the state machine level.

---

## What This Tells You for Future CPTs

- The `GPIO.cleanup` missing-parens bug is a silent failure that even the students didn't notice in testing. Worth making it an explicit "watch for" in the lab — add it to the Day 5 Watch For list.
- The numbered-file progression (`gpio.py`, `gpio2.py`…) is a signal that a pair doesn't feel confident enough to edit and save — they're keeping every version as insurance. Teaching `git` or even just "you can always undo with Ctrl+Z" might address this.
- Four sensors is achievable even for a weaker team if they have time to calibrate. The hardware ambition was higher than team 1; the code structure was lower.
- `except SomeException or some_condition:` is a believable mistake for students who learned `if condition or other_condition:` and assumed `except` works the same way. Worth a brief explicit note in the lab: "except takes one thing — an exception type."
- The late-stage AI-assisted refactor (`BattleCodetest.py`) is a net positive — cleaner code is cleaner code. The question for assessment is whether they understand what changed and why. The oral demo component handles this.
