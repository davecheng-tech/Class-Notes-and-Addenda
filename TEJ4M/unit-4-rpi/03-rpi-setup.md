# Raspberry Pi Setup

This note covers Day 4: connecting to your Pi over SSH, authenticating to the school network, and getting your script running on real hardware for the first time.

**What you need:**
- Your Pi's IP address (posted in Google Classroom)
- Your `blink.py` script from Day 3
- Your Chromebook terminal (or any SSH client)

<br>

## 1. SSH In

SSH lets you run a terminal on the Pi from your laptop over the network. No monitor required.

Open a terminal on your Chromebook and connect:

```
ssh pi@<your-pi-ip>
```

The first time you connect, you'll see a fingerprint warning — type `yes` and press Enter. When prompted for a password, type `raspberry` (nothing will appear as you type — that's normal).

You should see the Pi's welcome banner and a prompt like `pi@rpi-01:~ $`. Every command you type from here runs on the Pi, not your laptop.

> [!NOTE]
> Both partners should SSH into the Pi simultaneously — same IP, same credentials. Run `who` to confirm you can see each other's sessions. This is the same multi-user Linux behaviour from Unit 2, now visible on a physical machine on your desk.

**Basic orientation:**

```
pwd          # current directory → /home/pi
ls           # contents of home directory
uname -a     # confirms you're on the Pi (ARM processor, not x86)
```

Create a working directory for your GPIO scripts:

```
mkdir gpio
cd gpio
```

All your lab scripts live here for the rest of the unit.

<br>

## 2. Authenticate to YCBYOD

YCBYOD uses a **captive portal** — a login page that blocks internet traffic until you authenticate. On a Pi with no graphical browser, you authenticate using **lynx**, a text-based web browser.

### 2.1 Install lynx

lynx is not installed by default. Get it from the class file server (IP given in class):

```
mkdir -p ~/lynx-pkg && cd ~/lynx-pkg
curl -O http://<server-ip>:8080/lynx-common_2.9.2-1_all.deb
curl -O http://<server-ip>:8080/mailcap_3.74_all.deb
curl -O http://<server-ip>:8080/lynx_2.9.2-1+b1_arm64.deb
sudo dpkg -i lynx-common_2.9.2-1_all.deb mailcap_3.74_all.deb lynx_2.9.2-1+b1_arm64.deb
```

Verify the install:

```
lynx --version
```

### 2.2 Authenticate

```
lynx http://connectme.ycdsb.ca
```

lynx opens in the terminal. Use arrow keys to navigate, Enter to follow links, and fill in your credentials when prompted. Press `Q` then `Y` to quit when done.

Once authenticated, the Pi has outbound internet access for the rest of the session. You only need to do this once per boot.

> [!TIP]
> If the captive portal page doesn't load, try any plain HTTP address — the portal will intercept and redirect. `http://example.com` works. HTTPS addresses won't trigger the redirect.

<br>

## 3. Get Your Script onto the Pi

You need to transfer `blink.py` from your laptop to the Pi. Three options:

### Option A — `scp` (if the file exists on your laptop)

Open a **second terminal window on your laptop** (not the SSH session) and run:

```
scp ~/gpio/blink.py pi@<your-pi-ip>:~/gpio/blink.py
```

Confirm it arrived on the Pi:

```
ls ~/gpio/
```

### Option B — type it with `nano`

From the Pi:

```
nano ~/gpio/blink.py
```

Type the script from your Day 3 notes. Save with **Ctrl+X → Y → Enter**.

This option is useful if your Day 3 script isn't complete — retyping it is good practice before you wire anything.

### Option C — paste into nano

Copy the script from your Day 3 file or the course note, open `nano ~/gpio/blink.py`, and paste. Watch for indentation errors — paste can break Python's whitespace structure.

Check for syntax errors quickly:

```
python3 -c "import ast; ast.parse(open('blink.py').read())"
```

No output means the file is syntactically valid. An `IndentationError` means paste corrupted the structure — use Option B instead.

<br>

## 4. Swap the Import and Run

On the Pi, `gpio_sim` is not available — use the real GPIO library. Open the script:

```
nano ~/gpio/blink.py
```

Find:
```python
import gpio_sim as GPIO
```

Change it to:
```python
import RPi.GPIO as GPIO
```

Save and run:

```
python3 blink.py
```

`RPi.GPIO` controls actual hardware silently — no simulator output lines. The script runs without printing anything. Press **Ctrl+C** to stop; you should see `Done.` printed by your `finally` block.

> [!NOTE]
> If the script crashes with `RuntimeError: No access to /dev/gpiomem`, confirm you're running as the `pi` user: `whoami`. If it crashes with `ModuleNotFoundError: No module named 'gpio_sim'`, the import wasn't changed — open with nano and fix it.

No LED is wired yet — there's nothing to see. Day 5 adds the physical circuit. The script is correct if it runs silently and prints `Done.` when you stop it.

<br>

## 5. Shutdown

**Always shut down cleanly before unplugging power.** Pulling power mid-write corrupts the SD card.

```
sudo shutdown -h now
```

Wait for the green activity LED on the Pi to stop blinking, then unplug. This becomes a habit — one corrupted card costs 15 minutes and a re-image.

SD cards stay inserted in the Pis. Store your Pi on the shelf.

<br>

## Key Terms

| Term | Definition |
|------|-----------|
| **SSH** | Secure Shell — a protocol for running a terminal on a remote machine over a network |
| **headless** | Running without a monitor, keyboard, or mouse — terminal access only |
| **captive portal** | A web page that intercepts network traffic until you authenticate — used by YCBYOD |
| **lynx** | A text-based web browser — used to authenticate to YCBYOD from the terminal |
| **`scp`** | Secure Copy — transfers files between machines over SSH |
| **`dpkg -i`** | Installs a `.deb` package file directly, without using `apt` |
| **`GPIO.cleanup()`** | Resets all GPIO pins — runs in `finally` when the script ends |
