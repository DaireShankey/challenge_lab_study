# edge_detection.py
import cv2

# Step 1: Load the image in grayscale
image = cv2.imread('sample.jpg', 0)

# Step 2: Apply Canny edge detection
# 'cv2.Canny()' detects edges with specified threshold values.
edges = cv2.Canny(image, 100, 200)

# Step 3: Display the edge-detected image
cv2.imshow('Edges', edges)
cv2.waitKey(0)

# Step 4: Save the edge-detected image
cv2.imwrite('edges_image.jpg', edges)

cv2.destroyAllWindows()
