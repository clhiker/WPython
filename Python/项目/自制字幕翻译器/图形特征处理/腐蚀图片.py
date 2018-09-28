import cv2
import numpy
#腐蚀有风险！！！！！！！！！！！
#腐蚀 前景物体的厚度或大小会减小，
#或者图像中的白色区域会减少。这对于消除小的白噪声是有用的
#kernel = numpy.uint8(numpy.zeros((5,5)))
# for i in range(5):
#     kernel[i,2] = 1
#     kernel[2,i] = 1
kernel = numpy.ones((5,5),numpy.uint8)

image = cv2.imread('D://test/3.jpg',0)
cv2.imshow("3.jpg",image)
eroded = cv2.erode(image,kernel,iterations=1)
cv2.imwrite('D://test/2.jpg',eroded)
cv2.imshow("2.jpg", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()