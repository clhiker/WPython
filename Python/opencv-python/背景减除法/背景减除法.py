import cv2

def detect_video(video):
    camera = cv2.VideoCapture(video)
    history = 10    # 训练帧数
    bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)  # 背景减除器，设置阴影检测
    bs.setHistory(history)
    frames = 0

    while True:
        res, frame = camera.read()
        if not res:
            break
        fg_mask = bs.apply(frame)   # 获取 foreground mask
        if frames < history:
            frames += 1
            continue

        # 对原始帧进行膨胀去噪
        th = cv2.threshold(fg_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 3)), iterations=2)
        # 获取所有检测框
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            # 获取矩形框边界坐标
            x, y, w, h = cv2.boundingRect(c)
            # 计算矩形框的面积
            area = cv2.contourArea(c)
            if area > 100:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("detection", frame)
        #cv2.imshow("back", dilated)
        if cv2.waitKey(110) & 0xff == 27:
            break
    camera.release()

if __name__ == '__main__':
    video = 'D:\\3.mp4'
    detect_video(video)

#
# import numpy as np
# import cv2
#
# #BackgroundSubtractorMOG2
# #opencv自带的一个视频
# cap = cv2.VideoCapture('D:\\1.mp4')
# #创建一个3*3的椭圆核
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# #创建BackgroundSubtractorMOG2
# fgbg = cv2.createBackgroundSubtractorMOG2()
#
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     #形态学开运算去噪点
#     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
#     #寻找视频中的轮廓
#     im, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     for c in contours:
#         #计算各轮廓的周长
#         perimeter = cv2.arcLength(c,True)
#         if perimeter > 188:
#             #找到一个直矩形（不会旋转）
#             x,y,w,h = cv2.boundingRect(c)
#             #画出这个矩形
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#
#     cv2.imshow('frame',frame)
#     cv2.imshow('fgmask', fgmask)
#     k = cv2.waitKey(130) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()