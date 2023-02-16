import time
import board
import adafruit_bno055
import adafruit_bmp3xx
from random import randint 
from sys import stdout

#instantiate sensors
i2c = board.I2C()
imu = adafruit_bno055.BNO055_I2C(i2c)
alt = adafruit_bmp3xx.BMP3XX_I2C(i2c)
alt.pressure_oversampling = 8
alt.temperature_oversampling = 2

#start time
t1 = time.time()

while True:
    
    #concatenate samples
    sample = imu.acceleration    
    a = time.time() - t1, sample[0], sample[1], sample[2], alt.altitude
    
    #stringize and write samples
    string = str(a) + "\n"
    stdout.write(string)
    stdout.flush()

