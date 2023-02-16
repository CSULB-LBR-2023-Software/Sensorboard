import sys
import csv
import random
from threading import Timer
 
class logger:
	#start csv thread every time secnds 
	def __init__(self, directory, time):
		self.directory = directory
		self.file = None
		self.arr = []
		self.time = time
		self._save()
	
	#append array
	def log(self, line):
		self.arr.append(line)
	
	#internal logger
	def _save(self):
		self.file = open(self.directory, 'a',newline='')
		dataWriter = csv.writer(self.file)
		dataWriter.writerow(self.arr)
		self.arr.clear()
		self.file.close()
		
		t = Timer(self.time, self._save)
		t.start()

#create logger every 5 second, with csv in data directory
Logger = logger('../data/rawData.csv', 5)

while True:
	
	#read stdin for sensor data
	for line in sys.stdin:
		Logger.log(line)
		sys.stdin.flush()	
