# Learn to bind trackbar to OPENCV windows
# Import the necessary libraries:
import cv2
import numpy as np

# This is the callback function which is executed every time the trackbar value changes
# The default argument is the trackbar position(x)
# The function in this case do nothing
def nothing(x):
    pass

# Create a black image and a window:
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

# Create a trackbar to change colors:
cv2.createTrackbar('Red','image',0,255,nothing)
cv2.createTrackbar('Green','image',0,255,nothing)
cv2.createTrackbar('Blue','image',0,255,nothing)

# Create a switch for ON/OFF functionality:
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

# Create an infinite LOOP:
while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
# Get the current positions of the four trackbars:
    r = cv2.getTrackbarPos('Red','image')
    g = cv2.getTrackbarPos('Green','image')
    b = cv2.getTrackbarPos('Blue','image')
    s = cv2.getTrackbarPos(switch,'image')
# If statement for the switch functionality
    # If the switch functionality is off, the screen always remains black
    if s == 0:
       img[:] = 0
    # If the switch functionality is on, we can see the change of the colors
    else:
       img[:] = [b,g,r]
# Destroy all the windows we created:
cv2.destroyAllWindows()