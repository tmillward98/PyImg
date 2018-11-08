import numpy as np
import cv2 as cv

"""
For each pixel within an image, take a 9x9 grid of its neighbours. 
Sum the value of each pixel, and times by 1/9 (divide by 9)
This gives us the local neighbourhood smoothing algorithm
"""

def localBlur():
    img = cv.imread('altered/yeet.bmp', 0)  # Read the image
    local = cv.blur(img, (9, 9))
    cv.imwrite('localBlur.bmp', local)

"""
For each pixel within an image, go through and find the median from neighbouring pixels
Replace the current pixel with the median, repeat for each pixel
"""

def medianBlur():
    img = cv.imread('altered/yeet.bmp', 0)
    median = cv.medianBlur(img, 3)
    cv.imwrite('medianBlur.bmp', median)

