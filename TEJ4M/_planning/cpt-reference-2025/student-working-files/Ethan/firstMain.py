import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

lightInputPin = 22
lightOutputPin = 16


def lightSensorTimer(lightInputPin):
    count = 0
    GPIO.setup(lightInputPin, GPIO.OUT)
    GPIO.output(lightInputPin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(lightInputPin, GPIO.IN)

    while GPIO.input(lightInputPin) == GPIO.LOW:
        count += 1
    return count


def getLightSensor(lightInputPin):
    lightValue = round(lightSensorTimer(lightInputPin) / 100, 0)
    return lightValue


def controlLight(lightOutputPin, IOValue):
    GPIO.setup(lightOutputPin, GPIO.OUT)
    if IOValue == "1":
        GPIO.output(lightOutputPin, GPIO.HIGH)
        print("Light turned on")
        time.sleep(0.5)
    elif IOValue == "0":
        GPIO.output(lightOutputPin, GPIO.LOW)
        print("Light turned off")
        time.sleep(0.5)
    return 0


# Main Loop
try:
    while True:
        if getLightSensor(lightInputPin) > 3:
            controlLight(lightOutputPin, "1")
        else:
            controlLight(lightOutputPin, "0")
except KeyboardInterrupt:
    print("Terminating Program")
finally:
    GPIO.cleanup()
