import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

while True:
    buttonvalue = GPIO.input(26)
    print("The button is: "+str(buttonvalue))
    #time.sleep(0.5)
    if buttonvalue == 1:
          GPIO.output(17, True)
    else: GPIO.output(17, False)
