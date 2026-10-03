import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxes = detector.findPosition(img)
    if bboxes:
        center = bboxes['center']
    if not success:
        break
    cv2.imshow("Body Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break