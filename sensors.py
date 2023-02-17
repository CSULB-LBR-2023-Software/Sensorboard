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

#sensor configurations
alt.pressure_oversampling = 8
alt.temperature_oversampling = 2
alt.sea_level_pressure = 1024.2

#start time
t1 = time.time()

while True:
    
    #concatenate samples
    altitude_sample = alt.altitude
    imu_sample = imu.acceleration    
    data = time.time() - t1, imu_sample[0], imu_sample[1], imu_sample[2], altitude_sample
    
    #stringize and write samples
    string = str(data)[1:-1] + "\n"
    stdout.write(string)
    stdout.flush()

