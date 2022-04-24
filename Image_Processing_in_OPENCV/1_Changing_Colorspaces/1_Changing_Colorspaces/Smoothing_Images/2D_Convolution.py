# In the code below we will learn how to apply custom-made filters to images (2D convolution):
# Import the necessary packages:
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\4_Smoothing_Images\trex.png'

# Load the image:
img = cv2.imread(path)

# Define our kernel as a numpy array:
kernel = np.ones((5,5),np.float32)/25
# Use the function cv2.filter2D() to convolve(combine) a kernel with an image.
avr_blurred = cv2.filter2D(img,-1,kernel)

# Dislay the final results using pyplot:
# List of images:
images = [img, avr_blurred]
# Lits of titles:
titles = ['Original','Average Blur']

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

# Wait for a key to be pressed:
cv2.waitKey(0)
# Destroy all windows:
cv2.destroyAllWindows()