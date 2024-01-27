from PIL import Image

def resize(input, output, nwidth, nheight):
    image = Image.open(input)
    resize_img = image.resize(nwidth, nheight)
    resize_img.save(output)
    print(f'Resized image saved as {output}')

resize('grayscale.jpg', 'resize.jpg', 500, 500)
