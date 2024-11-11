# load_display_save.py
import cv2

# Step 1: Load an image from file
# 'cv2.imread()' loads an image. Argument '0' loads in grayscale, '1' in color.
image = cv2.imread('sample.jpg', 1)

# Step 2: Display the loaded image in a window
# 'cv2.imshow()' displays an image in a new window. First argument is window name.
cv2.imshow('Loaded Image', image)

# Step 3: Wait for a key press to close the display window
# 'cv2.waitKey(0)' waits indefinitely until any key is pressed.
cv2.waitKey(0)

# Step 4: Save the image to disk with a new name
# 'cv2.imwrite()' saves the image with specified filename.
cv2.imwrite('saved_image.jpg', image)

# Step 5: Destroy all windows after key press
cv2.destroyAllWindows()
