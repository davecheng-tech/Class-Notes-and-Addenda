import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# variables for start stop button and light sensor readings 
startup = False
buffer = False
frontRightSensor = 0
frontLeftSensor = 0
backRightSensor = 0
backLeftSensor = 0
ultraSonicSensor = 0
frontRightSensorBlackReading = 35000
frontLeftSensorBlackReading = 70000
backRightSensorBlackReading = 40000
backLeftSensorBlackReading = 20000

# set GPIO Pins for our ultrasonic sensor
GPIO_TRIGGER = 21
GPIO_ECHO = 20

# settings up GPIO pins - 5 is for LED, 17, 23, 24, 27 are motors, 26 is for our button 
GPIO.setup(5, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(26, GPIO.IN) 
GPIO.setup(GPIO_ECHO, GPIO.IN)

# uses the ultra sonic sensor to measure the distance between our robot and the other robot 
def distance():

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

# fucntion to measure the light sensor value and how much light it reads 
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

        # checks if the start button is pressed and the robot is not already started or in buffer mode
        if (GPIO.input(26) == 1 and startup == False and buffer == False): 
            
            print("Starting up")
            GPIO.output(5, GPIO.HIGH)
            time.sleep(5)
            startup = True
            
        while (startup == True):

            frontLeftSensor = rc_time(18)
            frontRightSensor = rc_time(12)
            backLeftSensor = rc_time(22)
            backRightSensor = rc_time(6)

            # checks if all sensors are not reading a white line 
            if (backRightSensor > backRightSensorBlackReading and frontRightSensor > frontRightSensorBlackReading and frontLeftSensor > frontLeftSensorBlackReading and backLeftSensor > backLeftSensorBlackReading):

                # sets the ultrasonic sensor to read the distance
                ultraSonicSensor = distance()

                # checksd if there is anything infront of the robot using the ultrasonic sensor
                if (ultraSonicSensor < 120):

                    # moves fowrads if there is an obstacle infront of the robot
                    GPIO.output(23, GPIO.LOW)
                    GPIO.output(24, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(23, GPIO.LOW)
                    GPIO.output(24, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)

                else:

                    # rotate to scans 
                    GPIO.output(23, GPIO.HIGH)
                    GPIO.output(24, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(23, GPIO.LOW)
                    GPIO.output(24, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)                    
                


            # checks if the front left sensor is reading a white line  
            elif (frontLeftSensor < frontLeftSensorBlackReading):
                
                # move backwards to get away form the edge of the map 
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.75)

                # rotates 90 degrees 
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.75)

                # moves forwards to get away from the edge of the map
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.5)

                # stops the robot to give sensors time to read again
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
        
            # checks if the front right sensor is reading a white line  
            elif (frontRightSensor < frontRightSensorBlackReading):

                
                # moves backwards to get away from the edge of the map
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.75)

                # rotates 90 degrees
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.75)

                # moves forwards to get away from the edge of the map
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.5)

                # stops the robot to give sensors time to read again
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
    
            # checks if the back left sensor is reading a white line  
            elif (backLeftSensor < backLeftSensorBlackReading):

                # moves forwards to get away from the edge of the map
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.75)

                # rotates 90 degrees
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.75)
                
                # moves forwards to get away from the edge of the map
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.5)

                # stops the robot to give sensors time to read again
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)

            # checks if the back right sensor is reading a white line  
            elif (backRightSensor < backRightSensorBlackReading):

                # moves forwards to get away from the edge of the map
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.75)

                # rotates 90 degrees
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.75)

                # moves forwards to get away from the edge of the map
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.5)

                # stops the robot to give sensors time to read again
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
    
            # start and stop button 
            if (GPIO.input(26) == 1 and startup == True):

                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)  
                GPIO.output(5, GPIO.LOW)
                print("Shutting Down")
                buffer = True
                startup = False
            
except KeyboardInterrupt or startup == False:

    GPIO.output(5, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)  
    print("Exiting")

finally:

    GPIO.cleanup()
    
