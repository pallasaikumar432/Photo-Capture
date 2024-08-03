import cv2
def capture_photo(camera_index=0, file_name="captured_photo.jpg"):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)
#     # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    # Read a frame from the camera
    ret, frame = cap.read()
    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame")
        cap.release()
        return
    # Save the captured frame as an image
    cv2.imwrite(file_name, frame)
    # Release the camera
    cap.release()
    print(f"Photo captured and saved as '{file_name}'")
# Capture a photo and save it as 'captured_photo.jpg'
capture_photo()






