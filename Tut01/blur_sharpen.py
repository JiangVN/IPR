from PIL import Image, ImageFilter

# Open an image file
img = Image.open('...........jpg')

# Apply a box blur filter to the image
img_blurred = img.filter(ImageFilter.BLUR)

# Apply a sharpen filter to the image
img_sharpened = img.filter(ImageFilter.SHARPEN)

# Display the original, blurred, and sharpened images
img.show()
img_blurred.show()
img_sharpened.show()