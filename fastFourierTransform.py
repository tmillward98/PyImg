import numpy as np
import matplotlib as plt
import random
from PIL import Image

#The forward discrete fourier transformation is defined by
#SIGMA N-1: xn * e^-i2pikn/N

def fast_dft(x):
    x = np.asarray(x, dtype=float) #Load each pixel into an array
    N = x.shape[0] #Returns size of Array
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)

im = Image.open('PandaNoise.bmp')