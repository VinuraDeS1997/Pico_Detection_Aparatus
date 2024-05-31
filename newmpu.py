# Example code for (GY-521) MPU6050 Accelerometer/Gyro Module
# Write in MicroPython by Warayut Poomiwatracanont JAN 2023

from MPU6050 import MPU6050
import time
from machine import Pin
from time import sleep_ms


VCC = Pin(13, Pin.OUT)
GND = Pin(12, Pin.OUT)
VCC.value(1)
GND.value(0)
time.sleep(.5)


mpu = MPU6050()


while True:
        # Accelerometer Data
    accel = mpu.read_accel_data() # read the accelerometer [ms^-2]
    aX = accel["x"]
    aY = accel["y"]
    aZ = accel["z"]
    #print(aZ)
    #print((aY+8) * (135/15))
    print((aX+10) * (135/20), (aY+8) * (135/15))
    
        # Gyroscope Data
    gyro = mpu.read_gyro_data()   # read the gyro [deg/s]
    gX = gyro["x"]
    gY = gyro["y"]
    gZ = gyro["z"]
   
#     print("x:" + str(gX) + " y:" + str(gY) + " z:" + str(gZ))


    time.sleep(.5)