import RPi.GPIO as GPIO
import time
# for future, BCM is the GPIO pin number, Board means the pin number on the board, not the relaive GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(16, GPIO.OUT)

while True:
    buttonvalue = GPIO.input(26)
    print("The button is: "+str(buttonvalue))
    #time.sleep(0.5)
    if buttonvalue == 1:
          GPIO.output(16, True)
    else: GPIO.output(16, False)

