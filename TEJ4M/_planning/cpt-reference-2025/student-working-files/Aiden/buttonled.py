import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
LED_PIN = 16
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
	buttonvalue = GPIO.input(19)
	if buttonvalue == 0:
		GPIO.output(16,GPIO.HIGH)
	else:
		GPIO.output(16, GPIO.LOW)
	time.sleep(0.2)

	
