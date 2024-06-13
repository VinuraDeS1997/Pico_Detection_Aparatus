"""
Module for configuring and reading data from a serial port.
"""

import serial

# Configure the serial port
ser = serial.Serial('/dev/ttyACM0')  # Replace 'COM3' with the appropriate port

while True:
    """
    Main loop to read data from the serial port and print it.
    """
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()
    print(data)  # Print the received data

    if data:
        # Split the data into x and y values
        x, y = data.split(',')
        x = int(x.split('.')[0])  # Convert x value to integer
        y = int(y.split('.')[0])  # Convert y value to integer

        # Print the received values
        print(f"Received: x={x}, y={y}")
