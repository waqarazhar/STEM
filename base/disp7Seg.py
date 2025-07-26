import tm1637
import time 

class disp7Seg():
    """docstring for disp7Seg"""

    def __init__(self, clk, dio):
        super().__init__()
        
        self.tm = tm1637.TM1637(clk=clk, dio=dio)
        
        time.sleep(2)

        self.tm.numbers(0,0,0)

    def write(self, number):

        self.tm.number(number)
    
