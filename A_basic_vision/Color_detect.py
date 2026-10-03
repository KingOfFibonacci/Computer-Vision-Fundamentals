import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)

myColorFinder = ColorFinder(trackBar=False)

hsvVal = {'hmin': 0, 'smin': 102, 'vmin': 126, 'hmax': 56, 'smax': 255, 'vmax': 255}


while True:
    success, img = cap.read()
    if not success:
        break

    imgColor, mask = myColorFinder.update(img, hsvVal)

    imgStack = cvzone.stackImages([img, imgColor, mask], 3, 0.5)

    cv2.imshow("Color Detection", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break