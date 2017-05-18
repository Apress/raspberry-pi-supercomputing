import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('/home/pi/book/Dataset/4.2.01.tiff')
img_ch = img[:, :, 0]

plt.subplot(1, 2, 1)
plt.imshow(img_ch)
plt.title('Default Colormap')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(img_ch, cmap='hot')
plt.title('Hot Colormap')
plt.xticks([]), plt.yticks([])

plt.show()
