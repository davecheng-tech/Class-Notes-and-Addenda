# Addendum: Separate Motor Power Supply (4-Motor Builds)

If your robot uses **two L293D chips and four TT motors**, you need a dedicated power supply for the motors. This addendum explains why, what to buy, and how to wire it.

---

## The Problem

The L293D has two separate power pins:

- **Vss (pin 16)** — logic power, runs the chip's control circuitry
- **Vm (pin 8)** — motor power, runs the output transistors and through them the motors

In Lab 03, both Vm and Vss connect to the cobbler's 5V rail. That works fine for one L293D and two motors on a bench. Add a second chip and two more motors, and the current budget runs out.

The USB power bank powering the Pi delivers around 2.1–2.4A from its output port. The Pi alone consumes ~700mA. Four TT motors driving hard draw another ~800mA — and at stall (when the robot is pushing against another robot) up to ~2.4A more. You can't fit all of that through one USB port without the voltage sagging and the Pi browning out.

The fix: give the motors their own battery. The Pi runs on the power bank; the motors run on an AA pack. They share a ground, and that's it.

---

## The Battery Box

A **battery holder with a power switch** wires directly into your breadboard. No soldering required if the leads are bare wire — just push them into a breadboard row.

**Available at [Sayal Electronics, Markham](https://secure.sayal.com/STORE4/storelocations.php)**
7701 Woodbine Ave., Unit 1-3, Markham — Mon–Fri 8:00–5:30, Sat 10:00–4:00

| Format | SKU | Voltage (alkaline) | Voltage (NiMH) |
|---|---|---|---|
| 4×AA holder with switch | 269667 | 6V | 4.8V |
| 6×AA holder with switch | 261058 | 9V | 7.2V |

> [!NOTE]
> Sayal also carries TT motors, wheels, and HC-SR04 ultrasonic sensors if your group needs spares or extensions.

**Which battery configuration is right for your group?**

The L293D drops approximately 1.8V between Vm and the motor output — so what you supply is not what the motor sees:

| Configuration | Vm voltage | Motors see | Compared to 5V rail |
|---|---|---|---|
| 4×AA NiMH (1.2V × 4) | 4.8V | ~3.0V | ≈ same — closest match to current behaviour |
| 4×AA alkaline (1.5V × 4) | 6V | ~4.2V | noticeably more torque |
| 6×AA NiMH (1.2V × 6) | 7.2V | ~5.4V | significantly more torque |
| 6×AA alkaline (1.5V × 6) | 9V | ~7.2V | strong — may be faster than expected |

**Recommendation:** Start with **4×AA alkaline**. The motors are currently underpowered running off the 5V rail through the L293D — more torque is a good thing in a sumo match, and the behaviour difference won't surprise you badly. 6×AA is fine if that's what you have, but test before the competition so you know how your robot handles.

> [!NOTE]
> **Vss (pin 16) must not exceed 7V** — that is the logic supply, and it stays connected to the cobbler 5V rail. Vm (pin 8) is the motor supply and is a separate pin rated to 36V — the battery voltage goes there, not to Vss.

---

## ⚠️ Critical Wiring Warning — Read Before Touching the Breadboard

> [!WARNING]
> **Do not connect the battery supply rail to the cobbler 5V rail. This will destroy the Raspberry Pi.**
>
> The Raspberry Pi 4 costs over $80 to replace. The school has a limited number of them.
>
> Here is what happens if you bridge the two rails: the battery voltage (6V or 9V) backfeeds through the cobbler directly into the Pi's 5V power bus. There is no fuse or protection on that path. The Pi will be damaged immediately and silently — it will simply stop working.
>
> **The battery (+) rail and the cobbler 5V rail must never be connected to each other.** They share a GND rail. That is the only connection between them.

Use a physically separate breadboard power rail for the battery supply, and double-check before applying power.

---

## Wiring

**Remove:** the jumper from cobbler 5V to L293D pin 8 (Vm) on each chip.

**Add:**

| From | To | Notes |
|---|---|---|
| Battery box red (+) | Breadboard power rail — **separate from cobbler 5V** | Motor supply |
| Battery box black (–) | Breadboard GND rail | Same GND rail as the cobbler — required |
| Battery rail (+) | L293D chip 1, pin 8 (Vm) | Motor power, chip 1 |
| Battery rail (+) | L293D chip 2, pin 8 (Vm) | Motor power, chip 2 |

**Leave unchanged:**

| Connection | Stays on |
|---|---|
| L293D pin 16 (Vss) — both chips | Cobbler 5V rail |
| L293D pins 1, 9 (EN1, EN2) — both chips | Cobbler 5V rail (or GPIO if using PWM) |
| All GPIO signal wires (IN1–IN4) | As wired in Lab 03 |

> [!IMPORTANT]
> **The GND rail must be shared.** The battery box black wire and the cobbler GND both connect to the same breadboard ground rail. Without a shared ground, the L293D cannot read the GPIO control signals correctly and the motors will not respond.

---

## What Changes in Code

Nothing. The L293D still receives the same GPIO signals on IN1–IN4 and EN1–EN2. The motor supply voltage affects speed and torque, not how the chip is controlled. Your existing motor code from Lab 03 works without modification.

---

## Before Powering On — Checklist

- [ ] Battery box switch is **off** before wiring
- [ ] Battery red wire connects to a power rail that is **not** connected to cobbler 5V
- [ ] Battery black wire connects to the **same GND rail** as the cobbler
- [ ] Both Vm pins (L293D pin 8, both chips) connect to the battery rail, **not cobbler 5V**
- [ ] Both Vss pins (L293D pin 16, both chips) still connect to cobbler 5V
- [ ] All EN and IN pins unchanged from Lab 03 wiring
- [ ] **No bridge between the battery rail and the cobbler 5V rail** — ask your teacher to check before powering on if you are unsure
