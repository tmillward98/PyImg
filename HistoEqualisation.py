from PIL import Image, ImageFilter
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Start by loading the image
equalImage = cv2.imread('PandaNoise.bmp', 0)

#Flattens the array into a 1 dimensional array
hist,bins = np.histogram(equalImage.flatten(), 256, [0, 256])

#Calculate, then normalise the CDF
cdf = hist.cumsum()
cdf_normalised = cdf * hist.max()/cdf.max()

plt.plot(cdf_normalised, color = 'b')
plt.hist(equalImage.flatten(), 256, [0, 256], color='r')
plt.xlim([0,256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

