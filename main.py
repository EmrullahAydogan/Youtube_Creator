import cv2

# Open the video file
video_path = 'C:/Users/mega8/PycharmProjects/Videos/forcode.mp4'  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Set the desired frame rate (in milliseconds)
frame_delay = 30  # Adjust this value to control the playback speed

# Loop to read frames from the video
while True:
    ret, frame = cap.read()

    # Check if we have reached the end of the video
    if not ret:
        break

    # Display the current frame
    cv2.imshow('Video', frame)

    # Delay to control playback speed
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
