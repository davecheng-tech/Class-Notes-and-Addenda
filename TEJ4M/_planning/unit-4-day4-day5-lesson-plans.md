# Unit 4: Days 4–5 Lesson Plans — First SSH + LED Lab

**Day 4 — May 21 (Thu):** RPi first boot, SSH in, file transfer, run first script on real hardware  
**Day 5 — May 22 (Fri):** GPIO Lab 1 — LED digital output, BCM pin numbering, physical wiring

These plans assume:
- Students completed Days 2–3 (Python for GPIO, `gpio_sim` blink script)
- All Pis imaged by teacher before class: RPi OS Lite, hostname pre-set (`rpi-01` etc.), SSH enabled, WiFi pre-configured to YCBYOD — no in-class imaging needed
- SSH password: `raspberry` (set at image time via Imager OS Customisation)
- Pairs: 2 students per Pi throughout
- Period length: **70 minutes**
- Pis shut down at end of each class; SD cards stay in Pis stored on a shelf

**Student notes to have ready:**  
- `unit-4-rpi/02-python-for-gpio.md` (already distributed)  
- `unit-4-rpi/03-rpi-setup.md` ← needs to be written before Day 4  
- `unit-4-rpi/lab-01-led.md` ← needs to be written before Day 5

---

## Before Day 4 — Setup Checklist

**Imaging (do at home before class):**
- [ ] Flash all SD cards with RPi OS Lite using Raspberry Pi Imager
  - OS Customisation (gear icon): hostname = `rpi-01`, `rpi-02`…; SSH enabled (password auth); user `pi` / password `raspberry`; WiFi SSID = `YCBYOD` + school password; country = `CA`
  - Save settings as default in Imager — each subsequent card is one click
- [ ] Boot each Pi at home, confirm it connects to your home WiFi (or a hotspot), confirm SSH works
- [ ] Re-image any cards that don't connect cleanly

**Day-of:**
- [ ] Arrive early, power on all Pis, confirm they're on YCBYOD
- [ ] Run network scan to build the IP list (see below), post to Google Classroom before students arrive

**Finding Pi IPs on YCBYOD (run from your Lubuntu Chromebook):**
```bash
# Find your subnet first:
ip route | grep proto
# Then scan (replace 192.168.x with your actual subnet):
sudo nmap -sn 192.168.x.0/24 | grep -A1 "rpi-"
```
If avahi/mDNS works on YCBYOD (worth testing — it may not on a school network), students can skip IPs entirely and SSH as `ssh pi@rpi-01.local`. Test this from a student Chromebook before Day 4.

