import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        time.sleep(1)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    print("Exiting")
finally:
    GPIO.cleanup