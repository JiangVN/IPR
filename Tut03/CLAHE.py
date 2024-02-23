import cv2
import numpy as np

# Load a low-contrast image
img = cv2.imread('ycrcb_image.jpg', cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply CLAHE to the grayscale image
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_gray = clahe.apply(gray)

# Convert the CLAHE-equalized grayscale image back to color
clahe_img = cv2.cvtColor(clahe_gray, cv2.COLOR_GRAY2BGR)

# Combine the original and enhanced images for comparison
result = np.hstack((img, clahe_img))

cv2.imwrite('CLAHE.jpg', result)