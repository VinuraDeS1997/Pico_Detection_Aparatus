[COMConfig]
# Windows PC (Python)
import serial

# Configure the serial port
ser = serial.Serial('/dev/ttyACM0')  # Replace 'COM3' with the appropriate port

while True:
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()
    print(data)    # Check if data was received
    
    
    if data:
        # Split the data into x and y values
        x, y = data.split(',')
        x = int(x.split('.')[0])
        y = int(y.split('.')[0])

        # Print the received values
        print(f"Received: x={x}, y={y}")
