import sys
import csv
import random
import numpy as np
from time import sleep
import RPi.GPIO as GPIO
from threading import Timer, Lock

class logger:
    #start csv thread every time secnds 
    def __init__(self, debug, directory, time):
        
        #set configuration flags
        self.debug = True if debug == "-d" else False
        self.directory = directory
        self.file = None
        self.time = float(time)
        
        #mutex lock
        self.arr = []
        self.arrLock = Lock()
        
        #LED setup
        self.LED_State = True
        self.LED_PIN = 7
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LED_PIN, GPIO.OUT, initial = GPIO.HIGH)
        
        #begin CSV file saver      
        self.save() 
 
    #blink indicator LED
    def toggleLED(self):
        GPIO.output(self.LED_PIN, self.LED_State)
        self.LED_State = not(self.LED_State)
    
    #append array
    def log(self, line):
        
        #append line       
        try:
            self.arrLock.acquire()
            self.arr.append(line)

        finally:
            self.arrLock.release()
            
            #print sensors data
            if self.debug:
                print(line)

    #save CSV
    def save(self):
        self.file = open(self.directory,'a')
        dataWriter = csv.writer(self.file)
        
        #write buffer to CSV        
        try:
            self.arrLock.acquire()
            
            dataWriter.writerow(self.arr)
            
            self.arr.clear()
        
        #close buffer, blink LED
        finally:
            self.arrLock.release()
            self.file.close()

            t = Timer(self.time, self.save)
            t.start()
            
            self.toggleLED()

args = sys.argv[1:]
Logger = logger(*args)

while True:

    #read stdin for sensor data
    for line in sys.stdin:
        Logger.log(line.replace(",",""))
        sys.stdin.flush()
