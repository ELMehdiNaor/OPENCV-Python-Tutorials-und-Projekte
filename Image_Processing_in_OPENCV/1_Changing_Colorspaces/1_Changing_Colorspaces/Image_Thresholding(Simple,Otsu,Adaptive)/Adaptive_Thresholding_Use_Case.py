# Tn the code below we used Adaptive Thresholding
# to have a better results for images with varying illumination
# Import the necessary librarie:
import cv2
from matplotlib import pyplot as plt

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\2_Image_Thresholding\number_plate2.jpg'

# Load the input image, convert it to a grayscale-image and blur it slightly:
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_image, (7,7), 0)

# Apply some Simple Image Thresholding:
(T1,thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
print("[INFO] simple thresholding value: {}".format(T1))

# Apply Otsu's Image Thresholding:
(T2,OtsuThresh) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("[INFO] otsu's thresholding value: {}".format(T2))

# Apply Adaptive Thresholding:
AdptThresh = cv2.adaptiveThreshold(blurred, 255,  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)

# List of Titles:
titles = ['Original','Blurred', 'Simple', 'Otsu', 'Adapative']
# List of Images:
images = [gray_image,blurred, thresh, OtsuThresh, AdptThresh]

# For Loop to display multiple images:

for i in range(5):
    plt.subplot(1,5,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Wait for a key to be pressed:
cv2.waitKey(0)
# Destroy all windows:
cv2.destroyAllWindows()