[PiPico.py]
import serial
class Pico:
    def __init__(self, port):
        self.port = serial.Serial(port)
        
    def data(self):
        data = self.port.readline().decode('utf-8').strip()
        x, y = data.split()
        x = int(x.split('.')[0])
        y = int(y.split('.')[0])
        if y > 0 & y < 135:
            return x, y
        
        
        
