# CPT Reference — 2024–25 Sumo Robot Cohort

Three robot codebases from the 2024–25 TEJ4M CPT. Archived here as teacher reference: calibrating expectations, identifying common failure modes, and finding teaching examples. All robots competed.

---

## Quick Comparison

| | Team 1 | Team 2 | Team 3 |
|-|--------|--------|--------|
| **Skill level** | High (likely FTC student driving) | Mid-low | Mid |
| **Code structure** | Modular (`motor.py`, `light.py`, `main.py`) | Monolithic, numbered files | Monolithic, but clean functions |
| **Sensors** | 1 photoresistor + HC-SR04 | 4 photoresistors + HC-SR04 | 1 photoresistor |
| **Opponent detection** | ✓ HC-SR04 distance threshold | ✓ HC-SR04 distance threshold | ✗ |
| **Start button** | ✓ with 5s delay | ✓ with 5s delay | ✓ with 5s delay + edge detection |
| **Manual control** | ✓ curses keyboard mode | ✗ | ✗ |
| **`GPIO.cleanup()` correct** | Mostly (keyboard.py bug) | ✗ (missing parens throughout) | ✓ |
| **`try/finally`** | ✓ | Mixed | ✓ |
| **Notable reach** | curses keyboard driver | 4-sensor per-corner logic | Threading; fallback direction search |
| **Source folder** | `team-1/` | `team-2/` | `team-3/` |

---

## Team 1 — `team-1/`

**Highest skill level.** Clean three-module architecture from fairly early in development. Almost certainly driven by a student with FTC or ICS4U experience.

**Final project:** `final-project/` — `main.py` imports `motor.py` and `light.py`. Two autonomous strategies (`autonomous` and `betterAuton`), the latter adding opponent detection via HC-SR04 and a 5-second start delay. `keyboard.py` adds curses-based arrow-key manual control for testing — sophisticated and practical.

**Student working files:** `student-working-files/` — Three students' lab progressions.
- **Ethan's light sensor arc** (`lightsensor.py` → `lightsensor2.py` → `lightMethod.py` → `firstMain.py`) is the standout teaching example across all three teams: four files documenting a student figuring out RC timing from scratch, then refactoring into a module. Use this to calibrate what independent discovery looks like.
- **Aiden's `buttonled.py`** (no cleanup) vs `led.py` (has cleanup) from the same student illustrates that knowing the pattern and applying it consistently are different things.
- **Aiden's `motortesting.py`**: motors set HIGH in a `while True` with no `stop()` and no cleanup — the dangerous pattern. Useful counterexample.

**Known bugs:**
- `keyboard.py` has a left/right motor pin swap — left motor directions inverted in keyboard mode
- `getDistance()` in `light.py` has no timeout on the HC-SR04 echo loop — blocks forever on a missed pulse
- `GPIO.setmode(GPIO.BCM)` called redundantly in three files

---

## Team 2 — `team-2/`

**Mid-low skill level.** Numbered monolithic files (`gpio.py` → `gpio2.py` → …). No module separation at any stage. But the hardware ambition was the highest of the three: 4 photoresistors with per-sensor calibration, HC-SR04, directional edge recovery.

**Final code:** `BattleCode.py` — all inline, 280 lines. Per-corner sensor thresholds calibrated individually (different values for each of the 4 sensors). Motor sequences differ based on which corner detected the edge. `BattleCodetest.py` is a late refactor — named constants, movement functions, MAX_COUNT cap on RC loop — likely AI-assisted but cleaner.

**Most instructive bugs for teaching:**

