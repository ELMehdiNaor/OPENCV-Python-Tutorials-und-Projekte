# The Mouse as a Paint Brush
# Import the necessary libraries:
import cv2

# This piece of code will list all available events:
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# Path to the image:
path = r'D:\PyCharm\OPENCV_Tutorial\Resources\lena.png'
img  = cv2.imread(path)

# Defining a Mouse callback function and it's arguments:
def draw_red_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,0,225),-1)

# Create a window and bind the function to window:
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_red_circle)

# Create an infinite Loop:
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('testImage.png',img)
        # Stop if the condition is true
        break
cv2.destroyAllWindows()