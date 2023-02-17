import sys
import csv
import random
from threading import Timer, Lock

class logger:
    #start csv thread every time secnds 
    def __init__(self, directory, time):
        self.directory = directory
        self.file = None
        self.arr = []
        self.arrLock = Lock()
        self.time = time
        self._save()

    #append array
    def log(self, line):
        try:
            self.arrLock.acquire()
  
            #print("Log has lock")
            self.arr.append(line)

        finally:
            self.arrLock.release()

    #internal logger
    def _save(self):
        self.file = open(self.directory,'a',newline='')
        dataWriter = csv.writer(self.file)
            
        try:
            self.arrLock.acquire()
            #print("Save has lock")
            dataWriter.writerow(self.arr)
            self.arr.clear()
        
        finally:
            self.arrLock.release()
            self.file.close()

            t = Timer(self.time, self._save)
            t.start()

#create logger every 1 second, with csv in data directory
Logger = logger('../data/rawData.csv', 1)

while True:

    #read stdin for sensor data
    for line in sys.stdin:
        Logger.log(line)
        sys.stdin.flush()	
