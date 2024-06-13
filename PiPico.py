[PiPico.py]
#Import functions from what file you're trying to read the data for the pyserial from the serial port
import serial
#Define class
class Pico:
    #initialize instance of Pico set up a serial connection to the specified port
    def __init__(self, port):
        self.port = serial.Serial(port)
     #Defines coordinates of X and Y as whole numbers
    def data(self):
        data = self.port.readline().decode('utf-8').strip()
        x, y = data.split()
        x = int(x.split('.')[0])
        y = int(y.split('.')[0])
        #Check if 'y' is between 0 and 135
        if y > 0 and y < 135:
            return x, y
        
        
        
