import cv2
import numpy as np

# Load the image
image = cv2.imread("separatedSaturation.png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to extract the white rectangles
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours of the white rectangles in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract the coordinates of the bounding rectangles for each contour
rectangles = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    rectangles.append((x, y, x + w, y + h))

# Display the rectangles
for rectangle in rectangles:
    cv2.rectangle(image, (rectangle[0], rectangle[1]), (rectangle[2], rectangle[3]), (0, 255, 0), 2)

# Show the image
cv2.imshow("Image", image)
cv2.waitKey(0)

# Print the rectangles list
print(rectangles)
