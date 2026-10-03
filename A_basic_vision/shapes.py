import cv2
import cvzone
import numpy as np
from cvzone.Utils import findContours

img = cv2.imread("shapes1.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(imgGray, 50, 150)
imgDilated = cv2.dilate(imgCanny, np.ones( (2, 2), np.uint8), iterations=1)

imgContours, conFound = findContours(img, imgDilated, filter = [3, 4], drawCon = True)

print(conFound[0]['bbox'])

imgStack = cvzone.stackImages([img, imgGray, imgCanny, imgDilated, imgContours], 3, 0.5)

cv2.imshow("Image Stack", imgStack)

cv2.waitKey(0)