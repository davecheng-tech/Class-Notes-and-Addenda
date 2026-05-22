# Lab 03: Motors — H-Bridge Control

In Labs 01 and 02 you used GPIO pins to control an LED (output) and read a button (input). Today you add a motor — a fundamentally different kind of output that requires a driver chip between the Pi and the physical world.

**By the end of Day 7** you will have one motor wired through an L293D and running forward and reverse under Python control.

**By the end of Day 8** you will have two motors running coordinated movement sequences — the direct foundation of the CPT robot drive system.

**Hardware (Day 7):** RPi + cobbler + breadboard, 1× L293D (DIP-16), 1× TT gearbox motor, jumper wires

**Hardware (Day 8):** Same + 1× additional TT gearbox motor

---

## 1. Why You Can't Drive a Motor Directly from GPIO

A GPIO output pin on the Raspberry Pi can source or sink at most **16 mA**. A small TT gearbox motor draws **150–400 mA** when running and much more at stall. Connecting a motor directly to a GPIO pin would immediately overdraw the pin — at best the Pi resets, at worst the GPIO circuitry is permanently damaged.

There's a second problem: **back-EMF**. When a spinning motor is switched off, the magnetic field in its coil collapses and generates a reverse voltage spike — sometimes several times the supply voltage, lasting microseconds. Without protection, this spike travels back up the wire and into your GPIO pin.

The solution is a **motor driver chip** that sits between the Pi and the motor:
- It takes low-current logic signals from the GPIO (safe for the Pi)
- It switches a separate, higher-current supply through the motor (safe for the motor)
- It includes built-in protection diodes to absorb back-EMF spikes

---

## 2. The H-Bridge

To run a motor forward and reverse, you need to reverse the direction of current through it. An **H-bridge** does this using four switches arranged in a pattern that looks like the letter H:

```
       +V
        │
   ┌────┤────┐
   │    │    │
  [S1]  │  [S2]
   │    │    │
   ├────┤────┤
   │  MOTOR  │
   ├────┤────┤
   │    │    │
  [S3]  │  [S4]
   │    │    │
   └────┤────┘
        │
       GND
```

- **S1 + S4 closed:** current flows left-to-right through the motor → forward
- **S2 + S3 closed:** current flows right-to-left → reverse
- **S1 + S3, or S2 + S4:** both motor terminals at the same voltage → stop (brake)
- **All open:** motor coasts to a stop

The L293D implements this with transistors, driven by logic signals from your GPIO pins. You never interact with the switches directly — you just write HIGH or LOW to two input pins.

---

## 3. The L293D

The L293D is a **dual H-bridge** chip in a DIP-16 package — it fits directly across the centre channel of your breadboard and can drive two motors independently.

```
               L293D (top view)
            ┌────────────────┐
   EN1 ─── 1│                │16 ─── Vss  (logic power, 5V)
   IN1 ─── 2│                │15 ─── IN4
  OUT1 ─── 3│  Motor 1  │  2 │14 ─── OUT4
   GND ─── 4│                │13 ─── GND
   GND ─── 5│                │12 ─── GND
  OUT2 ─── 6│                │11 ─── OUT3
   IN2 ─── 7│                │10 ─── IN3
    Vm ─── 8│                │ 9 ─── EN2
            └────────────────┘
```

| Pin | Name | Role |
|-----|------|------|
| 1 | EN1 | Enable motor 1 — HIGH to run, LOW to disable |
| 2 | IN1 | Direction input A (from GPIO) |
| 3 | OUT1 | Motor 1 terminal A |
| 4, 5 | GND | Ground |
| 6 | OUT2 | Motor 1 terminal B |
| 7 | IN2 | Direction input B (from GPIO) |
| 8 | Vm | Motor power supply (5V from cobbler) |
| 9 | EN2 | Enable motor 2 |
| 10 | IN3 | Direction input C (from GPIO) |
| 11 | OUT3 | Motor 2 terminal A |
| 12, 13 | GND | Ground |
| 14 | OUT4 | Motor 2 terminal B |
| 15 | IN4 | Direction input D (from GPIO) |
| 16 | Vss | Logic power supply (5V from cobbler) |

**Vm vs Vss:** Both are powered from the cobbler's 5V rail, but they are separate pins with different roles. Vm powers the motors; Vss powers the chip's logic. Wire them separately — one jumper each.

