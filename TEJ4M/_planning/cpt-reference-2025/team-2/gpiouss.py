import RPi.GPIO as GPIO
import time

TRIG_PIN = 12  # GPIO 12
ECHO_PIN = 16  # GPIO 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.05)

    # Trigger pulse
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Timeout start
    timeout = time.time() + 0.04  # 40ms timeout for start
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
        if time.time() > timeout:
            return None  # Timeout occurred

    timeout = time.time() + 0.04  # 40ms timeout for end
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
        if time.time() > timeout:
            return None  # Timeout occurred

    pulse_duration = pulse_end - pulse_start
    distance_cm = pulse_duration * 17150
    return round(distance_cm, 2)

try:
    while True:
        cm = measure_distance()
        if cm is None or cm <= 2.0 or cm > 400:
            print("Distance: Out of range or no object detected.")
        else:
            mm = cm * 10
            m = cm / 100
            print(f"Distance: {mm:.1f} mm | {cm:.2f} cm | {m:.3f} m")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMeasurement stopped by user.")
    GPIO.cleanup()
