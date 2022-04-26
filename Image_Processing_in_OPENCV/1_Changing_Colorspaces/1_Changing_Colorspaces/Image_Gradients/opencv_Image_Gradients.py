# In the code bellow we will learn how to use gradient filters to detect edges
# Import the necessary libraries:
import cv2
from matplotlib import pyplot as plt

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\4_Image_Gradients\Sudoku.png'

# Load the image:
img = cv2.imread(path)

# Set the kernel size, depending on whether we are using the Sobel
# operator of the Scharr operator, then compute the gradients along
# the x and y axis, respectively:
gX = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
gY = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)
gL = cv2.Laplacian(img, cv2.CV_64F)

# Displaying the images:
images = [img,gX,gY,gL]
titles = ['Original','Sobel_X','Sobel_Y','Laplacian']
for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
# Wait for a key to be pressed:
cv2.waitKey(0)
# Destroy all windows:
cv2.destroyAllWindows()