import cv2

def resizeImage(origin_image, number):
    new_size = (origin_image.shape[0]//number, origin_image.shape[1]//number)
    new_image = cv2.resize(origin_image,new_size,interpolation=cv2.INTER_AREA)
    cv2.imshow('new_image',new_image)

    # 保存
    cv2.imwrite('small.png',new_image)

def main():
    origin_image = cv2.imread('origin.png')
    cv2.imshow('origin.png',origin_image)
    resizeImage(origin_image, 10)
    cv2.waitKey(0)

main()