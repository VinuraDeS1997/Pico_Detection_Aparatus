#test.py
#Control the angle of a 
#Servo Motor with Raspberry Pi

import RPi.GPIO as GPIO
from time import sleep
from servo import Servo
from PiPico import Pico
# from COMConfig import data

GPIO.setmode(GPIO.BOARD)

Servo_A = Servo(11, 50)
Servo_B = Servo(16, 50)
count = 0
numLoops = 2

Serial = Pico('/dev/ttyACM0')

while True:
    Pivot_x, Pivot_y = Pico.data(Serial)
    Servo.setAngle(Servo_A, Pivot_x)
    Servo.setAngle(Servo_B, Pivot_y)
    sleep(0.5)
    
    
#22 max, 6 min, 14, mid

# while count < numLoops:
#     print("set to 0-deg")
#     Servo.setAngle(Servo_A, 0)
#     sleep(1)

        
#     print("set to 90-deg")
#     Servo.setAngle(Servo_A, 90)
#     sleep(1)

#     print("set to 135-deg")
#     Servo.setAngle(Servo_A, 135)
#     sleep(1)
#     print("set to 0-deg")
#     Servo.setAngle(Servo_B, 0)
#     sleep(1)

        
#     print("set to 90-deg")
#     Servo.setAngle(Servo_B, 90)
#     sleep(1)

#     print("set to 135-deg")
#     Servo.setAngle(Servo_B, 135)
#     sleep(1)
    
#     count=count+1


    
   



