import sys
from time import sleep
import RPi.GPIO as GPIO

sys.path.append('./base/')
import button 

# Update the number based on your connection
LED_YELLOW = 25
LED_RED = 17
LED_GREEN = 22

LEFT_BUTTON = 24
RIGHT_BUTTON = 23


def initilizePi():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_YELLOW, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)

def printUsage():
    print("To cross the road press right or left button button \n")
    
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
    leftButton = button.button("left buuton", LEFT_BUTTON)
    rightButton = button.button("right button", RIGHT_BUTTON)

    # Dont Change this code above
    
    print("Hello My name is Pi \n ")
    
    printUsage()
    
    # This loop is needed to run continuesly
    while(1):
            
        if( (leftButton.readStable() == 1) or (rightButton.readStable()) ): 
            
            print(" Please Wait ! Cars are on the road")

            # Add a sleep for 5 sec
            
            # Turn the red led ON for trafic
            

            # Wiat for 5 sec

            # Turn the yellow led ON for pedistrians     
            print(" Please cross the road ")

            # Wiat for 10 sec
            print(" Please stop crossing the road ")

            # Turn the yellow led OFF for pedistrians        

        else: 
            #print("right button is pressed")     
            GPIO.output(LED_RED, 0)
            GPIO.output(LED_GREEN, 1)


