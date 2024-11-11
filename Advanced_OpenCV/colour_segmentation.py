# color_segmentation.py
import cv2
import numpy as np

# Step 1: Load the image
image = cv2.imread('sample.jpg')

# Step 2: Convert the image to HSV color space
# HSV (Hue, Saturation, Value) is better for color-based segmentation
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Step 3: Define the color range for segmentation (e.g., red color)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
# These arrays define the range of red in HSV space

# Step 4: Create a mask based on the color range
mask = cv2.inRange(hsv_image, lower_red, upper_red)
# 'cv2.inRange()' returns a binary mask where the red areas are white (255) and the rest is black (0)

# Step 5: Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Step 6: Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
