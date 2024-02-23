import cv2
import numpy as np

# Load an image
image = cv2.imread('...........jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Otsu thresholding to the grayscale image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize the marker image with the background marked as 0
marker = np.zeros_like(gray)

# Mark the foreground objects with unique labels
for i, contour in enumerate(contours):
    cv2.drawContours(marker, [contour], -1, i+1, -1)

# Apply the watershed algorithm to the marker image
_, labels, _, _ = cv2.watershed(image, marker)

# Set the watershed lines to the background color
marker[labels == -1] = 0

# Create a color image from the labeled regions
colored_labels = cv2.cvtColor(marker.astype(np.uint8), cv2.COLOR_GRAY2BGR)

# Display the original image and the segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', colored_labels)
cv2.waitKey(0)
cv2.destroyAllWindows()