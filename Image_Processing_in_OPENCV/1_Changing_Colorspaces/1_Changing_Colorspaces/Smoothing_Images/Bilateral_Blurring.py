# In the code bellow we will learn how to do Bilateral Blurring:
# Import the necessary libraries:
import cv2
import numpy as np

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\3_Smoothing_Images\beach.png'

# Load the image:
img = cv2.imread(path)

# In order to bilateral blur an image, we make use of the cv2.bilateralFilter function.
# This function requires four arguments.
# The first parameter we supply is the image we want to blur. Then we need to define the diameter of our pixel neighborhood.
# The third argument is our color sigma. Finally we need to supply the space of sigma.
blurred_img1 = cv2.bilateralFilter(img, 3, 21, 21)
blurred_img2 = cv2.bilateralFilter(img, 5, 31, 31)
blurred_img3 = cv2.bilateralFilter(img, 7, 41, 41)

# We make use of the np.stack function to stack our output images together.
# This method "horizontally stacks" our three images into a row.
# This is useful since we don't want to create three separate windows using the cv2.imshow function
blurred = np.hstack([blurred_img1, blurred_img2, blurred_img3])

# Display the results:
cv2.imshow("Bilateral Blurring", blurred)

# Wait for a key to be pressed:
cv2.waitKey(0)

# Destroy all Windows:
cv2.destroyAllWindows()