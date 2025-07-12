import RPi.GPIO as GPIO
import time

class button():
    
    name=""
    pin=27
    state=1
       
    def __init__(self, name, pin):
        
        self.name = name
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def read(self):
        input = GPIO.input(self.pin)
        if( self.state == 1 and input == 0 ):
            print(self.name , "is pressed")
            time.sleep(0.2)
            self.state = input
            return 1
        else:
            self.state = input
            return 0
    
    def readStable(self):
        input = GPIO.input(self.pin)
        if( self.state == 1 and input == 0 ):
            while(GPIO.input(self.pin) == 0 ):
                pass
            print(self.name , "is pressed")
            self.state = input
            return 1
        else:
            self.state = input
            return 0


if __name__ == "__main__":
      
      mybutton = button("left",27)

      while(1):
            x = mybutton.readStable()
            if(x == 1):
                print(x)