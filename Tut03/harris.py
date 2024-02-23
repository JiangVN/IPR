import cv2
import numpy as np

# Load an image
image = cv2.imread('...........jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Harris Corner Detection
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate the image to mark the corners
dst = cv2.dilate(dst, None)

# Threshold for an optimal value
image[dst > 0.01 * dst.max()] = [0, 0, 255]

# Display the image with detected corners
cv2.imshow('dst', image)