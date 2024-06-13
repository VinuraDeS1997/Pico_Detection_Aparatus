"""
Module for controlling a servo motor using Raspberry Pi GPIO.
"""
#servo.py
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

#Define class
class Servo:
"""
    A class to represent a servo motor.
    
    Attributes
    ----------
    pin : int
        The GPIO pin number where the servo is connected.
    data_rate : int
        The data rate for PWM signal.

    Methods
    -------
    set_angle(angle)
        Sets the angle of the servo motor.
"""
    def __init__(self, pin, data_rate):
"""
        Constructs all the necessary attributes for the servo object.

        Parameters
        ----------
        pin : int
            The GPIO pin number where the servo is connected.
        data_rate : int
            The data rate for PWM signal.
"""
        self.pin = pin
        self.data_rate = data_rate
        #Setup of Servo
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.data_rate)
        self.pwm.start(0)
        
    #Sets the angle of servo
    def setAngle(self, angle):
"""
        Sets the angle of the servo motor.

        Parameters
        ----------
        angle : float
            The angle to set the servo to.
"""
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(duty)


