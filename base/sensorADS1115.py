import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class sensorADS1115():
    """docstring for sensorADS1115"""

    def __init__(self, params, verbose = False):
        super().__init__()
        self.params = params
        self.verbose = verbose
        self.name = params["name"]
        self.address = 0x48
        self.i2cPort = params["port"]
        self.channel = int(params["channel"])


        if self.verbose :
            print("Initializing ", self.params["name"], "of type : ", self.params["type"])

        # Initialize I2C and ADS1115 ADC
        self.bus = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.bus, address=self.address)


    def read(self):

        data = {}

        # Select Analog Input Channel (A0)
        value = AnalogIn(self.ads, self.channel)
        if self.verbose :
            print("Voltage : ", value.voltage)

        data[self.name] = value.voltage
        return data




if __name__ == '__main__':

    params = {}
    params["name"] = "water sensor"
    params["type"] = "sensorADS1115"
    params["port"] = 1
    params["channel"] = 0
    
    myAnalog = sensorADS1115(params,verbose=True)

    for i in range(0, 10):
        myAnalog.read()

        time.sleep(2)


