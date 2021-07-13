import cv2

capture = cv2.VideoCapture(0)
image =cv2.imread('images.jpg')
image2 = cv2.imread('image2.png')
image3 = cv2.imread('download.jpg')
image4 = cv2.imread('Universe2020_Wallpaper_Desktop_Main.png')
image5 = cv2. imread('Universe2020_Wallpaper_Desktop_University.png')
image6 = cv2. imread('maxresdefault.jpg')
while True:
    flag, frame = capture.read()
    if not flag:
        print("Could not process the webcam")
        break
    image=cv2.resize(image,(frame.shape[1],frame.shape[0]))
    image2 = cv2.resize(image2, (frame.shape[1], frame.shape[0]))
    image3 = cv2.resize(image3, (frame.shape[1], frame.shape[0]))
    image4 = cv2.resize(image4, (frame.shape[1], frame.shape[0]))
    image5 = cv2.resize(image5, (frame.shape[1], frame.shape[0]))
    image6 = cv2.resize(image6, (frame.shape[1], frame.shape[0]))
    blended_frame1 = cv2.addWeighted(frame,0.8,image,0.2,gamma=0.1)
    blended_frame2 = cv2.addWeighted(frame, 0.8, image2, 0.2, gamma=0.1)
    blended_frame3 = cv2.addWeighted(frame, 0.8, image3, 0.4, gamma=0.2)
    blended_frame4 = cv2.addWeighted(frame, 0.8, image4, 0.5, gamma=0.3)
    blended_frame5 = cv2.addWeighted(frame, 0.8, image5, 0.6, gamma=0.4)
    blended_frame6 = cv2.addWeighted(frame, 0.8, image6, 0.6, gamma=0.4)
    cv2.imshow("Blended Frame1",blended_frame1)
    cv2.imshow("Blended Frame2", blended_frame2)
    cv2.imshow("Blended Frame3", blended_frame3)
    cv2.imshow("Blended Frame4", blended_frame4)
    cv2.imshow("Blended Frame5", blended_frame5)
    cv2.imshow("Blended Frame6", blended_frame6)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()