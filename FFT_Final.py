import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
The function is passed the size of the image and the array itself
From this, choose the size of the area you wish to keep and which parts you want to filter out
Apply the transformation function on the image, returning the result
"""

def lowpassFilter(irows, icols, imgarray):
    huv = np.zeros(shape=(irows, icols))
    x = round(irows/3)
    y = round(icols/3)
    x2 = round(irows - x)
    y2 = round(icols - y)

    for temp in range(x, x2):
        for temp1 in range (y, y2):
            huv[temp, temp1] = 1

    imgarray = imgarray * huv
    return imgarray

img = cv.imread('res/PandaNoise.bmp', 0) #Read in the image
f = np.fft.fft2(img) #Perform the FFT transformation
fshift = np.fft.fftshift(f) #Reorder the data such that zero values are centred
magnitude_spectrum = 20*np.log(np.abs(fshift)) #Convert from complex numbers
cv.imwrite('originalspectrum.bmp', magnitude_spectrum) #Write as image


rows, cols = img.shape
crow, ccol = round(rows/2) , round(cols/2)
#fshift[crow-rows:crow+rows, ccol-100:ccol+100] = 0;


fshift = lowpassFilter(rows, cols, fshift)

magnitude_spectrum = 20*np.log(np.abs(fshift))
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
cv.imwrite('yeet.bmp', img_back)
cv.imwrite('lowpassspectrum.bmp', magnitude_spectrum)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(magnitude_spectrum)
plt.title('Spectrum with HPF'), plt.xticks([]), plt.yticks([])

plt.show()