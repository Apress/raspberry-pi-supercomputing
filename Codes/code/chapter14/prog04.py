import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('/home/pi/book/Dataset/Sample03.jpg')
img_ch = img[:, :, 0]

plt.hist(img_ch.ravel(), 256, [0, 256])
plt.title('Histogram Demo')
plt.xticks([]), plt.yticks([])

plt.show()
