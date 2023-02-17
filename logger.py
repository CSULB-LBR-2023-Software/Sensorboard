import sys
import csv
import random
from threading import Timer, Lock

class logger:
    #start csv thread every time secnds 
    def __init__(self, debug, directory, time):
        self.debug = True if debug == "-d" else False
        self.directory = directory
        self.file = None
        self.time = float(time)
        self.arr = []
        self.arrLock = Lock()
        self._save()

    #append array
    def log(self, line):
        
        #append line       
        try:
            self.arrLock.acquire()
            self.arr.append(line) 

        finally:
            self.arrLock.release()
            
            #printg
            if self.debug:
                print(line)

    #save CSV
    def _save(self):
        self.file = open(self.directory,'a',newline='')
        dataWriter = csv.writer(self.file)
         
        try:
            self.arrLock.acquire()
            dataWriter.writerow(self.arr)
            self.arr.clear()
        
        finally:
            self.arrLock.release()
            self.file.close()

            t = Timer(self.time, self._save)
            t.start()

#define logger parameters
if sys.argv[1] == "-d":
    print("Debug enabled")

Logger = logger(sys.argv[1], sys.argv[2], sys.argv[3])

while True:

    #read stdin for sensor data
    for line in sys.stdin:
        Logger.log(line)
        sys.stdin.flush()	
