import sys
import csv
import random
from threading import Timer
 
class logger:
	def __init__(self, directory, time):
		self.directory = directory
		self.file = None
		self.arr = []
		self.time = time
		self._begin()

	def log(self, line):
		self.arr.append(line)

	def _begin(self):
		self.file = open(self.directory, 'a', newline='')
		dataWriter = csv.writer(self.file)
		dataWriter.writerow(self.arr)
		self.arr.clear()
		self.file.close()
		
		t = Timer(self.time, self._begin)
		t.start()


Logger = logger('../data/rawData.csv', 1)

while True:

	for line in sys.stdin:
		Logger.log(int(line))
		sys.stdin.flush()	
