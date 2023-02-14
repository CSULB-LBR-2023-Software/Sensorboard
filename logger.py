import sys
import time
while True:
	for line in sys.stdin:
		a = time.time()
		print(line, file=sys.stdout)
