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
    print("Select the direction that you want to turn ")
    print("\t To turn left --> press LEFT and enter ")
    print("\t To turn right --> press RIGHT and enter ")
    
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

        if(key == "left"): 
            print("Blinking RED LED ")     
            # blink red LED 3 times
            
            printUsage()

        elif( key == "right" ):
            print("Blinking GREEN LED")     
            # blink red LED 3 times
            
            printUsage()

        elif( key == "exit" ):
            print("bye ! Pi is closing")
            exit(1)    
        else:
            print("Invalid Key")
            printUsage()


