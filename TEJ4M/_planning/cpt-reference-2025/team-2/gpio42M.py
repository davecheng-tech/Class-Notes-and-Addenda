import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        print("test complete")
        

except KeyboardInterrupt:
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    print("Exiting")
finally:
    GPIO.cleanup
    
    ##pin 17, 27 for motor2