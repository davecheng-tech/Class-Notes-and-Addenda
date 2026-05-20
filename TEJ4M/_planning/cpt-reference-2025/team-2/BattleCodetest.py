import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Motor control pins
MOTOR_LEFT_FORWARD = 23
MOTOR_LEFT_BACKWARD = 24
MOTOR_RIGHT_FORWARD = 27
MOTOR_RIGHT_BACKWARD = 17

# Button input pin
BUTTON_PIN = 26

# Ultrasonic sensor pins
GPIO_TRIGGER = 21
GPIO_ECHO = 20

# Light sensor pins
SENSOR_FR = 12
SENSOR_FL = 18
SENSOR_BR = 6
SENSOR_BL = 22

# Initialize motor pins
GPIO.setup(MOTOR_LEFT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD, GPIO.OUT)

# Button and ultrasonic setup
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# State flags
startup = False
buffer = False

# Measure distance with ultrasonic sensor
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance_cm = (TimeElapsed * 34300) / 2
    return distance_cm

# Read light level from sensor
def rc_time(pin_to_circuit):
    count = 0
    MAX_COUNT = 1000000

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)

    while GPIO.input(pin_to_circuit) == GPIO.LOW and count < MAX_COUNT:
        count += 1

    return count

# Stop all motors
def stop_motors():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)

# Movement functions
def move_forward():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)

def move_backward():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.HIGH)

def turn_left():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)

def turn_right():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.HIGH)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == 1 and not startup and not buffer:
            startup = True
            print("Startup activated")

        while startup:
            val_FR = rc_time(SENSOR_FR)
            val_FL = rc_time(SENSOR_FL)
            val_BR = rc_time(SENSOR_BR)
            val_BL = rc_time(SENSOR_BL)

            print(f"FR: {val_FR}, FL: {val_FL}, BR: {val_BR}, BL: {val_BL}")

            if val_BR > 100000 and val_FR > 100000 and val_FL > 100000 and val_BL > 45000:
                if distance() < 200:
                    move_forward()
                else:
                    turn_right()

            elif val_FL < 100000:
                print("White detected: Front Left")
                move_backward()
                time.sleep(0.3)
                turn_right()
                time.sleep(0.4)
                stop_motors()

            elif val_FR < 100000:
                print("White detected: Front Right")
                move_backward()
                time.sleep(0.3)
                turn_left()
                time.sleep(0.4)
                stop_motors()

            elif val_BL < 45000:
                print("White detected: Back Left")
                move_forward()
                time.sleep(0.3)
                turn_right()
                time.sleep(0.4)
                stop_motors()

            elif val_BR < 100000:
                print("White detected: Back Right")
                move_forward()
                time.sleep(0.3)
                turn_left()
                time.sleep(0.4)
                stop_motors()

            if GPIO.input(BUTTON_PIN) == 1 and startup:
                stop_motors()
                startup = False
                buffer = True
                print("Stopped")

except KeyboardInterrupt:
    print("Interrupted, exiting...")

finally:
    stop_motors()
    GPIO.cleanup()
