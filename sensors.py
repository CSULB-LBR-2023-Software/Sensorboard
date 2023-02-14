from time import sleep
from random import randint 
from sys import stdout

while True:
	string = str(randint(0, 10)) + "\n"
	stdout.write(string)
	stdout.flush()
	sleep(0.1)
