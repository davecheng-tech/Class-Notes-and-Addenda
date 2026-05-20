import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.IN)
GPIO.setup(16, GPIO.OUT)

startup = False
buffer = False

def rc_time (pin_to_circuit):

    count = 0

    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count

try:    

    while True:

        if (GPIO.input(26) == 1 and startup == False and buffer == False): 
            GPIO.output(5, GPIO.HIGH)
            startup = True
            print(startup)
            time.sleep(1)

        while (startup == True):

            print("6 " + str(rc_time(6)))
            print("12 " + str(rc_time(12)))
            print("18 " + str(rc_time(18)))
            print("22 " + str(rc_time(22)))
            time.sleep(1)

            if (GPIO.input(26) == 1 and startup == True):
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)  
                buffer = True
                startup = False
            
except KeyboardInterrupt or startup == False:
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)  
    print("Exiting")

finally:
    GPIO.cleanup
    
    ##pin 17, 27 for motor2