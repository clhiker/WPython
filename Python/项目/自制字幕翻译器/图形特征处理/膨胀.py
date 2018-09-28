import cv2
import numpy

kernel = numpy.ones((5,5),numpy.uint8)

image = cv2.imread("D://test/3.jpg",0)
cv2.imshow('3.jpg',image)

image4 = cv2.dilate(image,kernel,iterations=1)#先膨胀
eroded = cv2.erode(image,kernel,iterations=1)#再腐蚀
cv2.imshow('4.jpg',image4)
cv2.imshow('5.jpg',eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
