import cv2

cap = cv2.VideoCapture('input_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply Gaussian blur
    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    cv2.imshow('Blurred Video', blurred_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
