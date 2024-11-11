# resize_crop.py
import cv2

# Step 1: Load the image
image = cv2.imread('sample.jpg', 1)

# Step 2: Resize the image
# 'cv2.resize()' changes the dimensions of the image. Arguments are (width, height).
resized_image = cv2.resize(image, (300, 300))
cv2.imshow('Resized Image', resized_image)

# Step 3: Crop the image
# Image slicing: [y1:y2, x1:x2] where (x1, y1) is top-left and (x2, y2) is bottom-right.
cropped_image = image[50:250, 50:250]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)

# Step 4: Save resized and cropped images
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imwrite('cropped_image.jpg', cropped_image)

cv2.destroyAllWindows()
