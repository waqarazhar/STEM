import sys
from time import sleep
import RPi.GPIO as GPIO


# Update the number based on your connection
LED_YELLOW = 25
LED_RED = 17
LED_GREEN = 22


def initilizePi():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)

def printUsage():
    print("Select the direction that you want to turn ")
    print("\t To turn left --> press LEFT and enter ")
    print("\t To turn right --> press RIGHT and enter ")
    
# You have to complete this function
def blink(LED_NUMBER, DELAY):
    GPIO.output(LED_NUMBER, 1)
    sleep(DELAY)
    GPIO.output(LED_NUMBER, 0)
    sleep(DELAY)


# You have to complete this function
def reapeatBlink(LED_NUMBER, DELAY, COUNT):
    for x in range(0, COUNT):
        # Add blink function here
        blink(LED_NUMBER, DELAY)                    

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
            print("Blining RED LED ")     
            # blink red LED on left
            reapeatBlink(LED_RED, 1, 5)
            printUsage()

        elif( key == "right" ):
            print("Turning GREEN LED")     
            # blink red LED on left
            reapeatBlink(LED_GREEN, 1, 5)
            printUsage()

        elif( key == "exit" ):
            print("bye ! Pi is closing")
            exit(1)    
        else:
            print("Invalid Key")
            printUsage()


