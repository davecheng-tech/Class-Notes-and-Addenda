import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

while True:
	buttonvalue = GPIO.input(26)
	print("The button is: "+str(buttonvalue))
	time.sleep(0.5)
