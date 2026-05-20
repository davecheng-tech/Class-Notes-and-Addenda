import RPi.GPIO as GPIO
import time

ledPin = 16    # define ledPin
buttonPin = 26    # define buttonPin


    
GPIO.setmode(GPIO.BCM)      # use PHYSICAL GPIO Numbering
GPIO.setup(ledPin, GPIO.OUT)   # set ledPin to OUTPUT mode
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    

logic = 0
while True:
    while GPIO.input(buttonPin) == 1:
        time.sleep(0.5)
             
    logic = logic + 1
    if logic > 1:
        logic = 0
        
    GPIO.output(ledPin,logic)   
                   
    while GPIO.input(buttonPin) == 0:
        time.sleep(0.5)

