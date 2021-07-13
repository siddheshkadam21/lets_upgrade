import cv2
import numpy as np

capture=cv2.VideoCapture(0)

while capture.isOpened():
    scuess, frame =capture.read()
    if scuess:
        gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blue_frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        cv2.imshow("blue_frame",blue_frame)
        cv2.imshow("Gray Frame",gray_frame)
        cv2.imshow("Frame",frame)
        k= cv2.waitKey(0)
        if k & 0xff ==ord("q"):
            break
        else:
            print("Click q to close buddy")
            break
capture.release()
cv2.destroyAllWindows()

