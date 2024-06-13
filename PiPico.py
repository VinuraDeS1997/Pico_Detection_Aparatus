"""
Module for interacting with a Raspberry Pi Pico via a serial connection.
"""
#PiPico.py
#Import functions from what file you're trying to read the data for the pyserial from the serial port.
import serial
#Define class.
class Pico:
"""
    A class to represent a Raspberry Pi Pico device.

    Attributes:
        port (serial.Serial): The serial port connection to the Pico.
"""

    #initialize instance of Pico set up a serial connection to the specified port.
    def __init__(self, port):

        self.port = serial.Serial(port)

     #Defines coordinates of X and Y as whole numbers.
    def data(self):
"""
        Reads data from the Pico and returns the x and y coordinates as whole numbers.

        Returns:
            tuple: A tuple containing the x and y coordinates as integers, if y is between 0 and 135.
            None: If y is not between 0 and 135.
"""

        data = self.port.readline().decode('utf-8').strip() #data function is defined where it strips the self port readline in utf-8 format.
        x, y = data.split()
        x = int(x.split('.')[0])
        y = int(y.split('.')[0])
        #Check if 'y' is between 0 and 135.
        if y > 0 and y < 135:
            return x, y
        
        
        
