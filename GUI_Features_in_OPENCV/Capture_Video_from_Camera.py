# import the necessary libraries:
import cv2
# Create a Video capture object, It's argument is the device index:
video_capture = cv2.VideoCapture(0)
# Little check:
if not video_capture.isOpened():
    print("Cannot open the camera")
    exit()

# Loop to read one frame at a time:
while True:
    # capture frame by frame:
    ret, frame = video_capture.read()
    # Little check:
    if not ret:
        print("Can't receive frame.....")
        break
    # otherwise display:
    cv2.imshow('laptopCamera', frame)
    # until the user presses the key:
    if cv2.waitKey(1) == ord('q'):
        break
# When everything is done, release the capture:
video_capture.release()
cv2.destroyAllWindows()