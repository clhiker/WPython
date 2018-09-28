import cv2
from PIL import Image
import configparser
import os


old_folder = input('请输入原始文件夹')
new_folder = input('请输入新文件夹')
file_list = os.listdir(old_folder)

count = 0
for file in file_list:
    old_filename = old_folder + '\\' + file
    new_filename = new_folder + '\\' + str(count) + ".png"
    positive_picture = cv2.imread(old_filename)
    negative_picture = positive_picture.copy()
    # 取反颜色
    for i in range(0, positive_picture.shape[0]):
        for j in range(0, positive_picture.shape[1]):
            negative_picture[i, j] = 255 - positive_picture[i, j]

    cv2.imwrite(new_filename,negative_picture)
    count += 1
