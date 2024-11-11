# camera_application.py
import cv2
from datetime import datetime

# Initialize camera and set video writer to None initially
cap = cv2.VideoCapture(0)
video_writer = None
recording = False

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw red dot if recording
    if recording:
        cv2.circle(frame, (20, 20), 10, (0, 0, 255), -1)

    # Show the preview
    cv2.imshow("Camera Preview", frame)

    # Capture key events
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Start/Stop recording
        if recording:
            video_writer.release()  # Stop recording
            recording = False
        else:
            # Start recording with a unique filename
            filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
            video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
            recording = True
    elif key == ord('c'):  # Capture an image
        img_filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(img_filename, frame)
    elif key == ord('q'):  # Quit
        break

    # Write frame to video file if recording
    if recording and video_writer:
        video_writer.write(frame)

# Release resources
cap.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()