> [!WARNING]
> **Vss (pin 16) must not exceed 7V.** If you use a higher-voltage supply for Vm (e.g. a 9V battery for more torque), Vss must still connect to 5V. Feeding 9V into pin 16 destroys the chip.

**Direction truth table for motor 1:**

| EN1 | IN1 | IN2 | Motor |
|-----|-----|-----|-------|
| HIGH | HIGH | LOW | Forward |
| HIGH | LOW | HIGH | Reverse |
| HIGH | LOW | LOW | Stop (coast) |
| HIGH | HIGH | HIGH | Stop (brake) |
| LOW | × | × | Disabled |

Motor 2 (EN2, IN3, IN4, OUT3, OUT4) works identically.

---

## 4. Wiring — One Motor (Day 7)

Place the L293D spanning the breadboard centre channel. Pin 1 is marked with a notch or dot on one end of the chip.

![L293D one-motor wiring diagram — L293D on breadboard with one TT motor, 5V to Vm and Vss, GPIO 23 and 24 to IN1 and IN2](./images/lab-03-one-motor-circuit.png)

**Connections:**

| From | To | Notes |
|------|----|-------|
| Cobbler 5V | L293D pin 16 (Vss) | Logic power |
| Cobbler 5V | L293D pin 8 (Vm) | Motor power |
| Cobbler GND | L293D pin 4 | |
| Cobbler GND | L293D pin 5 | |
| Cobbler 5V | L293D pin 1 (EN1) | Tied HIGH — motor always enabled |
| GPIO 23 | L293D pin 2 (IN1) | Direction A |
| GPIO 24 | L293D pin 7 (IN2) | Direction B |
| L293D pin 3 (OUT1) | Motor terminal (either) | |
| L293D pin 6 (OUT2) | Motor terminal (other) | |

**Before powering on:**
- Confirm pin 1 orientation (notch or dot)
- Confirm Vss (pin 16) and Vm (pin 8) are both connected to 5V — not to each other, not to GND
- Confirm GND is on pins 4 and 5, not 4 and 16

> [!TIP]
> The motor terminals are not polarised — OUT1 and OUT2 just determine which direction is "forward" and which is "reverse". If the motor spins the wrong way for your robot, swap the two motor wires rather than changing the code.

---

## Part A — One Motor: Forward, Reverse, Stop

Create a new file:

```bash
nano ~/gpio/motors.py
```

```python
import RPi.GPIO as GPIO
import time

IN1 = 23
IN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def reverse():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

try:
    print("Forward 2s")
    forward()
    time.sleep(2)

    print("Stop 0.5s")
    stop()
    time.sleep(0.5)

    print("Reverse 2s")
    reverse()
    time.sleep(2)

    print("Stop")
    stop()

finally:
    GPIO.cleanup()
    print("Done.")
```

Run it:

```bash
python3 ~/gpio/motors.py
```

The motor should spin in one direction, pause, then spin the other way.

**If the motor does nothing:** confirm EN1 (pin 1) is connected to 5V — if it's floating or at GND, the chip is disabled and no signal on IN1/IN2 will do anything.

**If the motor runs but doesn't reverse:** IN1 and IN2 may be swapped, or both connected to the same pin. Check the wiring against the table above.

**If the Pi resets when the motor starts:** the USB power bank can't supply enough current. Try a different power bank, or reduce other loads.

**If the motor runs in only one direction regardless of IN1/IN2:** both IN pins may be wired to the same GPIO pin. Check continuity on the breadboard rows.

---

## 5. Wiring — Two Motors (Day 8)

Add the second motor using the other half of the L293D (pins 9–15). GND pins 12 and 13 should already be in the breadboard if you wired them on Day 7 — if not, add them now.

![L293D two-motor wiring diagram — both motor channels wired, GPIO 23/24 for motor 1, GPIO 27/17 for motor 2](./images/lab-03-two-motor-circuit.png)

**Additional connections:**

| From | To | Notes |
|------|----|-------|
| Cobbler GND | L293D pin 12 | |
| Cobbler GND | L293D pin 13 | |
| Cobbler 5V | L293D pin 9 (EN2) | Tied HIGH |
| GPIO 27 | L293D pin 10 (IN3) | Motor 2 direction A |
| GPIO 17 | L293D pin 15 (IN4) | Motor 2 direction B |
| L293D pin 11 (OUT3) | Motor 2 terminal (either) | |
| L293D pin 14 (OUT4) | Motor 2 terminal (other) | |

