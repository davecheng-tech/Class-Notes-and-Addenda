# CPT Reference — 2024–25 Cohort

Student working files and final project from the 2024–25 TEJ4M sumo robot CPT.
Hardware: Pi 4B, L293D H-bridge, GL5528 photoresistor (RC timing), HC-SR04 ultrasonic, LED floor illuminator.

---

## Final Project (`final-project/`)

Three-module structure: `motor.py` + `light.py` imported into `main.py`. Clean separation of concerns — this is exactly the Part D lab structure in practice.

**`motor.py`** — 4 GPIO pins (BCM 20/21/23/24) driving L293D. `moveForward`, `moveBackward`, `turnLeft`, `turnRight` all take a duration in seconds, call `stop()` after the sleep. No PWM — full speed only.

**`light.py`** — RC timing photoresistor on BCM 22, LED on BCM 16, button on BCM 19, HC-SR04 on BCM 17/18. Key functions: `lightSensorTimer()` (count loop, not wall time), `getLightSensor()` (divides by 100 and rounds), `isBlack()` (threshold > 5), `getDistance()` (pulse timing × 17150 for cm).

**`main.py`** — Two autonomous strategies. `autonomous()`: edge detection only (see white → back up + random turn). `betterAuton()`: adds 5-second start delay, initial forward movement to clear the edge, then distance-gated opponent charging (< 60cm → charge, else → turn and scan).

**`keyboard.py`** — `curses`-based arrow-key manual control. Used for testing and driving during non-battle time. Note: **has a bug** — reassigns `motor.leftForward = 21` and `motor.leftBackward = 20`, which is the opposite of `motor.py`'s definitions (20 and 21 respectively). Left motor directions are inverted in keyboard mode.

**Known issues in final project:**
- `GPIO.setmode(GPIO.BCM)` called redundantly at the top of `light.py`, `motor.py`, and `main.py`
- `getDistance()` has no timeout — if the HC-SR04 echo never arrives, the while loop blocks forever
- `isBlack()` threshold of 5 is hardcoded; recalibration requires editing source
- RC count loop is CPU-load-sensitive — values drift when running motor + sensor simultaneously
- `keyboard.py` left/right motor pin swap (see above)

---

## Student Working Files

### Aiden

**`led.py`** — First clean blink script. Has `try/finally` with `GPIO.cleanup()`. Uses `except KeyboardInterrupt` rather than bare `finally` — slightly less robust (doesn't catch errors, only Ctrl+C) but shows the pattern was understood.

**`buttonled.py`** — Button (BCM 19) controls LED (BCM 16). **No `try/finally`** — the loop just runs bare. If Ctrl+C mid-loop, GPIO state is undefined. Good example to show students: what happens when you skip cleanup on a robot vs on a laptop.

**`motortesting.py`** — Four motor pins set to specific HIGH/LOW state and left there in a `while True` with no `stop()` and no `try/finally`. Motors spin forever until power is cut. **Classic dangerous pattern** — useful to show as a counterexample: "this is what happens if you wire motors and forget cleanup."

---

### Ethan

Ethan's files are the clearest learning arc in the cohort. Three iterations of the same problem — reading the photoresistor — each building on the last.

**`lightsensor.py` — First attempt.** Discharges the capacitor, switches to input, then immediately reads `GPIO.input()` once and prints 0 or 1. **Doesn't count — just samples the pin once.** He's done the discharge but hasn't figured out the timing loop yet. No `try/finally`. The output would be almost random because the capacitor hasn't finished charging.

**`lightsensor2.py` — RC timing discovered.** Adds `rc_time()` with the count loop (`while GPIO.input == LOW: count += 1`). Now measuring charge time correctly. Has `try/finally` with `GPIO.cleanup()`. `getLightSensor()` still calls `rc_time()` twice — wastes one measurement and doubles the discharge cycle per reading, but works.

**`lightMethod.py` — Refactored into a module.** Functions take pin numbers as parameters instead of using globals. Adds `controlLight()` to drive the illuminator LED. Main loop uses the light sensor to toggle the LED — basically a working light-reactive circuit. Has `try/finally`. `controlLight()` takes `"1"`/`"0"` strings instead of booleans — a small design smell but functional.

**`firstMain.py`** — Assembled module version: imports `lightMethod` functions, adds a `try/finally` main loop with autonomous light-reactive behaviour. This is the direct precursor to `Main/light.py` — the function names and logic carry through almost unchanged.

---

### Ryan

**`button.py`** — Button (BCM 19) toggles LED (BCM 16). Clean structure: named constants, `GPIO.setup` before the loop, `try/finally` with `GPIO.cleanup()`. The cleanest early-lab script in the cohort.

**`motor.py`** — Motor setup and direction functions. No `time.sleep` or `stop()` inside the movement functions (unlike the final `motor.py`) — movements run until the caller decides to stop. No `try/finally`. Likely a starting point that was merged into the final project's `motor.py` with `stop()` added.

---

## What This Tells You for Future CPTs

- The RC timing approach (capacitor + count loop) works and students can figure it out with minimal guidance if given the right starting question ("how would you measure resistance without a multimeter?")
- The modular structure (motor.py / sensor.py / main.py) emerges naturally when students start sharing code — worth scaffolding explicitly in Day 3 Part D rather than waiting for them to discover it
- `try/finally` is absorbed well; the main failure mode is students who write working code fast and skip the structure because it runs fine in testing (Aiden's `buttonled.py`, Ryan's `motor.py`)
- The biggest quality gap between early and final code is **pin assignment consistency** — hardcoded numbers vs named constants, and pin numbers changing between files. Worth emphasising named constants from Day 1 of labs
- `keyboard.py` with curses is genuinely impressive — if you have FTC-level students again, suggest this as a test harness early; it makes motor debugging much faster than guessing duration values
