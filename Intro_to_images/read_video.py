import cv2

cap = cv2.VideoCapture("test_video.mp4")

while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Video", img)
    cv2.waitKey(1)