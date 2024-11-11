# contour_detection.py
import cv2

# Step 1: Load the image and convert to grayscale
image = cv2.imread('sample.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Apply a binary threshold to get a binary image
_, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Step 3: Find contours
# 'cv2.findContours()' returns the contours and the hierarchy
contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 4: Draw bounding boxes around each contour
for contour in contours:
    # Get the bounding box coordinates for the contour
    x, y, w, h = cv2.boundingRect(contour)
    # Draw a rectangle around the contour
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Step 5: Display the image with bounding boxes
cv2.imshow('Contours with Bounding Boxes', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
