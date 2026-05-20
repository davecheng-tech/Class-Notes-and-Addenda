# import libraries
# import api to access the raspberry pi’s GPIO pins… represented by variable GPIO
import RPi.GPIO as GPIO
# import time api to we can make our pi pause/sleep
import time

# Use BCM pin numbering
# setting the board to BCM mode (broadcom mode)... 
# we can access the GPIO pins based on its GPIO number and NOT its board number
GPIO.setmode(GPIO.BCM)

# Set up GPIO 16 as an output
LED_PIN = 16
# setting up the pin as an output pin
GPIO.setup(LED_PIN, GPIO.OUT)
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # LED off
        time.sleep(1)                    # Wait 1 second
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    GPIO.cleanup()  # Reset GPIO settings

