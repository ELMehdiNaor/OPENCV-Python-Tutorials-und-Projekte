# In the code bellow we will learn how to do some average blurring:
# Import the necessary packages:
import cv2
import numpy as np

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\3_Smoothing_Images\trex.png'

# Load the image:
img = cv2.imread(path)

# In order to average blur an image, we use the cv2.blur function.
# This function requires two arguments, the image we want to blur and the size of the kernel.
# As the lines below show, we blur our image with increasing-sized kernels.
# The larger the kernels becomes, the more blurred our image will appear
blurred_img1 = cv2.blur(img,(3,3))
blurred_img2 = cv2.blur(img,(5,5))
blurred_img3 = cv2.blur(img,(7,7))

# We make use of the np.stack function to stack our output images together.
# This method "horizontally stacks" our three images into a row.
# This is useful since we don't want to create three separate windows using the cv2.imshow function
blurred = np.hstack([
          blurred_img1,
          blurred_img2,
          blurred_img3])

# Display the end result:
cv2.imshow("Averages", blurred)
# Wait for key to be pressed:
cv2.waitKey(0)

# Destroy all the windows:
cv2.destroyAllWindows()