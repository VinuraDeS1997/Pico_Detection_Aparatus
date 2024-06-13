#servo.py
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

class Servo:
    def __init__(self, pin, data_rate):
        self.pin = pin
        self.data_rate = data_rate
        #Setup of Servo
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.data_rate)
        self.pwm.start(0)
    #Sets the angle of servo
    def setAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(duty)


