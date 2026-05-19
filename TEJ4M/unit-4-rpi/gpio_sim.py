"""
gpio_sim.py — Raspberry Pi GPIO simulator for use on laptops (no Pi required).

Drop this file in the same folder as your GPIO script.
Change:   import RPi.GPIO as GPIO
To:       import gpio_sim as GPIO

All other code stays the same. On a real Pi, switch back to RPi.GPIO.

To simulate a button press, set SIMULATED_INPUT = True at the bottom of this file.
"""

# --- Constants (match RPi.GPIO values) ---
BCM   = 11
BOARD = 10
OUT   = 0
IN    = 1
HIGH  = True
LOW   = False
PUD_UP   = 22
PUD_DOWN = 21

# --- Simulated state ---
_pin_modes  = {}   # pin -> OUT or IN
_pin_states = {}   # pin -> True/False

# Edit this to simulate button presses or sensor readings.
# True = HIGH (button pressed / sensor triggered)
# False = LOW (button released / sensor quiet)
SIMULATED_INPUT = False


# --- GPIO functions ---

def setmode(mode):
    name = "BCM" if mode == BCM else "BOARD"
    print(f"[GPIO] setmode: {name}")


def setup(pin, mode, pull_up_down=None):
    _pin_modes[pin] = mode
    if mode == OUT:
        _pin_states[pin] = False
        print(f"[GPIO] setup: pin {pin} → OUT")
    else:
        print(f"[GPIO] setup: pin {pin} → IN")


def output(pin, value):
    if _pin_modes.get(pin) != OUT:
        print(f"[GPIO] WARNING: pin {pin} is not set up as OUT")
    _pin_states[pin] = bool(value)
    level = "HIGH" if value else "LOW"
    print(f"[GPIO] output: pin {pin} → {level}")


def input(pin):
    if _pin_modes.get(pin) != IN:
        print(f"[GPIO] WARNING: pin {pin} is not set up as IN")
    return bool(SIMULATED_INPUT)


def cleanup():
    for pin in list(_pin_states):
        _pin_states[pin] = False
    _pin_modes.clear()
    print("[GPIO] cleanup")


# --- PWM stub ---

class PWM:
    def __init__(self, pin, frequency):
        self._pin = pin
        self._freq = frequency
        print(f"[GPIO] PWM: pin {pin} at {frequency} Hz")

    def start(self, duty_cycle):
        print(f"[GPIO] PWM pin {self._pin}: start, duty cycle {duty_cycle}%")

    def ChangeDutyCycle(self, duty_cycle):
        print(f"[GPIO] PWM pin {self._pin}: duty cycle → {duty_cycle}%")

    def ChangeFrequency(self, frequency):
        self._freq = frequency
        print(f"[GPIO] PWM pin {self._pin}: frequency → {frequency} Hz")

    def stop(self):
        print(f"[GPIO] PWM pin {self._pin}: stop")
