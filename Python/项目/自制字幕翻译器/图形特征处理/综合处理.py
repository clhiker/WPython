import cv2
import numpy

kernel = numpy.ones((5,5),numpy.uint8)

image = cv2.imread("D://test/3.jpg",0)
size = image.shape
width = size[0]
height = size[1]
print(width)
cv2.imshow('3.jpg',image)

open = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)                #打开
close = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)              #关闭
gradient = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)        #形态渐变
top_head = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)          #top head
black_head = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)      #black head
cv2.imshow('4.jpg',black_head)

cv2.waitKey(0)
cv2.destroyAllWindows()
