import time
import threading

balance = 0
lock = threading.Lock()

def changeIter(n):
    global balance
    balance = balance + n
    balance = balance - n

def runThread(n):
    for i in range(1000000):
        #加锁
        lock.acquire()
        try :
            #使用
            changeIter(n)
        finally:
            #解锁
            lock.release()

t1 = threading.Thread(target=runThread, args=(5,))
t2 = threading.Thread(target=runThread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)