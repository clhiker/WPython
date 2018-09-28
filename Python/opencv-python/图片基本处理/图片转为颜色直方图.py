# -*- encoding:utf-8 -*-
import cv2
import numpy
#from matplotlib import pyplot as plt


def readImage():
    # 读取图片 B，G，R，返回一个ndarray类型
    # cv2.IMREAD_COLOR  # 以彩色模式读入 1
    # cv2.IMREAD_GRAYSCALE  # 以灰色模式读入 0
    img = cv2.imread('1.png', cv2.IMREAD_COLOR)
    # 返回多维矩阵，#(384, 512, 3)，
    print(type(img), img.shape, img.size, img.dtype)
    # ravel()展平n维矩阵的所有
    print(img.ravel(), len(img.ravel()))


def cvt():
    '''
    经常用到的颜色转换BGR->Gray 和BGR->HSV
    '''
    # 读取图片 B，G，R，返回一个ndarray类型
    img = cv2.imread('1.jpg')
    # cv2.COLOR_BGR2GRAY;cv2.COLOR_BGR2HSV
    # 彩色图像转灰度图像YUV(Y即为灰度图) Y = 0.299R + 0.587G + 0.114B
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 彩色图像转灰度图像YUV(Y->亮度；U,V->色度)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # numpy.savetxt('1.txt',img1,fmt='%d',delimiter=' ',newline='\r\n')
    # numpy.savetxt('1.txt', img2, fmt='%d', delimiter=' ', newline='\r\n')
    # f = open('1.txt','w')
    # for i in range(img1):
    #     f.writelines(i)
    #     f.write('\n')

    # print(img1)
    # print(img2)

    row = len(img2)
    col = len(img2[0])

    list1 = [[0]*row]*col

    flag = 0
    i = 0
    j = 0
    for item1 in img2:
        for item2 in item1:
            for item3 in item2:
                if (item3 != 255) and (item3 != 0):
                    flag = 1
                else:
                    flag = 0
            if flag == 0:
                list1[i].append(0)
            else:
                list1[i].append(1)
        i+=1

    # f = open('2.txt','w')
    for it in list1:
        for item in it:
            if(item == 0):
                print(" ",end="")
            else:
                print("`",end="")
        print("\n")
    # f.close()


cvt()
