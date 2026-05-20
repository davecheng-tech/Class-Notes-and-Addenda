import RPi.GPIO as GPIO
import time

# Pin setup
intMotorPins = [5, 6, 23, 24]  # Motor control
intButtonPin = 26              # Start button
intLightSensorPin = 12         # Light sensor
intLEDPin = 16                 # LED pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for intPin in intMotorPins:
    GPIO.setup(intPin, GPIO.OUT)
GPIO.setup(intButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(intLEDPin, GPIO.OUT)

# Light sensor reading function
def fnReadLightSensor(intPin):
    intCount = 0
    GPIO.setup(intPin, GPIO.OUT)
    GPIO.output(intPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(intPin, GPIO.IN)
    while GPIO.input(intPin) == GPIO.LOW:
        intCount += 1
    return intCount

# Motor control
def fnMoveForward():
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

def fnMoveBackward():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)

def fnTurnLeft():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.2)

def fnTurnRight():
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.2)

def fnStopMotors():
    for intPin in intMotorPins:
        GPIO.output(intPin, GPIO.LOW)

try:
    print("Waiting for button press...")
    while GPIO.input(intButtonPin) == GPIO.LOW:
        time.sleep(0.1)
    while GPIO.input(intButtonPin) == GPIO.HIGH:
        time.sleep(0.1)

    print("Button pressed! Turning LED on and waiting 5 seconds...")
    GPIO.output(intLEDPin, GPIO.HIGH)
    time.sleep(5)

    print("Starting autonomous match!")
    while True:
        intLightReading = fnReadLightSensor(intLightSensorPin)
        print("Light:", intLightReading)

        if intLightReading < 850:
            print("Edge detected! Backing up...")
            fnMoveBackward()
            time.sleep(2.5)
            fnStopMotors()
            print("Turning left until black is found...")
            fltStartTime = time.time()
            while True:
                fnTurnLeft()
                time.sleep(0.2)
                intLightReading = fnReadLightSensor(intLightSensorPin)
                print("Light:", intLightReading)
                if intLightReading >= 900:
                    print("Black found. Stopping turn.")
                    break
                if time.time() - fltStartTime > 5:
                    print("Still white after 5 seconds, turning right...")
                    while True:
                        fnTurnRight()
                        time.sleep(0.2)
                        intLightReading = fnReadLightSensor(intLightSensorPin)
                        print("Light:", intLightReading)
                        if intLightReading >= 900:
                            print("Black found. Stopping right turn.")
                            break
                    break
        else:
            print("Inside ring. Moving forward.")
            fnMoveForward()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Interrupted!")
finally:
    fnStopMotors()
    GPIO.output(intLEDPin, GPIO.LOW)
    GPIO.cleanup()

