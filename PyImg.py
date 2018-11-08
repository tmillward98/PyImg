import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def FFT_Transform(img):
    f = np.fft.fft2(img)  # Perform the FFT transformation
    fshift = np.fft.fftshift(f)  # Reorder the data such that zero values are centred
    magnitude_spectrum = 20 * np.log(np.abs(fshift))  # Convert from complex numbers
    cv.imwrite('originalspectrum.bmp', magnitude_spectrum)  # Write as image
    return magnitude_spectrum

def FFT_Inverse(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    cv.imwrite('Inverse.bmp', img_back)
    return img_back

"""
This function is completely dependent on the two images being the exact same size, else out of bounds
The function is passed the spectrum of the image, then removes the given area
In this particular use case, it removes the area on the outside of the image, preserving only the centre
Namely, 2/3rds of the image around the outside.
"""
def lowpassFilter(imgarray):
    irows, icols = imgarray.shape
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

"""
For each pixel within an image, take a 9x9 grid of its neighbours. 
Sum the value of each pixel, and times by 1/9 (divide by 9)
This gives us the local neighbourhood smoothing algorithm
"""
def localBlur(img):
    local = cv.blur(img, (3, 3))
    cv.imwrite('LocalBlur.bmp', local)
    return local

"""
For each pixel within an image, go through and find the median from neighbouring pixels
Replace the current pixel with the median, repeat for each pixel
"""
def medianBlur(img):
    median = cv.medianBlur(img, 3)
    cv.imwrite('MedianBlur.bmp', median)
    return median

"""
Subtracts a sharp mask from the image it is given
Kernel is predefined
"""
def sharpenImage(img):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    im = cv.filter2D(img, -1, kernel)
    cv.imwrite('SharpImage_1.bmp', im)
    return im

"""
Self explanatory function, simply plots whatever image is passed to it
"""
def PlotSpectrum(magnitude_spectrum):
    plt.imshow(magnitude_spectrum, cmap= 'gray')
    plt.title('Fourier Domain Spectrum')
    plt.show()

"""
Read in the two images you want to compare
Subtract the value of each pixel from the other, and sum by difference^2
Divide by the total number of pixels to find the ASME
"""
def CalcAMSE(img1, img2):
    width, height = img1.shape

    sum = int(0)
    difference = int(0)

    for x in range(width):
        for y in range(height):
            difference = (img1[x, y]) - (img2[x, y])
            print("D: ", difference)
            sum = sum + (difference * difference)
            print("S:", sum)

    mse = round(sum / (width * height), 3)
    print(mse)