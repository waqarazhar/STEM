# Import necessary libraries
import time 
import sys
import tm1637
import signal  # Used for timer functionality

# Add custom module path
sys.path.append('./base/')
# Import custom modules for 7-segment display and button handling
import disp7Seg
import button

def printUsage():
    """Print instructions for using the stopwatch"""
    print("\t Start/Stop --> Press TOP button (GPIO 25)")
    print("\t Reset --> Press BOTTOM button (GPIO 22)")

class stopWatch():
    """Stopwatch class that handles timing and display"""
    
    def __init__(self, delay):
        """Initialize the stopwatch with given delay between updates"""
        self.count = 0        # Current count value
        self.started = False  # Is stopwatch running?
        self.delay = delay    # Delay between updates (in seconds)
        
        # Initialize 7-segment display on GPIO pins 3 (CLK) and 2 (DIO)
        self.display = disp7Seg.disp7Seg(clk=3, dio=2)
        
        # Set up signal handler for timer interrupts
        signal.signal(signal.SIGALRM, self.handler)

    def start(self):
        """Start the stopwatch timer"""
        self.started = True
        # Set timer to trigger every 'delay' seconds
        signal.setitimer(signal.ITIMER_REAL, self.delay, self.delay)

    def stop(self):
        """Stop the stopwatch timer"""
        self.started = False
        # Disable the timer
        signal.setitimer(signal.ITIMER_REAL, 0)

    def handler(self, signum, frame):
        """Handler function called by timer interrupt"""
        if self.started:
            # Increment count and update display
            self.count += 1
            self.display.write(self.count)
            time.sleep(0.05)  # Small delay for display stability

    def reset(self):
        """Reset the stopwatch to zero"""
        self.count = 0
        self.started = False
        self.display.write(self.count)  # Show 0 on display

if __name__ == "__main__":
    # GPIO pin numbers for buttons
    START_BUTTON = 25  # Top button (start/stop)
    RESET_BUTTON = 22   # Bottom button (reset)

    # Create stopwatch instance with 1-second updates
    watch = stopWatch(1)
    time.sleep(2)  # Give display time to initialize

    # Initialize buttons
    start = button.button("start/stop", START_BUTTON)
    reset = button.button("reset", RESET_BUTTON)
    
    # Print usage instructions
    printUsage()

    # Main program loop
    while True:
        # [EXERCISE 1: START/STOP BUTTON]
        # HINT: Check if start button is pressed (use readStable())
        if __________ == 1:
            # HINT: Add small delay to prevent button bouncing
            __________.sleep(0.2)
            
            # [EXERCISE 2: TOGGLE TIMER]
            # HINT: If watch is stopped, start it. Else, stop it.
            if watch.__________ == False:
                print("START")
                watch.__________()
            else:
                print("STOP")
                watch.__________()
        
        # [EXERCISE 3: RESET BUTTON]
        # HINT: Check reset button separately (use elif)
        __________ reset.readStable() == 1:
            print("RESET")
            watch.__________()
