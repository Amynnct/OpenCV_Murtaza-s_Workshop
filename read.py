import cv2 as cv

##### read image

# img = cv.imread("Photo/katrina.jpg")
# cv.imshow("Katrina", img)
# cv.waitKey(0)

##### read video
cap = cv.VideoCapture("Video/Kirby.mp4")

while True:
    success, frame = cap.read()
    cv.imshow("Video", frame)
    if cv.waitKey(10) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()

###### read from webcam

# cap = cv.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# while True:
#     success, frame = cap.read()
#     cv.imshow("Video", frame)
#     if cv.waitKey(10) & 0xFF==ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()