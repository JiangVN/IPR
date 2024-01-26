import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.transforms import ScalarMappable
import numpy as np

# Open the image file
image = imread('...........jpg')

# Get the current figure
fig = plt.gcf()

# Get the current image DPI
dpi = fig.dpi

# Calculate the new size of the image in pixels
new_width = 500
new_height = int(new_width * image.shape[0] / image.shape[1])

# Create a new figure with the desired DPI
fig = plt.figure(figsize=(new_width/dpi, new_height/dpi), dpi=dpi)

# Create a new subplot
ax = fig.add_subplot(111)

# Display the resized image
ax.imshow(image, cmap='gray')

# Set the limits of the colorbar
vmin = np.min(image)
vmax = np.max(image)

# Create a colorbar
cb = fig.colorbar(ScalarMappable(cmap='gray', norm=plt.Normalize(vmin, vmax)), ax=ax)

# Show the plot
plt.show()