import cv2

# Load an image
image = cv2.imread('...........jpg')

# Convert RGB to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split HSV image into separate channels
h, s, v = cv2.split(hsv_image)

# Display the separate channels of HSV
cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)

# Convert RGB to YCbCr
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Split YCbCr image into separate channels
y, cb, cr = cv2.split(ycrcb_image)

# Display the separate channels of YCbCr
cv2.imshow('Y Channel', y)
cv2.imshow('Cb Channel', cb)
cv2.imshow('Cr Channel', cr)

# Save the images
cv2.imwrite('hsv_image.jpg', hsv_image)
cv2.imwrite('ycrcb_image.jpg', ycrcb_image)