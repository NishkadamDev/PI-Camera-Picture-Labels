import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
import time

# Load YOLOv8 nano model (downloads automatically on first run)
model = YOLO("yolov8n.pt")

# Set up Pi Camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)}))
picam2.start()

print("Camera started. Press 'q' to quit.")
time.sleep(1)  # Let camera warm up

while True:
    # Grab frame from camera
    frame = picam2.capture_array()

    # Run YOLO detection
    results = model(frame, verbose=False)

    # Draw boxes and labels on the frame
    annotated_frame = results[0].plot()

    # Convert RGB to BGR for OpenCV display
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

    # Show the frame
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
picam2.stop()
cv2.destroyAllWindows()
