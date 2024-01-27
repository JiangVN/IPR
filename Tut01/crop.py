from PIL import Image

# Open the image file
image = Image.open('grayscale.jpg')

# Define the area to crop
left = 100
upper = 50
right = 400
lower = 350

# Crop the image
image = image.crop((left, upper, right, lower))

# Display the cropped image
image.show()