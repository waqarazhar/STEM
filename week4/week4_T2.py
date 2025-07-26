import time 
import sys
import tm1637

sys.path.append('./base/')
import disp7Seg
import button

def printUsage():
    print("\t Increment --> press the TOP button (GPIO 25)")
    print("\t Decrement --> press the BOTTOM button (GPIO 22)")

if __name__ == "__main__":
    # --- Exercise 1: Set Up GPIO Pins ---
    # TODO: Assign the correct GPIO pin numbers for the buttons
    # HINT: UP button = 25, DOWN button = 22
    UP_BUTTON = ____
    DOWN_BUTTON = ____
    
    # Initialize the 7-segment display (CLK=3, DIO=2)
    tm = disp7Seg.disp7Seg(clk=3, dio=2)
    time.sleep(2)  # Wait for display to start

    # --- Exercise 2: Initialize Buttons ---
    # TODO: Create button objects for "up" and "down"
    # HINT: Use button.button(name, pin)
    upButton = button.button("up button", ____)
    downButton = button.button("down button", ____)

    printUsage()  # Show instructions
    count = 0     # Start counting from 0
    tm.write(count)  # Display initial count

    while True:
        # --- Exercise 3: Read Button Presses ---
        # TODO: Check if the UP button is pressed
        # HINT: Use upButton.readStable() == 1
        if(____ == 1): 
            print("Incrementing Counter")     
            # TODO: Increase count by 1
            count = ____
            tm.write(count)
            time.sleep(0.5)  # Debounce delay

        # TODO: Check if the DOWN button is pressed
        elif(____ == 1):
            print("Decrementing Counter")     
            # TODO: Decrease count by 1
            count = ____
            tm.write(count)
            time.sleep(0.5)  # Debounce delay

        # --- Exercise 4 (Bonus): Add a Reset Feature ---
        # TODO: Can you add a way to reset to 0?
        # HINT: Use another button or a long press!
        # elif(____):
        #     count = 0
        #     tm.write(count)
        #     print("Counter reset!")
