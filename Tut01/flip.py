from PIL import Image

# Open an image file
img = Image.open('...........jpg')

# Rotate the image by 90 degrees
img_rotated_90 = img.transpose(Image.ROTATE_90)

# Rotate the image by 180 degrees
img_rotated_180 = img.transpose(Image.ROTATE_180)

# Rotate the image by 270 degrees
img_rotated_270 = img.transpose(Image.ROTATE_270)

# Flip the image horizontally
img_flipped_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)

# Flip the image vertically
img_flipped_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)

# Display the original and transformed images
img.show()
img_rotated_90.show()
img_rotated_180.show()
img_rotated_270.show()
img_flipped_horizontal.show()
img_flipped_vertical.show()