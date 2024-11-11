# save_as_npy.py
import cv2
import numpy as np
from datetime import datetime

# Initialize camera
cap = cv2.VideoCapture(0)
frames = []  # To store frames if saving as video

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera Feed", frame)

    # Capture and save a single frame as .npy when 'c' is pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.npy"
        np.save(filename, frame)
        print(f"Image saved as {filename}")

    # Capture and store frames to save as video
    if cv2.waitKey(1) & 0xFF == ord('v'):
        frames.append(frame)

    # Quit and save the video as .npy
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if frames:
            video_filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.npy"
            np.save(video_filename, np.array(frames))
            print(f"Video saved as {video_filename}")
        break

cap.release()
cv2.destroyAllWindows()
