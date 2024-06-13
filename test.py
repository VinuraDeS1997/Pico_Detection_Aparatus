"""
Script to control the angle of a servo motor with Raspberry Pi.
"""
#test.py
#Control the angle of a Servo Motor with Raspberry Pi.

#initialising components/imports from other files
import RPi.GPIO as GPIO
from time import sleep
from servo import Servo
from PiPico import Pico


GPIO.setmode(GPIO.BOARD)

#Number A is referencing what pins each servo is connected to whereas number Hz.
Servo_A = Servo(11, 50)
Servo_B = Servo(16, 50)
count = 0
numLoops = 2

Serial = Pico('/dev/ttyACM0')

#Determining which servo does which angle.
"""

Main loop to read data and set servo angles accordingly.

"""
while True:
    Pivot_x, Pivot_y = Pico.data(Serial)
    Servo.setAngle(Servo_A, Pivot_x)
    Servo.setAngle(Servo_B, Pivot_y)
    sleep(0.5)
    



    
   



