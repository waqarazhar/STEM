#run with sudo
import os
import RPi.GPIO as GPIO
from time import time,sleep
import sys

sys.path.append('./base/')
import inputKey
import sensorSR04


rpm_count = 0
lastcount = 0
lasttime = time()
dir = "cw"
duty = 20

ENB = 23
IN3 = 24
IN4 = 25
Enc_A = 17  
Enc_B = 27  



GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Enc_A, GPIO.IN)
GPIO.setup(Enc_B, GPIO.IN)
GPIO.setup(ENB,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.output(IN3,GPIO.HIGH)
GPIO.output(IN4,GPIO.LOW)


def rotation_decode(Enc_A):
	Switch_B = GPIO.input(Enc_B)
	global rpm_count
	global dir
	rpm_count += 1
	if rpm_count == 961: rpm_count = 1

def calc_rpm():
	global lastcount
	global lasttime
	count=rpm_count
	now = time()
	dcount = count - lastcount
	lastcount = count
	if dcount < 0: dcount += 960
	gap = now-lasttime
	lasttime = now
	pps = dcount/gap
	RPM = pps*60/960
	return round(RPM)

def pid(input, ref):
	
	error = input - ref

	return error


def printUsage():
	print("Motor Speed Control System")
	print("\t Press 'w' to increase the rpm & Press 's' to decrease rpm ")


if __name__ == '__main__':

	ref_distance = 50
	min_duty = 25
	max_duty = 60
	
	distanceSensor = sensorSR04.sensorSR04(trigger_pin=26, echo_pin=16)

	mykey = inputKey.inputKey(1)

	GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=1)
	pi_pwm = GPIO.PWM(ENB, 500)		#create PWM instance with frequency

	pi_pwm.start(min_duty)

	sleep(1)

	pi_pwm.ChangeDutyCycle(min_duty)

	try:
		while True:
			
			distance = distanceSensor.measureDistance(1)

			print("Distance : ",distance, " rpm ")
			print("Refernce Distance : ",ref_distance, " rpm ")

			rpm = calc_rpm()
			print("Speed : ",rpm, " rpm ")
			
			duty = duty + pid(distance, ref_distance)
			print("duty : ", duty)

			if duty > max_duty:
				duty = max_duty
			elif duty < min_duty:
				duty = min_duty
			
			print("duty : ", duty)
						
			pi_pwm.ChangeDutyCycle(duty)

			sleep(0.2)

	except KeyboardInterrupt:
			GPIO.cleanup()
