# Read, Display and Write an Image using OpenCV
# Import the cv2 library
import cv2
# Path to the image
path = 'D:\PyCharm\OPENCV_Tutorial\Resources\lena.png'
# The function cv2.imread() is used to read an image
img = cv2.imread(path)
# The function cv2.imshow is used to display an image
cv2.imshow('displayedLena', img)
# The function cv2.waitKey() waits for a key press to close all the windows and 0 specifies indefinite Loop (time is in milliseconds)
cv2.waitKey(2000)
# The function cv2.destroyAllWindows simply destroys all the windows we created
cv2.destroyAllWindows()
# The function cv2.imwrite() is used to save an image
cv2.imwrite('savedLena.png', img)