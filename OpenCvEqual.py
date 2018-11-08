import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('medianBlur.bmp', 0)
equ = cv2.equalizeHist(img)

bin_count, bin_edges = np.histogram(img, bins=256)
bin_count1, bin_edges1 = np.histogram(equ, bins=256)

plt.subplot(121), plt.hist(bin_count, bin_edges, density=True, facecolor='g', alpha=0.75)
plt.xlabel('Grey Value')
plt.ylabel('Intensity')
plt.subplot(122), plt.hist(bin_count1, bin_edges1, density=True, facecolor='g', alpha=0.75)
plt.xlabel('Grey Value')
plt.ylabel('Intensity')
plt.show()


cv2.imwrite('equalisedImage.bmp', equ)