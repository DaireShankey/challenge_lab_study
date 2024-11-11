# video_capture.py
import cv2

# Step 1: Initialize video capture from the default camera
cap = cv2.VideoCapture(0)

# Step 2: Capture video frame-by-frame
while True:
    ret, frame = cap.read()  # 'ret' is True if frame is read correctly, 'frame' is the frame

    if not ret:
        print("Failed to capture video frame")
        break

    # Display the frame in a window
    cv2.imshow('Webcam Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 3: Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
