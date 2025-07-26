import time 
import sys
import tm1637

sys.path.append('/home/rpi/STEM/base/')
import disp7Seg
import button

def printUsage():
    """Print instructions for the interactive counter"""
    print("\n=== 7-Segment Counter Controls ===")
    print("Increment counter: Press '+' and ENTER")
    print("Decrement counter: Press '-' and ENTER")
    print("Reset counter:     Press '0' and ENTER")
    print("Exit program:      Type 'exit' and ENTER")

if __name__ == "__main__":
    # -------------------------------------------------------------------
    # EXERCISE 1: HARDWARE SETUP
    # Complete the display initialization below
    # HINT: The display uses GPIO pin 3 for CLK and pin 2 for DIO
    # -------------------------------------------------------------------
    tm = disp7Seg.disp7Seg(clk=____, dio=____)
    
    # Wait for display to initialize
    time.sleep(2)  

    # Show instructions
    printUsage()  

    # Start counting from 0
    count = 0  
    tm.write(count)  # Display initial value

    while True:
        # -------------------------------------------------------------------
        # EXERCISE 2: USER INPUT HANDLING
        # What does the input() function do?
        # Write your answer below:
        # ANSWER: This line _______________________________
        # -------------------------------------------------------------------
        key = input("Enter command: ")
        key = key.lower()  # Convert to lowercase for case-insensitive comparison

        # -------------------------------------------------------------------
        # EXERCISE 3: COUNTER CONTROLS
        # Complete the missing parts for each control:
        # -------------------------------------------------------------------
        if(key == "+"): 
            print("Incrementing Counter")     
            # TODO: Add 1 to the count
            count = ____
            tm.write(count)
            time.sleep(0.3)  # Small delay for display stability

        elif(key == "-"):
            print("Decrementing Counter")     
            # TODO: Subtract 1 from the count
            count = ____
            tm.write(count)
            time.sleep(0.3)

        elif(key == "0"):
            print("Resetting Counter")
            # TODO: Implement reset functionality
            count = ____
            tm.write(____)
            time.sleep(0.5)

        elif(key == "exit"):
            print("Goodbye! The program is closing.")
            exit(0)    
        else:
            print("Invalid command!")
            printUsage()

        # -------------------------------------------------------------------
        # EXERCISE 4 (BONUS): ADD YOUR OWN FEATURE!
        # Can you add another command? Some ideas:
        # - Double increment (press '++')
        # - Set specific value (press '5' to go to 5)
        # - Blink the display
        # 
        # TODO: Uncomment and complete this section
        # elif(key == ____):
        #     print("Special feature activated!")
        #     [Your code here]
        # -------------------------------------------------------------------
