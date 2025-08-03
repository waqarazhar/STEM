import time 
import sys
import sys
import signal

sys.path.append('./base/')
import disp7Seg
import button

def printUsage():
    print("\t Start/Stop --> press button on top ")
    print("\t Reset --> press button on bottom ")


class stopWatch():

    """docstring for stopWatch"""
    def __init__(self, delay):
        super(stopWatch, self).__init__()
        self.count = 0
        self.started = False
        self.delay = delay
        self.display = disp7Seg.disp7Seg(clk=21, dio=20)
        signal.signal(signal.SIGALRM, self.handler)

    def start(self):
        self.started = True
        signal.setitimer(signal.ITIMER_REAL, self.delay, self.delay)

    def stop(self):
        self.started = False
        signal.setitimer(signal.ITIMER_REAL, 0)

    def inrementCount(self):
        if(self.started == True):
            print("increment", self.count)
            self.count = self.count + 1
            self.display.write(self.count )
            time.sleep(0.05)

    def handler(self, signum,frame):
        
        if(self.started == True):
            print("increment", self.count)
            self.count = self.count + 1
            self.display.write(self.count )
            time.sleep(0.05)
            
    def runStatus(self):
        return self.started

    
    def reset(self):
        self.count = 0
        self.started = False
        self.display.write(self.count )


if __name__ == "__main__":

    START_BUTTON = 25
    RESET_BUTTON = 22

    watch = stopWatch(1)
    
    time.sleep(2)

    start = button.button("start/stop buuton", START_BUTTON)
    reset = button.button("reset button", RESET_BUTTON)

    printUsage()


    while(1):

        if(start.readStable() == 1):
            time.sleep(0.2)

            if(watch.runStatus() == False):
                print("Starting Stop Watch")     
                watch.start()
            
            elif(watch.runStatus() == True):
                print("Stoping Stop Watch")
                watch.stop()

        elif( reset.readStable() == 1 ):
            print("Reseting Counter")     
            watch.reset()

            


    

    



        

