import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('PandaNoise.bmp', 0)
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)

for x in range(fshift):
    if fshift[x] > 1000:
        fshift[x] = 0

magnitude_spectrum = 20*np.log(np.abs(fshift))

cv2.imwrite('fft.png', magnitude_spectrum)

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()