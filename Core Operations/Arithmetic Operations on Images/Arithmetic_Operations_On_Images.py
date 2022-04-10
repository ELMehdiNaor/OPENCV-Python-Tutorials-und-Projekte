# Let's learn how to perform several arithmetic operations on images:
# like addition, substraction, bitwise operations etc...
# We will learn to use these methods: cv2.add(), cv2.addWeighted()

# Import the necessary libraries:
import cv2
import numpy as np

# 1-Image addition:
# We can ann two images by using the OPENCV method cv2.add():
# A simple  example:
x = np.uint8([250])
y = np.uint8([10])
res = cv2.add(x,y)
# Display the results:
print(res)

# 2-Image Blending:
# Image Blending is also considered as an image addition, but differents weights are given to images,
# so that it gives a feeling of blending or transparency.
# Here we took two images to blend them together. The first image is given a weight of 0,7 and second image a weight of 0,3:
# Load the images:
path1 = r'D:\PyCharm\OPENCV_Tutorial\Resources\ML.jpg'
path2 = r'D:\PyCharm\OPENCV_Tutorial\Resources\obj.jpg'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
# Check of the image dimensions are the same:
print(img1.shape)
print(img2.shape)
# :
res1 = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
# Display the results:
cv2.imshow('Result', res1)
# Resize the Display_window:
cv2.resizeWindow('Result',200,200)
cv2.waitKey(0)

# 3-Bitwise Operations:
# This includes bitwise AND, OR, NOT and XOR operations. Below we will see an example on how
# to change a particular region of an image.
# We want to put the OPENCV logo, above an image. If we add two images, the color will change, if we blend it
# we will get a transparent effect. We want it to be opaque, so we can do it with bitwise operations as shown below:
# Let's load the two images first:
path3 = r'D:\PyCharm\OPENCV_Tutorial\Resources\messi5.jpg'
path4 = r'D:\PyCharm\OPENCV_Tutorial\Resources\opencv_logo.jpg'
img3 = cv2.imread(path3)
img4 = cv2.imread(path4)
# We want to put the logo on the top-left corner, so we create a Region of Interest:
rows, columns, channels = img4.shape
roi = img3[0:rows, 0:columns]
# Now we create a mask of logo and create its inverse mask also:
img2gray = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Now black out the area of the logo in the region of interest:
img3_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
# Take only the region of the logo from the logo image:
img4_fg = cv2.bitwise_and(img4, img4, mask = mask)
# Put the logo in the region of interest and modify the main image:
res2 = cv2.add(img3_bg, img4_fg)
img3[0:rows, 0:columns] = res2
# Let's display the results:
cv2.imshow('Results',img3)
cv2.imwrite('AOOI.jpg',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()