**Critical pre-check:** Confirm a student Chromebook can SSH to a Pi on YCBYOD. School BYOD networks sometimes enable **client isolation** (devices on the same SSID can't talk directly). If SSH is blocked, you need to escalate to IT before Day 4 — there is no workaround.

- [ ] Mains power adapters confirmed (one per Pi): USB-C for Pi 4/5, micro-USB for Pi 3B
- [ ] Know which model each group has — 3B/4/5 differ in power connector but GPIO is identical

---

## Day 4 — SSH In, File Transfer, First Real Script

**Goal:** Every pair SSHes into their Pi, gets their blink script on it, swaps the import, and runs it. No wiring today — output is terminal text. Day 5 adds the LED.

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Distribute hardware, power on Pis |
| 5–20 | Demo: SSH in (teacher on projector), filesystem orientation |
| 20–35 | Students SSH in — both partners connected simultaneously |
| 35–40 | `who` / `w` — two sessions, one machine; Unit 2 callback |
| 40–52 | File transfer + import swap + run script |
| 52–64 | Service audit + 3 safe disables as a class (Unit 2 callback) |
| 64–68 | `free -h` / process count before/after comparison |
| 68–70 | Preview Day 5 + clean shutdown |

---

### Distribute Hardware + Power On (5 min)

Hand each pair:
- 1× RPi (any model)
- 1× power adapter (correct connector for their model)
- 1× SD card (already imaged — insert it now if not pre-inserted)

Tell students: "Plug in the power adapter. The Pi boots without a monitor — there's no screen, that's intentional. Give it 30 seconds."

While they wait: ask what they expect to see. Answer: nothing visible. Say: "The OS is running headlessly — terminal only, over the network. That's exactly how a robot or server runs in production."

---

### Demo: SSH In + Filesystem Orientation (15 min)

Do this on the projector with one Pi assigned to you. Students watch first, then replicate.

**SSH in:**

```bash
ssh pi@<IP address>
```

Password: `raspberry`. Accept the fingerprint warning ("yes"). Students will see the Pi welcome banner.

Explain: "We're now at a terminal prompt running on the Pi itself — not on our laptop. Every command I type runs on the Pi."

**Quick orientation — run these with commentary:**

```bash
pwd          # where are we? → /home/pi
ls           # what's here? → empty home dir
uname -a     # what machine? → Linux, ARM processor — not the laptop
python3 --version   # Python is installed
```

Ask: "What does `uname -a` tell us that `pwd` doesn't?" → Which machine the commands are running on. The architecture line (`aarch64` or `armv7`) confirms it's the Pi's ARM CPU, not x86.

Create a working folder:

```bash
mkdir gpio
cd gpio
ls
```

Say: "This is where you'll keep your GPIO scripts for the rest of the unit. All your lab scripts live here."

---

### Students SSH In — Both Partners (15 min)

Post or display the IP list. Each pair uses the IP assigned to their Pi.

**First partner** SSHes in from their laptop:
```bash
ssh pi@<their IP>
```

Password: `raspberry` (nothing echoes — normal).

**Expected friction points:**

- **"Connection timed out"** → Pi hasn't finished booting. Wait 30 more seconds and retry. If still failing, check the power LED is solid (not blinking), and confirm the IP is correct.
- **"Connection refused"** → SSH daemon not running. Re-image the SD card. Workaround if needed today: mount SD card boot partition on a laptop, create an empty file named `ssh` in the root of that partition.
- **"WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED"** → Same IP assigned to a different Pi than last time. Fix: `ssh-keygen -R <IP>` on the student's laptop, then retry.
- **Students typing `raspberry` and nothing appearing** → Password field doesn't echo. Normal — just type and press Enter.

Once the first partner is in: **second partner opens their own terminal and SSHes into the same Pi simultaneously.** Same credentials, same IP.

Then both partners run:
```bash
who     # lists all logged-in users with terminal and login time
w       # same, plus what each session is currently running
```

They see each other's sessions: `pi pts/0` and `pi pts/1`. Ask: "What does this remind you of from Unit 2?" → Linux is a multi-user OS. This was abstract in Unit 2 — now there are two real humans on one physical machine on the desk.

Have one partner run the blink script (`python3 ~/gpio/blink.py` — if the file doesn't exist yet, do file transfer first). Have the other run:
```bash
ps aux | grep python3
```
They see the running script listed as a process. Both sessions, one shared system.

Have them create `~/gpio/` on the Pi and `cd` into it before moving on.

---

### File Transfer: Get the Script onto the Pi (15 min)

Students need to get their `blink.py` (or `day3.py`) from their laptop to the Pi. Three options — offer all three and let pairs choose:

#### Option A — `scp` (recommended if the file exists on the laptop)

From the laptop (not the Pi), open a second terminal window:
```bash
scp ~/gpio/blink.py pi@<IP>:~/gpio/blink.py
```

Students who understand networking can explain to their pair what this does. Confirm the file appeared on the Pi with `ls ~/gpio/`.

#### Option B — `nano` (type it directly)

From the Pi:
```bash
nano ~/gpio/blink.py
```

Type the script from memory or from the student note. Save with Ctrl+X → Y → Enter.

Good for: pairs who didn't finish the Day 3 script and need to write it properly. The act of typing it again reinforces structure.

#### Option C — paste via SSH

Copy the script from the note or their Day 3 file, paste it into `nano` on the Pi. Can be messy with indentation — only suggest this if the student is confident with nano.

> **If no script exists from Day 3:** Pair them on Option B and have them build the blink script from the Day 3 note (§6). This is fine — the typing is the learning.

---

### Swap Import + Run (5 min)

In `nano ~/gpio/blink.py`, find:
```python
import gpio_sim as GPIO
```

Change it to:
```python
import RPi.GPIO as GPIO
```

Save. Run:
```bash
python3 blink.py
```

Expected output:
```
[real RPi.GPIO — no output lines]
```

`RPi.GPIO` doesn't print simulator lines — it controls actual hardware. The script runs silently. Ctrl+C to stop.

Ask: "How do you know it's doing anything?" → You don't yet. Day 5 adds the LED so you can see it. If students are curious, they can check the GPIO state with `gpio readall` (if wiringpi is installed) — but don't go down this rabbit hole today.

Confirm `cleanup` ran: students should see their `"Done."` print after Ctrl+C.

**ICS/advanced students who want to verify something is happening:** Show them `pinout` or `gpio readall` to see pin states. Or tell them the BCM pin 18 voltage can be measured with a multimeter — preview of tomorrow.

---

### Service Audit — Unit 2 Callback (12 min)

This is a direct callback to Unit 2 (systemctl, processes, services) and has genuine practical value — the Pi runs leaner for the CPT. Do this as a class together, not independently, so you control what gets disabled.

**Run as a class:**
```bash
systemctl list-units --type=service --state=running
ps aux | wc -l     # total process count
free -h            # RAM: how much is the OS using on a headless machine?
```

Ask students to identify services they recognise from Unit 2. Then present three safe targets for a headless GPIO Pi:

| Service | What it does | Safe to disable? |
|---------|-------------|-----------------|
| `bluetooth.service` | Bluetooth stack | Yes — no BT needed for GPIO labs |
| `hciuart.service` | Bluetooth UART serial | Yes — same reason |
| `triggerhappy.service` | Keyboard hotkey daemon | Yes — headless, no keyboard ever attached |

```bash
sudo systemctl disable --now bluetooth hciuart triggerhappy
```

Rerun:
```bash
systemctl list-units --type=service --state=running
free -h
```

Students see the service count drop and a small but real RAM savings. Brief but concrete.

**Frame it carefully:** "You know `systemctl disable` from Unit 2. On a headless machine, disabling the wrong service — like `ssh` — locks you out permanently until re-image. There's no monitor to fix it. This is why we're doing this together and only disabling services we understand. On the CPT robot, you'll be able to make these calls yourself."

---

### Preview Day 5 + Shutdown (4 min)

> "Tomorrow you wire an LED to the Pi. BCM pin 18 → 330 ohm resistor → LED → ground. The script you ran today doesn't change — the only new thing is the physical component. For the first time, code you wrote produces something you can see and touch."

**Shutdown — do this every class:**
```bash
sudo shutdown -h now
```

Wait for the green activity LED on the Pi to stop blinking before pulling power. Pulling power mid-write corrupts the SD card. Make this a habit — it will save a re-image at some point.

Store Pis on the shelf. SD cards stay inserted.

---

### Watch For — Day 4

- **Pair dynamics:** One student SSHes in while the other watches. Enforce the "both partners in" step — it's not optional. The student who only watches will struggle on the CPT.
- **Second SSH connection fails:** If the first partner's SSH is still open but idle, the second partner may get "too many connections" if something is misconfigured. Just confirm both can run `who` and see two entries — that's the check.
- **`sudo` on `systemctl disable`:** Students may try without `sudo` and get a permissions error. Expected — explain that disabling services requires root. This is a Unit 2 touchpoint.
- **Students disabling services not on the approved list:** Stop them before they run the command. "Tell me what that service does before you disable it." If they don't know, they don't disable it.
- **Students who didn't finish Day 3:** Don't skip to the import swap. Use Option B to rebuild the script properly. They need to understand the structure before they wire anything.
- **`scp` from wrong directory:** Students who can't find their file — `ls ~/gpio/` on the laptop first. If the file is in a different folder, use the correct source path.
- **Nano indentation wrecked by paste:** `python3 -c "import ast; ast.parse(open('blink.py').read())"` checks for syntax errors fast. `IndentationError` means paste broke the structure — use Option B instead.
- **"Done." not printing after Ctrl+C:** `GPIO.cleanup()` or `print("Done.")` is inside the `while True` instead of in `finally`. Open with nano, check indentation.
- **Students not waiting for shutdown before pulling power:** The green activity LED stops blinking when shutdown is complete. Point at it explicitly the first time. One corrupted SD card in class costs 15 minutes and a re-image.

---

## Before Day 5 — Setup Checklist

- [ ] LED lab kits sorted into bags/trays, one per pair: breadboard, GPIO-to-breadboard ribbon cable + cobbler (or M-F jumpers), 2× LED (red or green), 2× 330Ω resistor
- [ ] Print or post the BCM pinout reference — `pinout.xyz` is excellent, or use the RPi GPIO pinout poster if you have one
- [ ] Confirm your own demo circuit works at home first: BCM 18 → 330Ω → LED → GND, `python3` blink script
- [ ] `lab-01-led.md` posted and accessible

---

## Day 5 — GPIO Lab 1: LED Digital Output

**Goal:** Students wire a real LED circuit and run their blink script. The LED physically blinks. This is the first moment code produces visible physical behaviour.

**Hardware per pair:** RPi (mains-powered), breadboard, 1–2 LEDs, 330Ω resistor, 3× M-F jumpers

### Timing

| Time | Activity |
|------|----------|
| 0–5 | Hook — the moment and why it matters |
| 5–20 | BCM pin numbering — demo and orientation |
| 20–35 | Demo: wire the LED circuit (teacher on projector) |
| 35–58 | Pairs wire their circuit + run blink script |
| 58–68 | Extension: second LED, alternating blink |
| 68–70 | Debrief + lab completion check + shutdown |

---

### Hook (5 min)

> "Everything you've done so far has been on-screen. Today the Pi talks to the physical world. When you run your blink script, the LED blinks. If your wiring is wrong, it doesn't. There's no error message — the circuit either works or it doesn't."

Leave it there. Don't over-explain. The moment of first blink lands harder if they don't know when to expect it.

---

### BCM Pin Numbering (15 min)

This is the conceptual anchor for the entire GPIO unit. Spend the time.

**The two numbering systems:**

Hold up a Pi (or show on projector). Point to the 40-pin header.

> "There are two ways to refer to a pin — by its physical position on the header (1 through 40, left-to-right top-to-bottom), or by its BCM number — the number the Broadcom chip uses internally. The BCM numbers are not sequential and do not match the physical positions. We always use BCM."

Draw or display the header layout. Mark the physical positions. Show that BCM 18 is physical pin 12.

Show the pinout reference (`pinout.xyz` or the printed poster). Point out:
- Not all pins are GPIO — some are 3.3V, 5V, GND, UART, I2C, SPI
- GND pins: physical 6, 9, 14, 20, 25, 30, 34, 39
- 3.3V pins: physical 1 and 17 — these are always-on power, not GPIO
- The GPIO pins: scattered throughout, with their BCM numbers

Ask: "If I write `GPIO.setup(18, GPIO.OUT)`, which physical pin is that?" → Physical pin 12. Have them find it on the pinout reference.

Ask: "What happens if I accidentally use physical pin numbering — `GPIO.setup(12, GPIO.OUT)` — in BCM mode?" → BCM 12 is a different pin (physical pin 32). Nothing obvious goes wrong — a different pin goes HIGH, your LED doesn't blink, and the error is silent.

> **This is why we always confirm with the pinout reference before wiring. The software won't tell you you're on the wrong pin.**

Ask: "What does `GPIO.setmode(GPIO.BCM)` do?" → Tells the library to interpret all pin numbers as BCM numbers. Without this line, pin 18 means something else. This is why the line is always first.

**Quick check:** Give students 2 minutes to find on their pinout: BCM 18, BCM 23, BCM 25, and two GND pins. These are the pins they'll use in labs 1–3.

---

### Demo: Wire the LED Circuit (10 min)

Wire on the projector with a real breadboard and Pi. Narrate as you go.

**Circuit:**

```
BCM 18 (physical pin 12)  →  [330Ω resistor]  →  LED anode (+, longer leg)
LED cathode (−, shorter leg)  →  GND (physical pin 6)
```

**How to do it:**

1. Pi is OFF or script stopped — always wire with GPIO pins at LOW (run `GPIO.cleanup()` or just stop the script)
2. M-F jumper from physical pin 12 (BCM 18) to a row on the breadboard
3. Place 330Ω resistor: one leg in the same row, other leg in a new row
4. Place LED: anode (longer leg) in the same row as the resistor's second leg, cathode in a new row
5. M-F jumper from cathode row to GND (physical pin 6)

Ask after wiring: "What does the resistor do?" → Limits current. 3.3V GPIO pin − 2.0V LED forward voltage = 1.3V across the resistor. 1.3V ÷ 330Ω ≈ 4mA. GPIO pins are rated max 16mA — 4mA is safe. Without the resistor, the LED draws too much current and may damage the GPIO pin.

Ask: "What happens if we wire the LED backwards?" → Current can't flow through a diode in reverse. LED doesn't light. Not damaging — just silent. We'll test this.

Run the blink script:
```bash
python3 ~/gpio/blink.py
```

LED blinks. Let it run for 10 seconds. Say: "This is exactly what you wrote on Day 3. Nothing changed in the code except the import."

Stop the script (Ctrl+C). Ask: "Is the LED on or off after cleanup?" → Off. `GPIO.cleanup()` resets all pins to input mode (safe default). This is the whole point of `try / finally`.

Now wire the LED backwards. Run the script. Nothing happens — LED doesn't light. Confirm there's no error — the code runs fine, the circuit is wrong. Put it back correctly.

---

### Pairs Wire Their Circuit + Run (20 min)

Distribute lab kits. Students wire and run.

**Before they touch a jumper:**

> "Look at the pinout reference. Find BCM 18 on your Pi. Find a GND pin. Tell your partner the physical pin numbers before you wire anything."

Circulate. Key checks:

1. Are they using BCM pin 18 or some other pin? (Check their pinout reference)
2. Is the resistor present? Where is it in the circuit?
3. LED polarity — longer leg to resistor, shorter leg to GND?
4. Are they running the script with `RPi.GPIO` (not `gpio_sim`)? Check with `head -2 ~/gpio/blink.py`

**Common failures:**

| Symptom | Likely Cause |
|---------|-------------|
| Script runs, LED does nothing | Wrong pin, or LED backwards — check pinout, swap LED legs |
| Script crashes with `RuntimeError: No access to /dev/gpiomem` | Not running as `pi` user, or missing `RPi.GPIO` install. Confirm: `whoami` → `pi` |
| LED always on, doesn't blink | LED wired to 3.3V pin (always-on power) instead of GPIO 18 |
| Script gives `ImportError: No module named 'RPi'` | Forgot to swap the import from `gpio_sim`. Open with nano, fix. |
| LED lights but very dim | Resistor value too high, or GPIO current limit hit. 330Ω should be fine — check for double-resistor accident. |

**First blink moment:** When a pair gets their LED blinking for the first time — acknowledge it. This is the payoff for three days of terminal work.

---

### Extension: Second LED, Alternating Blink (8 min)

For pairs who finish early:

> "Wire a second LED on BCM 23 (physical pin 16). Modify your script to alternate — one on while the other is off. Your Day 3 Part B script already does this with `gpio_sim`. The only change is the import."

This is Day 3 Part B deployed on real hardware. Students who wrote it on Day 3 just copy it over and run. Students who didn't write it get a practical reason to.

**Further extension (FTC/advanced):** Wire both LEDs, add a function `blink_n(pin, n, delay)` that blinks a single pin n times. Call it in `setup()` as a startup sequence. This is the robot code structure from Day 3 Part D — but now it makes the real LEDs blink.

---

### Debrief + Lab Completion Check (2 min)

Walk the room before the bell. For each pair, confirm:
1. LED blinks in sync with the script (or two LEDs alternating for extension)
2. Ctrl+C results in LED off (cleanup worked)

That's the lab completion mark. Working circuit + functioning script = credit.

---

### Watch For — Day 5

- **Students who don't consult the pinout reference:** They guess the pin. The guess is usually wrong. Stop them before they wire: "Show me BCM 18 on the pinout. What physical pin is it?" Make this a habit from day one — circuits don't give error messages.
- **LED in backwards:** The most common wiring mistake. If the LED does nothing and the script runs cleanly, swap the LED direction first — 9 times out of 10 that's it.
- **LED wired to 3.3V instead of GPIO 18:** LED stays on permanently, doesn't blink. The 3.3V pin (physical 1 or 17) looks close to GPIO 18 (physical 12) on the header. Emphasise counting pins — there are two rows, count from the end closest to the board edge.
- **No resistor:** LED may light but be very bright, and repeated use risks damaging the GPIO pin. Stop the script immediately. Add the resistor.
- **Pairs where one student wires while the other watches:** Require the second student to locate at least the GND connection and confirm LED polarity. Both students need to be able to wire this independently for the CPT.
- **`gpio_sim` import not swapped:** The most common software error. `gpio_sim.py` probably isn't on the Pi at all, so the error is `ModuleNotFoundError`, not a GPIO error. Good diagnostic: if the error says `gpio_sim`, the import wasn't changed.
- **Pis running very hot on mains:** Pi 4/5 can get warm under sustained load. Not dangerous without a case, but worth noting. Pi 5 benefits from a heatsink for sustained use.

---

## Connector: Day 5 → Day 6

Day 6: GPIO Lab 2 — Button (digital input). Same Pi, same wiring setup. Add:
- Tactile button + 10kΩ pull-down resistor
- New pin: BCM 25 (physical pin 22) as input
- Polling loop: `GPIO.input(BUTTON_PIN)` → True/False
- Connect to the LED: button press changes LED state

The conceptual jump: digital input vs output. Everything else (BCM numbering, import, try/finally) is established.
