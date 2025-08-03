import RPi.GPIO as GPIO
import time

class sensorSR04(object):
    
    """docstring for sensorSR04"""
    def __init__(self, trigger_pin, echo_pin):
        super(sensorSR04, self).__init__()
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.soundSpeed = 17150

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)   
        

    def singleMeasurement(self, verbose= False):

        if verbose == True:
            print("Starting Distance Measurement")
        GPIO.output(self.trigger_pin, False)
        time.sleep(2)
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        while GPIO.input(self.echo_pin) == 0:
            pulse_start= time.time()

        while GPIO.input(self.echo_pin)== 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 4)

        if verbose == True:
            print("Distance : ", distance)

        return distance

        
    def measureDistance(self, readingCount, verbose = False):

        avgDistance = 0.00

        for i in range(0, readingCount):
            avgDistance += self.singleMeasurement(verbose)


        avgDistance /=readingCount

        if verbose == True:
            print("Avergae Distance : ", avgDistance)

        return avgDistance


if __name__ == '__main__':
    
    mysensor = sensorSR04(trigger_pin=26, echo_pin=16)

    mysensor.measureDistance(10, verbose= True)


