import cv2

# Open the video file
video_path = "butterfly_flower_insect_nature_515.mp4"
cap = cv2.VideoCapture(video_path)

# Create a VideoWriter object to save the grayscale video
output_path = "output_video"
output = cv2.VideoWriter(output_path, 0, 1, (0, 0), isColor=False)

# Process each frame of the video
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Convert the frame to grayscale
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the grayscale frame to the output video
        output.write(grayscale_frame)

        # Display the grayscale frame
        cv2.imshow("Grayscale Video", grayscale_frame)

        # Check for 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the resources
cap.release()
output.release()
cv2.destroyAllWindows()
