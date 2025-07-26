import time 
import sys
import tm1637
import sys

sys.path.append('./base/')
import disp7Seg
import button

def printUsage():
    print("\t Increment --> press + and enter ")
    print("\t Decrement --> press - and enter ")


if __name__ == "__main__":
    
    tm = disp7Seg.disp7Seg(clk=3, dio=2)
    
    time.sleep(2)

    printUsage()

    count = 0

    while(1):
        
        
        key = input()
        key = key.lower()

        if(key == "+"): 
            print("Incrementing Counter ")     
            # increment the count
            count = count + 1 
            tm.write(count)
            time.sleep(2)

        elif( key == "-" ):
            print("Decrementing Counter ")     
            # decrement the count
            count = count - 1
            tm.write(count)

        elif( key == "exit" ):
            print("bye ! Pi is closing")
            exit(1)    
        else:
            print("Invalid Key")
            printUsage()

    

    



        

