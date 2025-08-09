import board
import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

class sensorBME280_AF( ):
    """docstring for sensorBME280"""
    def __init__(self, seaLevelPressure):
        super().__init__()
        
        # BME280 sensor address (default address)
        self.address = 0x76
        self.seaLevelPressure = seaLevelPressure

        # Create the I2C bus
        self.bus = busio.I2C(board.SCL, board.SDA)
        
        # Load calibration parameters
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.bus, address=self.address)

        # Set the pressure at sea level
        self.bme280.sea_level_pressure = self.seaLevelPressure

    def read(self, readingCount, delay, verbose=False):

        dataDic = {}

        avgTemprature = 0
        avgPressure = 0
        avgHumidity = 0
        avgAltitude = 0

        for i in range(0, readingCount):
            
            # Read sensor data
            temperature = self.bme280.temperature
            pressure = self.bme280.pressure
            humidity = self.bme280.humidity
            altitude = self.bme280.altitude


            if verbose:
                print("\nTemperature: %0.1f C" % temperature)
                print("Humidity: %0.1f %%" % humidity)
                print("Pressure: %0.1f hPa" % pressure)
                print("Altitude = %0.2f meters" % altitude)

            avgTemprature += temperature
            avgPressure += pressure
            avgHumidity += humidity
            avgAltitude += altitude

            time.sleep(delay)

        # Extract temperature, pressure, and humidity
        dataDic["temperature"] = avgTemprature/readingCount
        dataDic["pressure"] = avgPressure/readingCount
        dataDic["humidity"] = avgHumidity/readingCount
        dataDic["altitude"] = avgAltitude/readingCount

        if verbose:
            # Print the readings
            print("Average Temperature: {:.2f} °C".format(dataDic["temperature"]))
            print("Average Pressure: {:.2f} hPa".format(dataDic["pressure"]))
            print("Average Humidity: {:.2f} %".format( dataDic["humidity"] ))
            print("Average Altitude: {:.2f} %".format( dataDic["altitude"] ))

        return dataDic


if __name__ == '__main__':

    sea_level_pressure = 1018
    
    myBME = sensorBME280_AF(sea_level_pressure)

    myBME.read(10, 1, verbose= True)
