from time import sleep
import sys

while True:
	print("Test sensor data", file=sys.stdout)
	sys.stdout.flush()
	sleep(1)

