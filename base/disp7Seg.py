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

    def writeFloat(self, numberFloat, verbose = False):

        num = round(numberFloat, 2)

        num1 = int(num)
        num2 = int((num -num1)*100) 
        
        if verbose == True:
            print(num)
            print("num1 : ", num1)
            print("num2 : ", num2)
        
        self.tm.numbers(num1, num2)



if __name__ == "__main__":

    myDisp = disp7Seg(clk=21, dio=20)

    myDisp.write(100)

    myDisp.writeFloat(20.17)