- **`GPIO.cleanup` without parentheses** — appears in 5 files including `gpiocleaner.py`, a script they wrote specifically to fix a stuck GPIO state (which therefore also didn't work). Silent failure — no error, pins just don't reset. Add to Day 5 Watch For.
- **`except KeyboardInterrupt or startup == False:`** — Python misconception: `except` takes an exception class, not a boolean. Works by accident because `KeyboardInterrupt or <anything>` evaluates to `KeyboardInterrupt`. 
- **`gpiouss.py`** has timeout handling on the HC-SR04 (returns `None` on timeout, validated at call site) — quality jump significant enough to suggest AI or a much better tutorial. Better implementation than team 1's.

---

## Team 3 — `team-3/`

**Mid level — simpler robot, strongest final code structure.** One sensor, no opponent detection. Representative of a guided-build team that got a working autonomous robot without hardware extensions. Best `try/finally` hygiene of the three.

**Practice files:** `PracticeCmmds/` — 11 files showing a clear lab progression. Edited directly on the Pi via vim (`.swp` swap files present). Notable:
- `ledblink.py` — the most thoroughly commented early-lab file across all three teams. Near tutorial quality.
- Threading arc: `trio.py` → `quad.py` → `all.py` (truncated) → `stop.py` — they independently discovered `threading` to run the light sensor concurrently with motor control. `stop.py` has a daemon thread with `motor_running` and `suspended_due_to_light` global flags.
- `bheels.py` — `import RPI.GPIO` (wrong capitalisation), crashes on line 1.

**Final code:** `code.py` — Hungarian notation (`intMotorPins`, `fnMoveForward`, `fltStartTime`), motor pins in a list with loop-based setup and stop, `GPIO.PUD_UP` pull-up (only team to use this — no external resistor needed). Edge recovery has a **fallback**: turn left until black found, 5-second timeout, then try right. Most robust edge logic of the three despite fewest sensors.

**Incomplete:** `launcher.sh` exists but is empty — they planned auto-start on boot, didn't finish.

---

## Cross-Team Teaching Examples

Use these when preparing labs, anticipating student mistakes, or calibrating the CPT rubric.

### Bugs to pre-empt in labs

| Bug | Where | Fix to teach |
|-----|-------|-------------|
| `GPIO.cleanup` without `()` | Team 2, 5 files | "Function reference vs function call — no parens = nothing happens" |
| `import RPI.GPIO` (capitalisation) | Team 3, `bheels.py` | "Module names are case-sensitive: `RPi.GPIO`" |
| `except X or condition:` | Team 2, 2 files | "`except` takes an exception type, not a boolean expression" |
| HC-SR04 echo loop with no timeout | Team 1 + Team 2 | "What happens if the pulse never returns? Add a timeout." |
| No cleanup when motors running | Team 1 `motortesting.py`, Team 2 multiple | `try/finally` lesson — make it physical: motors keep spinning |

### Positive examples to reference

| Pattern | Where | Use for |
|---------|-------|---------|
| RC timing figured out from scratch | Team 1, Ethan's arc | Show what independent discovery looks like; calibrate guided vs open tasks |
| Per-sensor calibration | Team 2, `BattleCode.py` | Show that hardware variance is real; calibrate each sensor individually |
| Fallback direction search | Team 3, `code.py` lines 82–100 | Show algorithm thinking without hardware complexity |
| Threading (sensor + motor concurrently) | Team 3, `stop.py` | CPT extension suggestion for advanced students |
| curses keyboard driver | Team 1, `keyboard.py` | CPT extension — manual testing harness |
| `GPIO.PUD_UP` on button | Team 3, `code.py` | Cleaner button wiring — introduce in Lab 2 |
| `fnStopMotors` via pin list loop | Team 3, `code.py` | Single source of truth for pin lists |

### Skill range calibration

All three teams competed. The spread from team 1 (modular, keyboard driver, curses) to team 3 (one sensor, clean structure, threading attempted) to team 2 (4 sensors, inline, persistent cleanup bug) maps well onto your expected class composition: FTC-level, ICS-background, and guided-build-only students. No team produced uncompeteable code. The minimum viable bar — move, detect edge, respond, run without SSH — is achievable by all three.
