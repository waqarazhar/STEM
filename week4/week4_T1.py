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
    print("\t Exit --> type 'exit' and enter ")

if __name__ == "__main__":
    # Exercise 1: Initialize the 7-segment display
    # The display uses GPIO pins 3 (CLK) and 2 (DIO)
    # TODO: Create the display object by completing the line below
    tm = disp7Seg.disp7Seg(clk=3, dio=2)
    
    time.sleep(2)  # Give the display time to initialize

    printUsage()  # Show instructions

    count = 0  # This will store our current count
    tm.write(count)  # Show initial count (0) on display

    while(1):
        # Exercise 2: Get user input
        # TODO: What does this line do? Write your answer as a comment:
        # This line _______________________________
        key = input()
        key = key.lower()  # Convert to lowercase

        if(key == "+"): 
            print("Incrementing Counter ")     
            # Exercise 3: Increment the counter
            # TODO: Add 1 to the count variable
            count = count + 1 
            tm.write(count)  # Update display
            time.sleep(0.5)  # Small delay

        elif(key == "-"):
            print("Decrementing Counter ")     
            # Exercise 4: Decrement the counter
            # TODO: Subtract 1 from the count variable
            count = count - 1
            tm.write(count)  # Update display
            time.sleep(0.5)  # Small delay

        elif(key == "exit"):
            print("Goodbye! The program is closing.")
            exit(1)    
        else:
            print("Invalid Key")
            printUsage()

        # Exercise 5 (Bonus): Add a new feature!
        # TODO: Can you add another command that does something special?
        # For example, maybe pressing "c" could reset the counter to zero
        # elif(key == "c"):
        #     count = 0
        #     tm.write(count)
        #     print("Counter reset!")
