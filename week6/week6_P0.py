import sys

sys.path.append('./base/')
import sensorBME280_AF


if __name__ == "__main__":

    # Göteborg's air pressure (hPa) at sea level
    sea_level_pressure = 1018     
    
    myBME = sensorBME280_AF.sensorBME280_AF(sea_level_pressure)

    print("Envirnmental Measurement \n")

    while True:
        
        dataDic = myBME.read(10, 1 )
    
        print("Average Temperature: {:.2f} °C".format(dataDic["temperature"]))
        print("Average Pressure: {:.2f} hPa".format(dataDic["pressure"]))
        print("Average Humidity: {:.2f} %".format( dataDic["humidity"] ))
        print("Average Altitude: {:.2f} %".format( dataDic["altitude"] ))
        print("\n")