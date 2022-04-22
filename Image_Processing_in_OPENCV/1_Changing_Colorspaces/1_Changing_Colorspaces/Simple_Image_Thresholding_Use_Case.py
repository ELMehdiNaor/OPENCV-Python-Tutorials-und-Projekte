# Tn the example below we used thresholding to detect coins in images
# Import the necessary packages:
import numpy as np
import cv2

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\2_Image_Thresholding\coins.png'

# Load the image, convert it to grayscale, and blur it slightly:
img   = cv2.imread(path)
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Let's apply basic thresholding. The first parameter is the image we want to threshold,
# the second value is our threshold. If a pixel value is greater than our threshold (in this case 155)
# we set it to be "White", otherwise it is "Black"
(T, thresh) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# Make the coins white rather than black
(T,threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# Finally, let's us our threshold as a mask and visualize only the coins in the image
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=threshInv))

# Wait for a key to pressed:
cv2.waitKey(0)

# Destroy all windows:
cv2.destroyAllWindows()