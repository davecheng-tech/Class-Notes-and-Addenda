import RPi.GPIO as GPIO
import time

# Define pins for motors and button
motor_pins = [6, 13, 23, 24]  # motor GPIO pins
button_pin = 26               # button GPIO pin

# Setup
GPIO.setmode(GPIO.BCM)
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to run motors forward
def start_motors():
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

# Function to stop motors
def stop_motors():
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

motor_running = False

try:
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            motor_running = not motor_running
            if motor_running:
                start_motors()
            else:
                stop_motors()

            # Debounce: wait until button is released
            while GPIO.input(button_pin) == GPIO.LOW:
                time.sleep(0.1)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    stop_motors()
    GPIO.cleanup()

