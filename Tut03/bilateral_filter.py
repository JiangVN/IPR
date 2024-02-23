import cv2

# Load an image
image = cv2.imread('...........jpg')

# Apply bilateral filter
bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)

# Display the original and filtered images
cv2.imshow('Original', image)
cv2.imshow('Bilateral Filter', bilateral_filtered_image)
