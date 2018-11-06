import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('res/PandaNoise.bmp', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = round(rows/2) , round(cols/2)
fshift[crow-40:crow+40, ccol-40:ccol+40] = 0; magnitude_spectrum = 20*np.log(np.abs(fshift))
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(magnitude_spectrum)
plt.title('Spectrum with HPF'), plt.xticks([]), plt.yticks([])

plt.show()

