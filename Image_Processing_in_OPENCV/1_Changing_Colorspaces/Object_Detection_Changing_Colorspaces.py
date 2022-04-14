# The purpose of this code was tracking my red hoodie:
# Importing the necessary packages:
import cv2
import numpy as np

# function do nothing:
def nothing(x):
    pass

# Read a video stream from the laptop built-in webcam:
# The device index for the built-in camera is 0
video_cap = cv2.VideoCapture(0)

# Create a window:
cv2.namedWindow("Trackbars")

# Creat Trackbars to set the values of the HSV-colorspace:
# Lower Values:
cv2.createTrackbar("L-H","Trackbars",0,179,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
# Upper Values:
cv2.createTrackbar("U-H", "Trackbars",0,179,nothing)
cv2.createTrackbar("U-S", "Trackbars",0,255,nothing)
cv2.createTrackbar("U-V", "Trackbars",0,255,nothing)

# Infinite Loop:

while True:
    #
    ret, frame = video_cap.read()
    # Transform the frames from the BGR-colorspace to the HSV-colorspace:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Get the values of the trackbar:
    # Lower Values:
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    # Upper Values:
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    # Define the thresholds:
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    # Let's make a Mask:
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # Show the actual frame:
    cv2.imshow("frame", frame)
    # Show the mask:
    cv2.imshow("mask", mask)
    # Show the end-result:
    cv2.imshow("result", result)
    # Wait for a keyboard to be pressed:
    key = cv2.waitKey(1)
    # If  the keyboard presses is esc,  then break the loop:
    if key == 27:
      break
# Destroy all created Windows and release all the captures:
cv2.destroyAllWindows()
video_cap.release()