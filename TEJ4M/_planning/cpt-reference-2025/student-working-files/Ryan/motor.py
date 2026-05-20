import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 16
BUTTON_PIN = 19

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.LOW)
        else:
            GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("exiting")

finally:
    GPIO.cleanup()
