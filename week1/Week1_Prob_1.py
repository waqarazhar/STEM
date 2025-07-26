import sys
from time import sleep
import RPi.GPIO as GPIO

sys.path.append('./base/')

import button 

# Update the number based on your connection
LED_YELLOW = 22
LED_RED = 17
SWITCH = 21
DELAY = 1
LEFT_BUTTON=27
RIGHT_BUTTON=27
LED_GREEN = 

def initilizePi():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_YELLOW, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# You have to complete this function
def blink(LED_NUMBER, DELAY):
    

# You have to complete this function
def reapeatBlink(LED_NUMBER, DELAY, COUNT):

    for x in range(0, COUNT):
                    
                  

if __name__ == "__main__":

    # Dont Change this code below
    initilizePi()
    # Dont Change this code above

    GPIO.output(LED_RED, 1)

    #leftButton = button.button("left", LEFT_BUTTON)

    # This loop runs continuesly
    while(1):
        
        pass
        """
        if( check button here ): 
            print some message
            blink led specified number of time
            
        else:
            GPIO.output(LED_RED, 0)
        """


