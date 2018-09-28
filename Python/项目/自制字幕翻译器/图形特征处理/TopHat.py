import cv2
import numpy

kernel = numpy.ones((5,5),numpy.uint8)

image = cv2.imread("D://test/3.jpg",0)
size = image.shape
width = size[0]
height = size[1]
print(width)
# cv2.namedWindow('3.jpg',0)
# cv2.resizeWindow('3.jpg',int(width),int(height))
cv2.imshow('3.jpg',image)

gradient = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
# cv2.namedWindow('4.jpg',0)
# cv2.resizeWindow('4.jpg',int(width),int(height))
cv2.imshow('4.jpg',gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
