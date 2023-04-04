import cv2
import numpy as np

#Loading image
image = cv2.imread("separatedSaturation.png")

#Greyscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Thresholding
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Exctracting coordinates
rectangles = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    rectangles.append((x, y, x + w, y + h))

#Displaying results
for rectangle in rectangles:
    cv2.rectangle(image, (rectangle[0], rectangle[1]), (rectangle[2], rectangle[3]), (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)

#Printing the final list of coordinates
print(rectangles)
