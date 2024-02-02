import cv2 as cv
import numpy as np

image = cv.imread('...........jpg', 0)

gray_image = cv.imread('...........jpg', cv.IMREAD_GRAYSCALE)
cv.imwrite('grayscale.jpg', gray_image)

ret,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)
cv.imwrite('binary_image.jpg', thresh1)

kernel_square = np.ones((5,5),np.uint8)
kernel_circle = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

dilation_square = cv.dilate(thresh1,kernel_square,iterations = 1)
cv.imwrite('dilation_square.jpg', dilation_square)

dilation_circle = cv.dilate(thresh1,kernel_circle,iterations = 1)
cv.imwrite('dilation_circle.jpg', dilation_circle)

erosion_square = cv.erode(thresh1,kernel_square,iterations = 1)
cv.imwrite('erosion_square.jpg', erosion_square)

erosion_circle = cv.erode(thresh1,kernel_circle,iterations = 1)
cv.imwrite('erosion_circle.jpg', erosion_circle)

cv.waitKey(0)
cv.destroyAllWindows()