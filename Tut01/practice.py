from PIL import Image

def loadImage(path):
    image = Image.open(path)
    image.show()

loadImage('...........jpg')