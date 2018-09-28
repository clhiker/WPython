import cv2
import numpy

kernel = numpy.ones((5,5),numpy.uint8)

image = cv2.imread("D://test/3.jpg",0)
cv2.imshow('3.jpg',image)

image4 = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow('4.jpg',image4)
cv2.waitKey(0)
cv2.destroyAllWindows()
