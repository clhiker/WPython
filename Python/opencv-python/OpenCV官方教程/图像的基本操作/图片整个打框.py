import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [0,0,255]

img1 = cv2.imread('d://test/test.png')

constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(constant,'gray'),plt.title('constant')
plt.show()