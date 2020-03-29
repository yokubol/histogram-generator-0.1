import matplotlib.pyplot as plt
import numpy as np
import skimage.io

image_input = input("specify your image name: ")

image = skimage.io.imread(f"{image_input}.jpg", as_gray=True)
image = np.uint8(image*255)

hist = np.histogram(image, bins=256)
plt.bar(x=np.arange(256), height=hist[0], align="center", width=0.5)
plt.show()