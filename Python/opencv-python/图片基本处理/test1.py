import cv2
import numpy

img = cv2.imread('white.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


row = len(img2)
col = len(img2[0])
print(row,col)
list1 = [[0 for i in range(col)] for j in range(row)]
flag = 0
i = 0
j = 0
for item1 in img2:                  # 图片行
    for item2 in item1:             # 图片列
        if item2[2] < 10:
            list1[i][j] = 0
        else:
            list1[i][j] = 1
        j += 1
    j = 0
    i += 1



print(len(list1))
print(len(list1[0]))
for it in list1:
    for item in it:
        if (item == 0):
            print("+", end="")
        else:
            print(" ", end="")
    print("\n")