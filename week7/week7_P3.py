#run with sudo
import os
import RPi.GPIO as GPIO
from time import time,sleep
import sys
import tm1637


sys.path.append('./base/')
import inputKey

rpm_count = 0
lastcount = 0
lasttime = time()
dir = "cw"
duty = 0

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


def printUsage():
	print("Motor Speed Control System")
	print("\t Press 'w' to increase & Press 's' to decrease speed ")
	print("\t Press 'd' for clockwise & Press 'a' for counter clockwise rotation ")


mykey = inputKey.inputKey(1)
display = tm1637.TM1637(clk=21, dio=20)

GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=1)
pi_pwm = GPIO.PWM(ENB,500)		#create PWM instance with frequency

pi_pwm.start(0)

sleep(1)

pi_pwm.ChangeDutyCycle(duty)

try:
	while True:
		rpm = calc_rpm()
		print(dir,duty,rpm)
		print("SPeed : ",rpm, " rpm ")
		display.number(rpm)
		printUsage()
		key = mykey.get()

		if key == "w": 
			if duty<100: duty = duty+1
		elif key == "s": #keys.DOWN:
			if duty>19: duty = duty-1
		elif key == "d": #keys.RIGHT:
			GPIO.output(IN3,GPIO.HIGH)
			GPIO.output(IN4,GPIO.LOW)
			dir = "cw "
		elif key == "a": #keys.LEFT:
			GPIO.output(IN3,GPIO.LOW)
			GPIO.output(IN4,GPIO.HIGH)
			dir = "ccw "
		elif key == 'e':
			GPIO.cleanup() 
			exit() 
		pi_pwm.ChangeDutyCycle(duty)
		sleep(0.2)
except KeyboardInterrupt:
       	GPIO.cleanup()
