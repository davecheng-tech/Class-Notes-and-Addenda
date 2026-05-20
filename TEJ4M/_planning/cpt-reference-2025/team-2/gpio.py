import RPi.GPIO as GPIO
import time
# for future, BCM is the GPIO pin number, Board means the pin number on the board, not the relaive GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
try:
    while True:
       # GPIO.output(5, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        
except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.cleanup
