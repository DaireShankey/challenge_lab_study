# video_progress_bar.py
import cv2

# Load video
cap = cv2.VideoCapture('task1.mp4')
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate progress bar width
    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    progress = int((current_frame / total_frames) * frame.shape[1])

    # Draw the progress bar
    cv2.rectangle(frame, (0, frame.shape[0] - 10), (progress, frame.shape[0]), (0, 255, 0), -1)

    # Display the frame
    cv2.imshow("Video with Progress Bar", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
