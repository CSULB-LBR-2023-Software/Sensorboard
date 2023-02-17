# SuperFastPython.com
# example of a mutual exclusion (mutex) lock
from time import sleep
from random import random
from threading import Thread
from threading import Lock
 
# work function
def task(lock, value):
    # acquire the lock
    with lock:
        print(f'>thread got the lock, sleeping for {value}')
        sleep(value)
 
# create a shared lock
lock = Lock()
# start a few threads that attempt to execute the same critical section
while True:    
# start a thread
    Thread(target=task, args=(lock, random())).start()
# wait for all threads to finish...
