# CPT Reference — 2024–25 Team 3

Simpler robot — one light sensor, no ultrasonic, no opponent detection.
Representative of a guided-build team that took the chassis and built functional autonomous code without going further.
Hardware: Pi (model unknown), H-bridge, 1× GL5528 photoresistor (RC timing), start button, indicator LED.

---

## Notable at a Glance

- **Edited directly on the Pi in vim** — `.swp` swap files in `PracticeCmmds/` confirm this (`lsensor.py.swp`, `twowheels.py.swp`). They SSH'd in and worked entirely in the terminal, no SCP from laptops.
- **Hungarian notation** throughout `code.py`: `intMotorPins`, `fltStartTime`, `fnMoveForward` — unusual in Python, but internally consistent. Likely a convention from a Java or C background (ICS student?).
- **Threading in practice files** — independently discovered `threading` to run the light sensor concurrently with motor control. Not taught. Remarkable for this tier.
- **`launcher.sh`** exists but is empty — planned to auto-start the battle code on boot, didn't finish.
- **`ledblink.py`** is the most thoroughly commented early-lab file across all three teams. Near tutorial quality.

---

## Practice Files (`PracticeCmmds/`)

Clear chronological progression — name progression doesn't make sense until you realise they were naming files by what they tested, not in sequence.

| File | What it is | Cleanup? |
|------|-----------|---------|
| `ledblink.py` | LED blink — heavily commented, explains BCM vs BOARD | ✓ try/finally |
| `button.py` | Button reads and prints value, nothing else | ✗ bare while |
| `buled.py` | Button toggles LED via integer toggle logic (0/1) | ✗ bare while |
| `wheels.py` | Two-pin motor test, forward/backward | ✗ bare while |
| `bheels.py` | RC timing sensor — **crashes immediately** (`import RPI.GPIO`, capital RPI) | ✓ try/finally (unreachable) |
| `lights.py` | RC timing sensor — copied from pimylife.com tutorial (has `__author__` attribution) | ✓ try/finally |
| `sensor.py` | Same RC timing, stripped of attribution | ✓ try/finally |
| `trio.py` | Button toggles motors + LED, with debounce | ✓ try/finally |
| `quad.py` | Button + motors + LED + light sensor thread (prints only) | ✓ try/finally |
| `all.py` | Threading with motor suspension on light reading — **truncated mid-line** | incomplete |
| `stop.py` | Threading with `daemon=True`, `suspended_due_to_light` global flag — most complete version | ✓ try/finally |

**Threading arc (`trio` → `quad` → `all` → `stop`):** These four files show the team independently working out how to run a light sensor concurrently with motor control using `threading.Thread`. `all.py` is an incomplete attempt that cuts off at `suspended_due`. `stop.py` is the working version — daemon thread, `motor_running` and `suspended_due_to_light` global flags, motor suspension when light threshold is exceeded. None of this was in the lab instructions. They found `threading` and figured it out.

**`bheels.py`:** `import RPI.GPIO` (capital R, P, I) — Python module names are case-sensitive. This file crashes on line 1 with `ModuleNotFoundError`. The `try/finally` inside is unreachable. They probably saw a tutorial with the wrong capitalisation and never diagnosed why it didn't run.

---

## Final Code (`code.py`)

The most structurally complete final code of the three teams.

**What it does well:**
- All pin assignments as named constants at the top
- Motor pins in a list, setup via loop — `fnStopMotors` also uses the list (`for intPin in intMotorPins: GPIO.output(intPin, GPIO.LOW)`) — single source of truth
- `GPIO.PUD_UP` pull-up on the button — the only team to configure this correctly. Means the button reads HIGH at rest, LOW when pressed. Logic in `code.py` handles this correctly.
- Full button start sequence: wait for press AND release before starting (edge-triggered, not level-triggered). Prevents accidental re-trigger.
- 5-second countdown with LED indicator before autonomous begins
- Edge recovery with **fallback**: turn left to find black, timeout after 5 seconds, then try turning right. No other team implemented a fallback direction search.
- `fnStopMotors()`, LED off, and `GPIO.cleanup()` all in `finally` — most complete cleanup of the three teams

**Limitations:**
- One sensor only — no directional edge detection, no per-corner logic
- No ultrasonic / no opponent detection — robot charges forward whenever it's not on an edge
- No opponent seeking or turning strategy — just "not white → forward"

**The Hungarian notation** (`fn` prefix for functions, `int`/`flt` for variables) is consistent throughout and not incorrect — just very un-Pythonic. If this was an ICS student applying Java conventions, it makes sense. Worth a brief mention in a future code review exercise: "Python convention is `snake_case` without type prefixes."

---

## What This Tells You for Future CPTs

- The vim + SSH workflow (editing directly on the Pi) is viable and some students will do it. The `.swp` files are a sign — if a student's Pi crashes or SSH drops mid-edit, the swap file is recovery. Not worth teaching, but worth knowing when you see `.swp` files in a directory.
- `import RPI.GPIO` (capital) is a plausible mistake, especially from tutorials. The error message (`ModuleNotFoundError: No module named 'RPI'`) is not immediately obvious — students may think the library isn't installed. Worth one sentence in the lab: "Module names are case-sensitive: `RPi.GPIO`, not `RPI.GPIO`."
- `GPIO.PUD_UP` is a useful pattern for buttons (no external pull-down resistor needed) — team 3 used it correctly. Worth introducing in Lab 2 and saving the external resistor for the explanation of why it's needed, not the lab wiring.
- The threading discovery is notable — two files in, they're writing daemon threads and global state flags. If you have students at this level again, threading is a legitimate CPT extension goal: sensor in one thread, motor logic in another. Cleaner than the polling loop.
- The fallback direction search in `code.py` (`turn left, timeout, try right`) is the most robust edge-recovery logic of the three teams despite having the simplest hardware. Algorithm quality ≠ hardware complexity.
