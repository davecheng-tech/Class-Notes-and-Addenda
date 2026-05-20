import RPi.GPIO as GPIO
import random
import time
import light
import motor

# setup GPIO, motors, and light
GPIO.setmode(GPIO.BCM)
motor.motorSetup()
light.toggleLight(1)
print("motor setup")


# testing method
def testLights():
    print(light.getLightSensor())
    if light.getLightSensor() < 2:
        light.toggleLight(1)
    else:
        light.toggleLight(0)
    time.sleep(0.2)


# testing method
def calibrateLightSensor():
    light.toggleLight(1)
    print(light.lightSensorTimer())
    time.sleep(0.5)


# testing method
def testMotor():
    motor.moveForward(10)


# previous auton method without distance sensor
def autonomous():
    if light.getButton() == 1:
        print("button pressed")
        light.toggleLight(1)
        while True:
            if light.isBlack():
                print("see black")
                motor.moveForward(10)
            else:
                print("see white")
                motor.moveBackward(10)
                if random.randint(0, 1) == 0:
                    motor.turnLeft(10)
                else:
                    motor.turnRight(10)


# auton with distance sensors
def betterAuton():
    # debug comments
    print(
        "distance: ",
        light.getDistance(),
        " light value: ",
        light.getLightSensor(),
        " isBlack: ",
        light.isBlack(),
    )

    if light.getButton() == 1:
        # wait 5 seconds
        print("button pressed")
        time.sleep(5)

        # move forward to get sufficiently away from edge
        motor.moveForward(1.5)
        while True:
            distance = light.getDistance()

            # debug
            print(
                "distance: ",
                distance,
                " light value: ",
                light.getLightSensor(),
                " isBlack: ",
                light.isBlack(),
            )
            # check if line is not black
            if not light.isBlack():
                print("see white")
                motor.moveBackward(1)
                if random.randint(0, 1) == 0:
                    motor.turnLeft(2)
                else:
                    motor.turnRight(2)
            else:
                # turns unti sees another robot
                if distance < 60:
                    motor.moveForward(0.5)
                else:
                    motor.turnLeft(0.1)


# Main Method

try:
    while True:
        betterAuton()
        # calibrateLightSensor()
except KeyboardInterrupt:
    print("Terminating Program")
finally:
    GPIO.cleanup()
