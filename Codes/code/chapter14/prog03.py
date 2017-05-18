import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('/home/pi/book/Dataset/4.2.01.tiff')
img_ch = img[:, :, 0]

plt.imshow(img_ch, cmap='nipy_spectral')
plt.title('Colorbar Demo')
plt.colorbar()
plt.xticks([]), plt.yticks([])

plt.show()
