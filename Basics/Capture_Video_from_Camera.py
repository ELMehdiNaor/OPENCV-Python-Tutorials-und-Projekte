# Import cv2 library
import cv2
# Create a VideoCapture() object. It's argument is the device index
video_capture = cv2.VideoCapture(0)
#
if not video_capture.isOpened():
    print("Cannot open camera")
    exit()

#
while True:
    # capture frame by frame
    ret, frame = video_capture.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame(stream end?). Exiting ...")
        break
    # Display the resulting frame
    cv2.imshow('actualFrame', frame)
    if cv2.waitKey(1) == ord('q'):
        break