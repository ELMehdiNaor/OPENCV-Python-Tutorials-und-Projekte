# Learn to draw different geometric shapes with OpenCV:
# Import the necessary libraries
import cv2
import numpy as np

# Create a black image:
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line:
cv2.line(img,(0,0),(511,511),(255,0,0),4)

# Draw a green rectangle:
cv2.rectangle(img,(384,0), (510,128), (0,255,0), 2)

# Draw a circle inside the rectangle drawn above:
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Draw an Ellipse:
cv2.ellipse(img,(256,256),(100,50) ,0 ,0 ,180 , 255, -1)

# Draw a Polygon:
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# Adding Text to our Image:
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# Display the image for a specific amount of time and save it:
cv2.imshow('actualImage', img)
cv2.imwrite('actualImage.jpg', img)
cv2.waitKey(2500)

# Destroy:
cv2.destroyAllWindows()


