"""
Module for interacting with a Raspberry Pi Pico via a serial connection.
"""

import serial


class Pico:
    """
    A class to represent a Raspberry Pi Pico device.

    Attributes:
        port (serial.Serial): The serial port connection to the Pico.
    """

    def __init__(self, port):
        """
        Initializes an instance of Pico, setting up a serial connection to the specified port.

        Args:
            port (str): The serial port to which the Pico is connected.
        """
        self.port = serial.Serial(port)

    def data(self):
        """
        Reads data from the Pico and returns the x and y coordinates as whole numbers.

        Returns:
            tuple: A tuple containing the x and y coordinates as integers, if y is between 0 and 135.
            None: If y is not between 0 and 135.
        """
        data = self.port.readline().decode('utf-8').strip()  # Read and decode data from serial port
        x, y = data.split()  # Split data into x and y
        x = int(x.split('.')[0])  # Convert x to integer
        y = int(y.split('.')[0])  # Convert y to integer

        # Check if 'y' is within the valid range
        if 0 < y < 135:
            return x, y
