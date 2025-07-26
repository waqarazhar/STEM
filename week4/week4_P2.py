import time 
import sys
import tm1637
import sys

sys.path.append('./base/')
import disp7Seg
import button

def printUsage():
    print("\t Increment --> press button on top ")
    print("\t Decrement --> press button on bottom ")


if __name__ == "__main__":

    UP_BUTTON = 25
    DOWN_BUTTON = 22
    
    tm = disp7Seg.disp7Seg(clk=3, dio=2)
    
    time.sleep(2)

    upButton = button.button("up buuton", UP_BUTTON)
    downButton = button.button("down buuton", DOWN_BUTTON)

    printUsage()

    count = 0

    while(1):
        

        if(upButton.readStable() == 1): 
            print("Incrementing Counter ")     
            # increment the count
            count = count + 1 
            tm.write(count)
            time.sleep(0.5)

        elif( downButton.readStable() == 1 ):
            print("Decrementing Counter ")     
            # decrement the count
            count = count - 1
            tm.write(count)
            time.sleep(0.5)


    

    



        

