import cv2

img = cv2.imread("../Intro_to_images/test.png")

# [y1:y2, x1:x2]
imgCrop = img[100:500, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Crop", imgCrop)
cv2.waitKey(0)