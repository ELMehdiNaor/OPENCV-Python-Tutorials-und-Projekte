# In the code bellow we will learn how to perform Median Blurring:
# Import the necessary libraries:
import cv2
import numpy as np

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\3_Smoothing_Images\trex.png'

# Load the image:
img = cv2.imread(path)

# In order to median blur an image, we make use of the cv2.medianBlur function
# This function requires two arguments, the image we want to blur and the size of the kernel,
# As the lines below show, we blur our image with increasing-sized kernels.
# The larger the kernels becomes, the more blurred our image will appears
blurred_image1 = cv2.medianBlur(img, 3)
blurred_image2 = cv2.medianBlur(img, 5)
blurred_image3 = cv2.medianBlur(img, 7)

# We make use of the np.stack function to stack our output images together.
# This method "horizontally stacks" our three images into a row.
# This is useful since we don't want to create three separate windows using the cv2.imshow function
blurred = np.hstack([blurred_image1, blurred_image2, blurred_image3])

# Display the final results:
cv2.imshow("Median_Blurring", blurred)

# Wait for a key to be pressed:
cv2.waitKey()

# Destroy all windows:
cv2.destroyAllWindows()