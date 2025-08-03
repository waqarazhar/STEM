import sys
from time import sleep
import RPi.GPIO as GPIO
import signal

sys.path.append('/home/rpi/repos/STEM_Course/base/')
import disp7Seg
import button 
import sensorSR04
import inputKey

def printUsage():
    print("Car Gear System")
    print("\t Press 'R' and enter to put car in reverse gear ")
    print("\t Press 'N' and enter to put car in neutral ")
    print("\t Press 'E' and enter to exit ")


if __name__ == "__main__":

    tm = disp7Seg.disp7Seg(clk=21, dio=20)

    mysensor = sensorSR04.sensorSR04(trigger_pin=26, echo_pin=16)

    mykey = inputKey.inputKey(1)

    state = "" 

    printUsage()
    
    while(1):

        key = mykey.get()

        if(key == "r"): 
            state = "Reversing"
            print("Reversing ! ")                    

        elif( key == "n" ):
            print("Neutral !") 
            state = "Neutral"    
           
        elif( key == "e" ):
            print("bye ! Pi is closing")
            exit(1)    

        if(state == "Reversing"):
            distance = mysensor.measureDistance(1)
            distance_mm = int(distance*10)
            tm.write( int(distance_mm) )
            print("distance :", distance_mm)

    
    