import os
from getkey import getkey, keys #pip install getkey for keyboard arrows
import RPi.GPIO as GPIO
from time import sleep
import tm1637


ENB = 23
IN3 = 24
IN4 = 25				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system
GPIO.setup(ENB,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.output(IN3,GPIO.HIGH)
GPIO.output(IN4,GPIO.LOW)
dir = "cw"
pi_pwm = GPIO.PWM(ENB,500)		#create PWM instance with frequency
pi_pwm.start(0)
duty = 19				#start PWM of required Duty Cycle 

display = tm1637.TM1637(clk=21, dio=20)

while True:
	
	key = getkey()
	os.system('clear')

	if key == keys.UP:
		
		if duty<100 and duty >18: 
			duty = duty + 1
		
		pi_pwm.ChangeDutyCycle(duty)
		print(dir,duty)
		display.number(duty)
	
	elif key == keys.DOWN:
		
		if duty>19:
			duty = duty-1
		
		
		pi_pwm.ChangeDutyCycle(duty)
		print(dir,duty)
		display.number(duty)

	elif key == keys.RIGHT:
		GPIO.output(IN3,GPIO.HIGH)
		GPIO.output(IN4,GPIO.LOW)
		dir = "cw "
		print(dir,duty)
		display.number(duty)
	
	elif key == keys.LEFT:
		GPIO.output(IN3,GPIO.LOW)
		GPIO.output(IN4,GPIO.HIGH)
		dir = "ccw "
		print(dir,duty)
		display.number(duty)
	
	elif key == 'E':
		GPIO.cleanup() 
		exit() 
	sleep(0.05)