"""
Module for controlling a servo motor using Raspberry Pi GPIO.
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


class Servo:
    """
    A class to represent a servo motor.

    Attributes:
        pin (int): The GPIO pin number where the servo is connected.
        data_rate (int): The data rate for PWM signal.
    """

    def __init__(self, pin, data_rate):
        """
        Constructs all the necessary attributes for the servo object.

        Args:
            pin (int): The GPIO pin number where the servo is connected.
            data_rate (int): The data rate for PWM signal.
        """
        self.pin = pin
        self.data_rate = data_rate
        # Setup of Servo
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.data_rate)
        self.pwm.start(0)

    def set_angle(self, angle):
        """
        Sets the angle of the servo motor.

        Args:
            angle (float): The angle to set the servo to.
        """
        duty = angle / 18 + 2  # Convert angle to duty cycle
        GPIO.output(self.pin, True)  # Enable PWM signal
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)  # Wait for servo to move
        GPIO.output(self.pin, False)  # Disable PWM signal
        self.pwm.ChangeDutyCycle(duty)  # Keep the duty cycle constant


