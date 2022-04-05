# First coding lesson
import cv2

# Specifying the path to the image
path = r'D:\PyCharm\OPENCV_Tutorial\Resources\lena.png'

# Load an image using 'imread'
img = cv2.imread(path)

# To display our image variable, we use 'imshow'
cv2.imshow('Lena', img)

# We specify a delay for how long you keep the window open (time is in milliseconds here)
cv2.waitKey(2000)

# This closes all open windows
cv2.destroyAllWindows()