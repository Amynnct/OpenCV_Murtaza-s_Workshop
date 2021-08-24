import cv2 as cv

img = cv.imread("Photo/minimalist_art.jpg")
print(img.shape) #show (height, width)

imgResize = cv.resize(img, (333, 500)) #define width first then height
imgCropped = img[100:500,100:400] #cropped img using array slicing

cv.imshow("Image", img)
cv.imshow("Image Rezise", imgResize)
cv.imshow("Image Cropped", imgCropped)
cv.waitKey(0)

#########################################################
# def rescaleFrame(frame, scale=0.75):    ##works with images, videos, and live videos
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture("Video/Kirby.mp4")

# while True:
#     success, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
    
#     cv.imshow("Video", frame)
#     cv.imshow("Video rescale", frame_resized)

#     if cv.waitKey(10) & 0xFF == ord('q'):
#         break

#######################################################
# def changeRes(width, height): #changing the resolution of a video
#     #only for live video
#     capture.set(3, width) #3 is the id for width
#     capture.set(4, height) #4 references the height

# capture = cv.VideoCapture(0)
# changeRes(200,100)
# while True:
#     success, frame = capture.read()
#     cv.imshow("Video", frame)
#     if cv.waitKey(10) & 0xFF == ord('q'):
#         break