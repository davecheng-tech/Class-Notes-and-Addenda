import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# setup GPIO
lightInputPin = 22
lightOutputPin = 16
buttonInputPin = 19
trig = 18
echo = 17

# Counts based on capacitor discharge time


def lightSensorTimer():
    count = 0
    GPIO.setup(lightInputPin, GPIO.OUT)
    GPIO.output(lightInputPin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(lightInputPin, GPIO.IN)

    while GPIO.input(lightInputPin) == GPIO.LOW:
        count += 1
    return count


# Returns a value based on lightSensorTimer


def getLightSensor():
    lightValue = round(lightSensorTimer() / 100, 0)
    return lightValue


def isBlack():
    if getLightSensor() > 5:
        return True
    else:
        return False


def getButton():
    GPIO.setup(buttonInputPin, GPIO.IN)
    if GPIO.input(buttonInputPin) == GPIO.HIGH:
        return 0
    elif GPIO.input(buttonInputPin) == GPIO.LOW:
        return 1
    else:
        print("An error with the button has occured")


# Light Control Method based on 1 or 0


def toggleLight(IOValue):
    GPIO.setup(lightOutputPin, GPIO.OUT)
    if IOValue == 1:
        GPIO.output(lightOutputPin, GPIO.HIGH)
        print("Light turned on")
    elif IOValue == 0:
        GPIO.output(lightOutputPin, GPIO.LOW)
        print("Light turned off")
    return 0


# uses the distance sensor to return a number in cm


def getDistance():
    # distance sensor has a trigger and an echo pin, trigger sends out a sound, and echo waits for the sound
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    # sends pulse
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)

    pulse_start = 0.0
    pulse_end = 0.0

    # measures how long it takes to recieve pulse
    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # calculates distance based on the speed of sound
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
