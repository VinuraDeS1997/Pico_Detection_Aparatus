"""
Script to control the angle of a servo motor with Raspberry Pi.
"""

# Initialising imports
import RPi.GPIO as GPIO
from time import sleep
from servo import Servo
from PiPico import Pico

GPIO.setmode(GPIO.BOARD)

# Initialize servos
servo_a = Servo(11, 50)
servo_b = Servo(16, 50)
count = 0
num_loops = 2

serial = Pico('/dev/ttyACM0')

while True:
    """
    Main loop to read data and set servo angles accordingly.
    """
    # Get data from Pico
    pivot_x, pivot_y = Pico.data(serial)
    
    # Set servo angles
    servo_a.set_angle(pivot_x)
    servo_b.set_angle(pivot_y)
    
    sleep(0.5)  # Wait before reading the next set of data
    



    
   



