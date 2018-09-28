import cv2

cap = cv2.VideoCapture("D://test/1.mp4")
if cap.isOpened() == False:
    print("error open!\n")
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#
# for i in range(count):
#     ret, frame = cap.read()
#     cv2.imwrite("D://test/" + str(i) + ".jpg", frame)
#     cv2.waitKey(1)
i = 1
while(1):
    ret, frame = cap.read()
    cv2.imshow('video',frame)
    if(i == 186):
        cv2.imwrite("D://test/1.jpg",frame)

    if(i<1000):
        cv2.waitKey(25)
    else:
        cv2.waitKey(1000)
    i += 1

cap.release()


