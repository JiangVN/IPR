import cv2
import numpy as np

# Load the image
img = cv2.imread('...........jpg',0)

# Apply the Sobel operator to find edges in the image
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# Display the original image and the edge images
cv2.imshow('Original Image', img)
cv2.imshow('Edge Image (x-direction)', np.uint8(np.absolute(sobelx)))
cv2.imshow('Edge Image (y-direction)', np.uint8(np.absolute(sobely)))

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()