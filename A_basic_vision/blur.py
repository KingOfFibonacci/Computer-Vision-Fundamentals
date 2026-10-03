import cv2

img = cv2.imread("../Intro_to_images/test.png")
imgBlur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Image", img)
cv2.imshow("Image Blur", imgBlur)
cv2.waitKey(0)