import cv2

image = cv2.imread("D://test/1.jpg",0)
size = image.shape
print(size)
cv2.imshow("1.jpg",image)
font = cv2.FONT_HERSHEY_SIMPLEX
image2 = cv2.putText(image,
                     'OpenCv',
                     (20,380),        #位置
                     font,
                     0.7,           #字号
                     (255,255,255), #颜色
                     2,             #粗细
                     cv2.LINE_AA
                     )
cv2.imshow("3.jpg",image2)
cv2.imwrite("D://test/3.jpg",image2)



cv2.waitKey(0)
cv2.destroyAllWindows()