# Motion Detection Camera using Python

import cv2

# Start webcam

camera = cv2.VideoCapture(0)

if not camera.isOpened():
print("Camera could not be opened!")
exit()

previous_frame = None

print("Motion Detection Camera Started")
print("Press 'q' to exit.")

while True:
ret, frame = camera.read()

```
if not ret:
    print("Unable to read camera.")
    break

# Convert frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Reduce image noise
gray = cv2.GaussianBlur(gray, (21, 21), 0)

# Store the first frame
if previous_frame is None:
    previous_frame = gray
    continue

# Find difference between frames
difference = cv2.absdiff(previous_frame, gray)

# Create threshold image
_, threshold = cv2.threshold(
    difference, 25, 255, cv2.THRESH_BINARY
)

# Find moving objects
contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

motion_detected = False

for contour in contours:

    # Ignore very small movements
    if cv2.contourArea(contour) < 500:
        continue

    motion_detected = True

    x, y, w, h = cv2.boundingRect(contour)

    # Draw rectangle around moving object
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display status
if motion_detected:
    status = "MOTION DETECTED"
    print("Motion detected!")
else:
    status = "NO MOTION"

cv2.putText(
    frame,
    status,
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
```
