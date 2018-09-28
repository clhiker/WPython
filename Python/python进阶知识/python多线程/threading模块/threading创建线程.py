import threading
import time

exit_flag = 0

class MyThread(threading.Thread):
    #只有这俩个方法可以被覆盖
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting ' + self.name)
        printName(self.name, self.counter, 5)
        print('Exiting ' + self.name)

def printName(thread_name, delay, counter):
    while counter:
        if  exit_flag:
            (threading.Thread).exit()
        time.sleep(delay)
        print(thread_name, time.time())
        counter -= 1

thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

thread1.start()
thread2.start()