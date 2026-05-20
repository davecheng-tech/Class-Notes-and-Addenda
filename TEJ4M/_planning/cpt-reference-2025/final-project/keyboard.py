import RPi.GPIO as GPIO
import random
import time
import light
import motor
import curses

light.lightInputPin = 22
light.lightOutputPin = 16
light.buttonInputPin = 19

motor.rightForward = 23
motor.rightBackward = 24
motor.leftForward = 21
motor.leftBackward = 20

GPIO.setmode(GPIO.BCM)
motor.motorSetup()
light.toggleLight(1)
print("motor setup")
# temporary distance sensor variables


def testLights():
    print(light.getLightSensor())
    if light.getLightSensor() < 2:
        light.toggleLight(1)
    else:
        light.toggleLight(0)
    time.sleep(0.2)


def calibrateLightSensor():
    light.toggleLight(1)
    print(light.lightSensorTimer())
    time.sleep(0.5)


def testMotor():
    motor.moveForward(10)


def autonomous():
    if light.getButton() == 1:
        print("button pressed")
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


def betterAuton():
    if light.getButton() == 1:
        print("button pressed")
        while True:
            distance = light.getDistance()
            if not light.isBlack():
                print("see white")
                motor.moveBackward(10)
                if random.randint(0, 1) == 0:
                    motor.turnLeft(10)
                else:
                    motor.turnRight(10)
            else:
                if distance < 175:
                    motor.moveForward(0.3)
                else:
                    motor.turnLeft(1)


def keyboardControls(stdscr):
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.addstr(0, 0, "movement test")
    try:
        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                motor.moveForward(0.1)
            if key == curses.KEY_DOWN:
                motor.moveBackward(0.1)
            if key == curses.KEY_LEFT:
                motor.turnLeft(0.1)
            if key == curses.KEY_RIGHT:
                motor.turnRight(0.1)
    except KeyboardInterrupt:
        print("Terminating Program")
    finally:
        GPIO.cleanup()


# Main Method

curses.wrapper(keyboardControls)
