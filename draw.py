import cv2 as cv
import numpy as np

#create a blank image to draw on or draw on the existing img
blank = np.zeros((500,500,3), dtype="uint8")
# img = cv.imread("Photo/katrina.jpg")
# cv.imshow("Blank", blank)

# cv.imshow("Katrina", img)

#1. Paint the image a certain colour
blank[:] = 0,255,0 #green
# cv.imshow("Green", blank)

blank[200:300, 300:400] = 0,0,255 #red
# cv.imshow("Red", blank)

#2. Draw a Rectangle 
#.rectangle(img-to-draw-on, point1, point2, colour)
cv.rectangle(blank, (0,0), (250, 250), (255,0,0), thickness=cv.FILLED)
#specific thinkness using cv.FILLED or thickness=-1 for the same result
#cv.imshow("Rectangle", blank)

#3. Draw a circle
#.circle(img-to-draw, center, radius, colour)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (255,255,255), thickness=-1)
# cv.imshow("Circle", blank)

#4. Draw a line
cv.line(blank, (0,0), (200,300), (0,0,0), thickness=3)
# cv.imshow("Line", blank)

#5. Write text
#putText(img, text, origin, font, fontScale, color, thickness)
cv.putText(blank, "Hello", (300,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), thickness=1)
cv.imshow("Text", blank)
cv.waitKey(0)
