import _thread
import time

def printTime(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(thread_name, time.ctime(time.time()))

#创建线程
try:
    _thread.start_new_thread(printTime, ('thread 1',2,))
    _thread.start_new_thread(printTime, ('thread 2',4,))
except:
    print('error : unable to create thread')

while True:
    pass