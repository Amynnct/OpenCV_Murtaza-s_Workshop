import cv2 as cv
import numpy as np

img = cv.imread("Photo/katrina.jpg")
kernel = np.ones((3,3), np.uint8) #(5,5) is the size of the kernel, np.uint8 defines the type of the obj -> Unsigned INTeger of 8 bit

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (5,5), 0)
imgCanny = cv.Canny(img, 150, 100)
imgDialation = cv.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv.erode(imgDialation, kernel, iterations=1)


cv.imshow("Gray Image", imgGray)
cv.imshow("Blur Image", imgBlur)
cv.imshow("Canny Image", imgCanny)
cv.imshow("Dialation Image", imgDialation)
cv.imshow("Erosion Image", imgEroded)

cv.waitKey(0)