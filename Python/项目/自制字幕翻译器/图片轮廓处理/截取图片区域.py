# import os
# import cv2
# for i in range(1,201):
#     if i==169 or i==189:
#         i = i+1
#     path = 'D://test/1.jpg'
#     image = cv2.imread(path)            //从指定路径读取图像
#     cropImg = image[600:1200,750:1500] //获取感兴趣区域
#     cv2.imwrite("C:\\Users\\Desktop\\qwe\\"+str(i)+".bmp",cropImg) //保存到指定目录
#    # print pth
# #cropImg = image[100:200, 100:200]
# #cv2.imwrite("a.bmp",cropImg)
import cv2

image = cv2.imread('D://test/1.jpg',0)
size = image.shape
print(image.shape)
print(size[0], end="\t")
print(size[1],end="\n")

cv2.imshow('1.jpg', image)  #int(size[1]):int(size[1])
crop_img =image[350:size[0], 0:int(size[1])]
cv2.imshow('2.jpg', crop_img)
cv2.imwrite('D://test/rect.jpg',crop_img)
cv2.waitKey(0)