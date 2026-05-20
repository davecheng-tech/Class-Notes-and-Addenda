import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO pin setup
rightForward = 23
rightBackward = 24
leftForward = 20
leftBackward = 21


def motorSetup():
    GPIO.setup(rightForward, GPIO.OUT)
    GPIO.setup(rightBackward, GPIO.OUT)
    GPIO.setup(leftForward, GPIO.OUT)
    GPIO.setup(leftBackward, GPIO.OUT)


def moveForward(duration):
    GPIO.output(rightForward, GPIO.HIGH)
    GPIO.output(rightBackward, GPIO.LOW)
    GPIO.output(leftForward, GPIO.HIGH)
    GPIO.output(leftBackward, GPIO.LOW)
    time.sleep(duration)
    stop()


def moveBackward(duration):
    GPIO.output(rightForward, GPIO.LOW)
    GPIO.output(rightBackward, GPIO.HIGH)
    GPIO.output(leftForward, GPIO.LOW)
    GPIO.output(leftBackward, GPIO.HIGH)
    time.sleep(duration)
    stop()


def turnLeft(duration):
    GPIO.output(rightForward, GPIO.HIGH)
    GPIO.output(rightBackward, GPIO.LOW)
    GPIO.output(leftForward, GPIO.LOW)
    GPIO.output(leftBackward, GPIO.HIGH)
    time.sleep(duration)
    stop()


def turnRight(duration):
    GPIO.output(rightForward, GPIO.LOW)
    GPIO.output(rightBackward, GPIO.HIGH)
    GPIO.output(leftForward, GPIO.HIGH)
    GPIO.output(leftBackward, GPIO.LOW)
    time.sleep(duration)
    stop()


def stop():
    GPIO.output(rightForward, GPIO.LOW)
    GPIO.output(rightBackward, GPIO.LOW)
    GPIO.output(leftForward, GPIO.LOW)
    GPIO.output(leftBackward, GPIO.LOW)
