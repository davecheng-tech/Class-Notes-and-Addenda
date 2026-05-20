import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# define the pin that goes to the circuit
pin_to_circuit = 22


def getLightSensor(pin_to_circuit):
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)

    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)
    if GPIO.input(pin_to_circuit) == GPIO.LOW:
        print("0")
    elif GPIO.input(pin_to_circuit) == GPIO.HIGH:
        print("1")
    else:
        print("An error has occured")


def getLightValue(pin_to_circuit):
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)

    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)
    print(GPIO.input(pin_to_circuit))


while True:
    getLightValue(pin_to_circuit)
    time.sleep(0.5)
