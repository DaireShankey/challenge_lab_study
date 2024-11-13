import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
video_writer = None
recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if recording:
        cv2.circle(frame, (20, 20), 10, (0, 0, 255), -1)
        video_writer.write(frame)

    cv2.imshow("Camera Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Start/Stop recording
        if recording:
            video_writer.release()
            recording = False
        else:
            filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
            video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
            recording = True
    elif key == ord('c'):  # Capture image
        img_filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(img_filename, frame)
    elif key == ord('q'):  # Quit
        break

cap.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()
