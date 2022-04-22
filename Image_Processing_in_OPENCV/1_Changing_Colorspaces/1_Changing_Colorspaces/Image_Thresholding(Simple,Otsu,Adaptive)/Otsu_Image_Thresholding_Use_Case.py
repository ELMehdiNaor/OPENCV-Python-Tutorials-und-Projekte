# Tn the code below we used Otsu's thresholding to detect coins in images
# Import the necessary libraries:
import cv2

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Image_Processing_in_OPENCV\2_Image_Thresholding\coins2.jpg'

# Load the image and display it:
image = cv2.imread(path)
cv2.imshow("Image", image)

# Convert the image to grayscale and blur it slightly:
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred  = cv2.GaussianBlur(gray_img, (7,7), 0)

# Apply Otsu's automatic thresholding which automatically determines
# the best threshold value:
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))

# Visualize only the masked regions in the image:
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Result",masked)

# Wait for a key to pressed:
cv2.waitKey(0)

# Destroy all windows:
cv2.destroyAllWindows()