# add_text.py
import cv2

# Step 1: Load the image
image = cv2.imread('sample.jpg', 1)

# Step 2: Define text and its properties
# 'cv2.putText()' adds text to the image. Arguments include text, position, font, font scale, color, and thickness.
text = "OpenCV Demo"
cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Step 3: Display the image with text
cv2.imshow('Text on Image', image)
cv2.waitKey(0)

# Step 4: Save the image with text
cv2.imwrite('text_image.jpg', image)

cv2.destroyAllWindows()
