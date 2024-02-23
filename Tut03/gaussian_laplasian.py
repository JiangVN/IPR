import cv2
import numpy as np

def generate_gaussian_pyramid(image, scale=1.5, minSize=(30, 30)):
    yield image

    while True:
        w = int(image.shape[1] / scale)
        image = cv2.resize(image, (w, int(image.shape[0] / scale)))

        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        yield image

def generate_laplacian_pyramid(gaussian_pyramid):
    laplacian_pyramid = []
    gaussian_pyramid = gaussian_pyramid[::-1]

    for i in range(1, len(gaussian_pyramid)):
        upscaled = cv2.resize(gaussian_pyramid[i], (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0]))
        laplacian = cv2.subtract(gaussian_pyramid[i - 1], upscaled)
        laplacian_pyramid.append(laplacian)

    return laplacian_pyramid

# Load an image
image = cv2.imread('...........jpg')

# Generate Gaussian pyramid
gaussian_pyramid = generate_gaussian_pyramid(image, scale=1.5)

# Generate Laplacian pyramid
laplacian_pyramid = generate_laplacian_pyramid(gaussian_pyramid)

# Display the Gaussian and Laplacian pyramids
for i, level in enumerate(gaussian_pyramid):
    cv2.imshow(f'Gaussian Pyramid - Level {i}', level)

for i, level in enumerate(laplacian_pyramid):
    cv2.imshow(f'Laplacian Pyramid - Level {i}', level)

cv2.waitKey(0)
cv2.destroyAllWindows()