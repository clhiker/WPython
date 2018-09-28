import cv2

def getTimeDifference():
    e1 = cv2.getTickCount()
    count = 0
    for i in range(10000):
        count += 1
    e2 = cv2.getTickCount()
    return (e2 - e1)/cv2.getTickFrequency()

