# Basic Operations on Images
# Import the necessary libraries:
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 1- Accessing and Modifying pixel values:
# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Resources\messi5.jpg'
# Using the cv2.imread() method to load the image:
img = cv2.imread(path)
# Let's access a pixel value by it's row and column coordinates:
pixel = img[200,200]
# Display the value of the pixel: It's a BGR image, it returns an array of Blue, Green, Red Values
print(pixel)
# Let's access only the green pixel:
g_pixel = img.item(200,200,1)
print(g_pixel)
# Modifying the Blue pixel values:
img.itemset((20,20,0),100)
b_pixel = img.item(20,20,0)
print(b_pixel)

# 2-Accessing Image Properties:
# Image Properties include number of rows, columns and channels, type of data image, number of pixels etc...
# Let's access the shape of this image. Since it's a colored image, the method returns a tuple of number of rows, column and channels:
print(img.shape)

# Let's access the total number of pixels:
print(img.size)

# Let's obtain the datatype of the image:
print(img.dtype)

# 3- Image Region OF interest:
# The ROI is obtained using Numpy indexing. Here we are selection the ball and copying it to another region in the image:
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
# Let's check the result:
cv2.imshow('LeoMessi',img)
cv2.imwrite('Messi6.jpg',img)
# The windows closes when I press any keyboard:
cv2.waitKey(0)


# 4-Splitting and Merging Image Channels:
# Splitting and Merging:
b,g,r = cv2.split(img)
print(b)
print(g)
print(r)
img = cv2.merge((b,g,r))

# Make all the blue pixels equal to zero:
img[0,:,:] = 0
print(img)

# 5- Making Borders for Images:
# If you want to create a border around an image, a border is something like a frame, you can use
# the cv2.copyMakeBorder() function.
# Let's do a simple demonstration for a better understanding:

# An array containing the color of the frame:
Blue = [0,0,255]
# Let's load the image used for this task:
path2 = r'D:\PyCharm\OPENCV_Tutorial\Resources\opencv_logo.jpg'
img2 = cv2.imread(path2)

# Let's create some borders:
replicate = cv2.copyMakeBorder(img2,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img2,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img2,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img2,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img2,10,10,10,10,cv2.BORDER_CONSTANT,value=Blue)

# Display Images using Matplotlib:
plt.subplot(231), plt.imshow(img2,'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate,'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect,'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101,'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap,'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant,'gray'), plt.title('CONSTANT')
plt.show()
