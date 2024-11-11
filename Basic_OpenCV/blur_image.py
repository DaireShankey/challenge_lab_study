# blur_image.py
import cv2

# Step 1: Load the image
image = cv2.imread('sample.jpg', 1)

# Step 2: Apply Gaussian blur
# 'cv2.GaussianBlur()' applies Gaussian blur with specified kernel size.
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Step 3: Display the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)

# Step 4: Save the blurred image
cv2.imwrite('blurred_image.jpg', blurred_image)

cv2.destroyAllWindows()
