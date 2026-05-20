import RPi.GPIO as GPIO
import time
import threading

# Define pins for motors, button, LED, and light sensor
motor_pins = [6, 13, 23, 24]  # motor GPIO pins
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
running_light_sensor = False
light_sensor_thread = None

def light_sensor_loop():
    while running_light_sensor:
        print("Light sensor reading:", rc_time(light_sensor_pin))
        time.sleep(1)

# Function to start all systems
def start_all():
    global running_light_sensor, light_sensor_thread
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(led_pin, GPIO.HIGH)
    running_light_sensor = True
    light_sensor_thread = threading.Thread(target=light_sensor_loop)
    light_sensor_thread.start()

# Function to stop all systems
def stop_all():
    global running_light_sensor
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(led_pin, GPIO.LOW)
    running_light_sensor = False
    if light_sensor_thread:
        light_sensor_thread.join()

motor_running = False

try:
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            motor_running = not motor_running
            if motor_running:
                start_all()
            else:
                stop_all()
            while GPIO.input(button_pin) == GPIO.LOW:
                time.sleep(0.1)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    stop_all()
    GPIO.cleanup()
