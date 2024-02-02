import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('...........jpg',0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])

equ = cv2.equalizeHist(img)
cv2.imwrite('equalization.jpg', equ)

# Display the histogram using matplotlib.pyplot.hist
plt.hist(img.ravel(),256,[0,256],color='k')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()