**GPIO pins used across both motors:**

| Signal | BCM | Physical |
|--------|-----|----------|
| IN1 (motor left) | 23 | 16 |
| IN2 (motor left) | 24 | 18 |
| IN3 (motor right) | 27 | 13 |
| IN4 (motor right) | 17 | 11 |

> [!NOTE]
> "Left" and "right" depend on which motor you wire to which channel and how they're mounted on the chassis. For now, just label them — you can swap the physical motor wires on the chassis if the directions are wrong.

---

## Part B — Two Motors: Movement Functions

Extend `motors.py` with the second motor's pins and a set of movement functions.

```python
import RPi.GPIO as GPIO
import time

IN1 = 23    # left motor
IN2 = 24
IN3 = 27    # right motor
IN4 = 17

GPIO.setmode(GPIO.BCM)
for pin in [IN1, IN2, IN3, IN4]:
    GPIO.setup(pin, GPIO.OUT)

def motor_left(direction):
    GPIO.output(IN1, direction == "forward")
    GPIO.output(IN2, direction == "reverse")

def motor_right(direction):
    GPIO.output(IN3, direction == "forward")
    GPIO.output(IN4, direction == "reverse")

def drive(direction, duration):
    motor_left(direction)
    motor_right(direction)
    time.sleep(duration)

def turn(direction, duration):
    if direction == "left":
        motor_left("reverse")
        motor_right("forward")
    else:
        motor_left("forward")
        motor_right("reverse")
    time.sleep(duration)

def stop():
    for pin in [IN1, IN2, IN3, IN4]:
        GPIO.output(pin, GPIO.LOW)

try:
    drive("forward", 2)
    stop()
    time.sleep(0.3)

    turn("right", 0.5)
    stop()
    time.sleep(0.3)

    drive("forward", 2)
    stop()

finally:
    GPIO.cleanup()
    print("Done.")
```

Run it. Both motors should drive forward, pause, execute a right turn (one motor forward, the other reverse), then drive forward again.

**Tuning the turn duration:** 0.5 seconds is a starting point. The actual angle turned depends on motor speed, surface friction, and chassis weight. On a desktop with no wheels and no load, the shaft just spins — tune turn duration on the actual chassis.

**If one motor runs and the other doesn't:** confirm EN2 (pin 9) is connected to 5V and that pins 12 and 13 are both grounded.

**If both motors run in the same direction for `drive()` but turn instead of driving straight:** the motors are mounted facing opposite directions on the chassis (standard for differential drive) and the wiring accounts for this by reversing one channel — or it doesn't yet, and you need to swap one motor's terminals.

---

## Extensions

### A — Sequence

Write a movement sequence: forward 1.5s, right turn 0.4s, forward 1.5s, left turn 0.4s, forward 1.5s, stop. No new concepts — just `drive()`, `turn()`, and `stop()` in sequence.

### B — Button start

Add the button from Lab 02 on GPIO 25. The motors should do nothing until the button is pressed, then execute the sequence once. Use the wait-for-release debounce pattern.

This is the CPT start button — one press launches the robot, which then runs autonomously.

### C — Refactor

The `motor_left()` and `motor_right()` functions are nearly identical. Refactor them into a single `motor(in_a, in_b, direction)` function that takes pin numbers as arguments. The calling code should then read:

```python
motor(IN1, IN2, "forward")
motor(IN3, IN4, "reverse")
```

Is this easier or harder to read than the named `motor_left`/`motor_right` approach? There's no single right answer — think about which you'd want to maintain six months later.

---

## Key Terms

| Term | Definition |
|------|-----------|
| **H-bridge** | A circuit of four switches that routes current through a motor in either direction |
| **Back-EMF** | A reverse voltage spike generated when a motor's field collapses — absorbed by the L293D's built-in diodes |
| **Vm** | Motor power supply pin on the L293D — powers the output transistors |
| **Vss** | Logic power supply pin on the L293D — powers the control circuitry; must not exceed 7V |
| **EN (enable)** | L293D enable pin — HIGH activates the channel; LOW disables it regardless of IN pins |
| **Differential drive** | A two-motor drive system where steering is achieved by varying the speed or direction of each motor independently |
