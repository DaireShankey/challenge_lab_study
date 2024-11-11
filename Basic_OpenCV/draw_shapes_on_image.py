# draw_shapes.py
import cv2

# Step 1: Load the image
image = cv2.imread('sample.jpg', 1)

# Step 2: Draw a line
# 'cv2.line()' takes start and end points, color, and thickness as arguments.
cv2.line(image, (50, 50), (200, 50), (255, 0, 0), 5)

# Step 3: Draw a rectangle
# 'cv2.rectangle()' takes top-left and bottom-right points, color, and thickness.
cv2.rectangle(image, (50, 100), (200, 200), (0, 255, 0), 3)

# Step 4: Draw a circle
# 'cv2.circle()' takes center, radius, color, and thickness.
cv2.circle(image, (300, 150), 50, (0, 0, 255), -1)  # -1 fills the circle

# Step 5: Display the image with shapes
cv2.imshow('Shapes on Image', image)
cv2.waitKey(0)

# Step 6: Save the image with shapes
cv2.imwrite('shapes_image.jpg', image)

cv2.destroyAllWindows()
