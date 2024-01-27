from PIL import Image, ImageEnhance

# Open the image file
image = Image.open('...........jpg')

# Increase the brightness and decrease the contrast
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(1.5)

enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(0.5)

# Display the enhanced image
image.show()