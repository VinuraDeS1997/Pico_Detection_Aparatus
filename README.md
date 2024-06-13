# Pico_Detection_Aparatus
All code and necessary functions to make Raspberry Pi detect a Raspberry Pi Pico's Position.

Specific Devices being used:
Raspberry Pi Pico W - Copyright Raspberry Pi 2022
Raspberry Pi: Raspberry Pi 3 Model B V1.2 
- Copyright Raspberry Pi 2015

2x Servos: SG90 Micro Servo 9G


COMConfig.py defines what COM port the Pi Pico is connected to.
newmpu.py defines the parameters for the Pi Pico.
servo.py defines the parameters for the servo and sets the max angle for them.
PiPico.py defines the parameters for reading serial from the Pi Pico coordinates in whole numbers.
test.py is the file that controls the angles that each servo is reading and moves them where the Pi Pico is being manually moved to.
