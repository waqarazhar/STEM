import sys
from time import sleep
import RPi.GPIO as GPIO


# Update the number based on your connection
LED_YELLOW = 25
LED_RED = 17
LED_GREEN = 22


def initilizePi():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_YELLOW, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)

def printUsage():
    print("To Control LED ")
    print("\t Turn it on --> press ON")
    print("\t Turn it off --> press OFF ")

# You have to complete this function
def blink(LED_NUMBER, DELAY):
    pass

# You have to complete this function
def reapeatBlink(LED_NUMBER, DELAY, COUNT):
    pass              

if __name__ == "__main__":

    # Dont Change this code below
    initilizePi()
    # Dont Change this code above
    
    print("Hello My name is Pi \n ")
    
    printUsage()
    
    # This loop is needed to run continuesly
    while(1):
        
        key = input()
        key = key.lower()

        if(key == "on"): 
            print("Turning LED ON")     
            # Write code to turn RED, GREEN, YELLOW LED ON
            GPIO.output(LED_RED, 1)
            GPIO.output(LED_GREEN, 1)
            GPIO.output(LED_YELLOW, 1)
            printUsage()

        elif( key == "off" ):
            print("Turning LED OFF")     
            # Write code to turn RED, GREEN, YELLOW LED ON
            GPIO.output(LED_RED, 0)
            GPIO.output(LED_GREEN, 0)
            GPIO.output(LED_YELLOW, 0)
            printUsage()

        elif( key == "exit" ):
            print("bye ! Pi is closing")
            exit(1)    
        else:
            print("Invalid Key")
            printUsage()


