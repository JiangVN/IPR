import cv2
from PIL import Image

# Read noisy image
noisy = cv2.imread('noisy_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply median filter
median_blur = cv2.medianBlur(noisy, 3)

# Display the original and filtered images
cv2.imshow('Noisy Image', noisy)
cv2.imshow('Filtered Image', median_blur)


im=Image.open("noisy_image.jpg")
im = im.convert('L')

for i in range(2,im.size[0]-2):
    for j in range(2,im.size[1]-2):
        b=[]
        for p in range(i-1,i+2):
            for q in range(j-1,j+2):
                b.append(im.getpixel((p,q)))
        b.sort()
        if im.getpixel((i,j))>0 and im.getpixel((i,j))<255:
            pass
        elif im.getpixel((i,j))==0 or im.getpixel((i,j))==255:
            if sum([1 for x in b if x==0 or x==255]) > 3*len(b)/4:
                b=[]
                for p in range(i-2,i+3):
                    for q in range(j-2,j+3):
                        b.append(im.getpixel((p,q)))
                if sum([1 for x in b if x==0 or x==255]) == len(b):
                    a=sum(b)/len(b)
                    im.putpixel((i,j),a)
                else:
                    b.remove(0)
                    b.remove(255)
                    im.putpixel((i,j),b[len(b)/2])

im.save("nonoise.jpg")