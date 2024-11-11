# grayscale_conversion.py
import cv2

# Step 1: Load an image in color
image = cv2.imread('sample.jpg', 1)

# Step 2: Convert the color image to grayscale
# 'cv2.cvtColor()' converts the image to grayscale using the specified color code.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)

# Step 4: Save the grayscale image to disk
cv2.imwrite('grayscale_image.jpg', gray_image)

cv2.destroyAllWindows()
