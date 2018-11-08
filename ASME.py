import numpy as np
import cv2 as cv

"""
Read in the two images you want to compare
Subtract the value of each pixel from the other, and sum by difference^2
Divide by the total number of pixels to find the ASME
"""

img1 = cv.imread('res/PandaOriginal.bmp', 0)
img2 = cv.imread('altered/medianBlur.bmp', 0)

width, height = img1.shape
sum = 0

for x in range(width):
    for y in range(height):
        difference = (img1[x, y] - img2[x, y])
        sum = sum + (difference*difference)

mse = round(sum / (width * height), 3)
print(mse)