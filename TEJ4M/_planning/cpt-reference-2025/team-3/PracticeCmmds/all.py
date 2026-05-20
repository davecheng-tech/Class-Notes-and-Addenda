import RPi.GPIO as GPIO
import time
import threading

# Define pins for motors, button, LED, and light sensor
motor_pins = [5, 6, 23, 24]  # motor GPIO pins
button_pin = 26               # button GPIO pin
led_pin = 16                  # LED GPIO pin
light_sensor_pin = 12         # light sensor GPIO pin

# Setup
GPIO.setmode(GPIO.BCM)
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

# Function to read light level using RC timing
def rc_time(pin):
    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == GPIO.LOW:
        count += 1
    return count

# Light sensor thread
motor_running = False
light_sensor_thread = None
suspended_due_to_light = False


def light_sensor_loop():
    global motor_running, suspended_due_to_light
    while True:
        reading = rc_time(light_sensor_pin)
        print("Light sensor reading:", reading)

        if motor_running:
            if reading > 700 and not suspended_due_to_light:
                stop_motors()
                suspended_due_to_light = True
            elif reading <= 700 and suspended_due_to_light:
                start_motors()
                suspended_due
