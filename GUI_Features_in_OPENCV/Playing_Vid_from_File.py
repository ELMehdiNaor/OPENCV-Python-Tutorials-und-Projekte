# Getting Started with Videos
# Import the cv2 library
import cv2
# Path to the video
path = r'D:\PyCharm\OPENCV_Tutorial\Resources\testVideo.mp4'
# Creat a video capture object, in this case we are reading the video from file
video_capture = cv2.VideoCapture(path)
# A Loop to read one frame at a time from the video stream using the video_capture.read() method
while video_capture.isOpened():
    ret, frame = video_capture.read()
      # If frame is read correctly ret is True, if not display the following message:
    if not ret:
         print("Can't receive frame (stream end?). Exiting...")
         break

 # Display the current frame in a window
    cv2.imshow('displayedVideo', frame)
     # Use the cv2.waitKey() function to pause for 1 ms between video frames
     # If the user presses the 'q' key, you exit the loop
    if cv2.waitKey(5) == ord('q'):
        break