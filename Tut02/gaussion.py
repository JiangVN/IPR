import cv2
import numpy as np

# Load the image
img = cv2.imread('...........jpg',0)

# Add Gaussian noise to the image
mean = 0
var = 0.1
sigma = var**0.5
noise = np.random.normal(mean,sigma,(img.shape[0],img.shape[1]))
noisy_img = img + noise
cv2.imshow('Original Image', img)
cv2.imshow('Noisy Image', np.uint8(noisy_img))

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()