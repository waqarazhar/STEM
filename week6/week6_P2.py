import sys
import time


sys.path.append('./base/')
import disp7Seg
import sensorADS1115

if __name__ == '__main__':

    name = "joy stick"
    paramX = {}
    paramX["name"] = name
    paramX["type"] = "sensorADS1115"
    paramX["port"] = 1
    paramX["channel"] = 0

    paramY = {}
    paramY["name"] = name
    paramY["type"] = "sensorADS1115"
    paramY["port"] = 1
    paramY["channel"] = 1
    
    xAxis = sensorADS1115.sensorADS1115(paramX,verbose=False)

    yAxis = sensorADS1115.sensorADS1115(paramY,verbose=False)

    while True:

        ref_voltage = 5
        
        x = xAxis.read()

        y = yAxis.read()

        print("x :" , round(x[name]/ref_voltage,1), "y : ", round(y[name],4))

        x_perc = int(x[name]*100/ref_voltage)

        y_perc = int(y[name]*100/ref_voltage)

        print("x ( % ):" , x_perc, "y : ", y_perc)
        
        time.sleep(1)
