# In the code bellow we will learn to do some Gaussian Blurring:
# Import the necessary packages:
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Define the path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\3_Smoothing_Images\trex.png'

# Load the image:
img = cv2.imread(path)

# In order to gaussian blur an image, we make use of the cv2.GaussianBlur function
# This function requires three arguments, the image we want to blur and the size of the kernel,
# The last parameter is our sigma, the standard deviation in the x-axis direction.
# As the lines below show, we blur our image with increasing-sized kernels.
# The larger the kernels becomes, the more blurred our image will appear
blurred_img1 = cv2.GaussianBlur(img,(3,3),0)
blurred_img2 = cv2.GaussianBlur(img,(5,5),0)
blurred_img3 = cv2.GaussianBlur(img,(7,7),0)

# We make use of the np.stack function to stack our output images together.
# This method "horizontally stacks" our three images into a row.
# This is useful since we don't want to create three separate windows using the cv2.imshow function
blurred = np.hstack([
          blurred_img1,
          blurred_img2,
          blurred_img3])


# Display the result:
cv2.imshow("Gaussian Blur", blurred)
# Wait for a key to be pressed:
cv2.waitKey(0)
# Destroy all windows:
cv2.destroyAllWindows()