
import threading, time

def Seeker(cond, name):
    time.sleep(2)
    cond.acquire()
    print(name + ' 我已经把眼睛蒙上了')
    cond.notify()
    cond.wait()
    for i in range(3):
        print(name + "is finding")
        time.sleep(2)
    cond.notify()
    cond.release()
    print(name + '我赢了')

def Hider(cond, name):
    cond.acquire()
    cond.wait()
    for i in range(2):
        print(name + 'is hiding')
        time.sleep(3)
    print(name + '已经藏好了')
    cond.notify()
    cond.wait()
    cond.release()
    print(name + '被你找到了')

if __name__ == '__main__':
    cond = threading.Condition()        #条件对象
    seeker = threading.Thread(target=Seeker,args=(cond,'seeker'))
    hider = threading.Thread(target=Hider,args=(cond,'hider'))
    seeker.start()
    hider.start()
