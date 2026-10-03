import cv2

img = cv2.imread("../Intro_to_images/test.png")

# location (x,y) - Font - Scale of font - Color (bgr) - thickness of font
cv2.putText(img, "Hello, from Brandon Welch", (100,200), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)