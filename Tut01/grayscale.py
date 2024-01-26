from PIL import Image

def grayScale(input, output):
    image = Image.open(input)
    grayScale_image = image.convert('L')
    grayScale_image.save(output)
    print(f"GrayScale Image saved as {output}")

grayScale('...........jpg', 'grayscale.jpg')