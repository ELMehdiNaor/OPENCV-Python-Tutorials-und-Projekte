# The purpose of this code is to learn how to perform simple thresholding
# Import the necessary libraries:
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\2_Image_Thresholding\gradient.png'
# Load the input image as a grayscale image:
img = cv2.imread(path, cv2.COLOR_BGR2GRAY)

# The first argument is the source image, which should be a grayscale image.
# The second argument is the threshold value which is used to classify the pixel values.
# The third argument is the maximum value which is assigned to pixel values exceeding the threshold
# If the pixel value is smaller than the threshold in this case 10, then it is set to 0(black).
# Otherwise it is set to the maximum value 255(white)
ret, thresh1 = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)

# List of titles
titles = ['Original Image','Binary','Binary_inv']
# List which contains the original image and the thresholded images:
images = [img, thresh1, thresh2]

# For Loop to display multiple images:
for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Wait for a keyboard-key to be pressed:
cv2.waitKey(0)
# Destroy all windows:
cv2.destroyAllWindows()