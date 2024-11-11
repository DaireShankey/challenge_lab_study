# motion_detection.py
import cv2
from datetime import datetime

# Initialize camera and background subtractor
cap = cv2.VideoCapture(0)
back_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = back_sub.apply(frame)

    # Detect contours to determine motion
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if any(cv2.contourArea(contour) > 500 for contour in contours):
        # Save a snapshot if motion is detected
        filename = f"motion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Motion detected, snapshot saved as {filename}")

    # Display the foreground mask
    cv2.imshow("Motion Detection", fg_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
