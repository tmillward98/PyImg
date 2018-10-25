from PIL import Image

def calcCDF(count, greyArray):
    resultArray = [0] * 256
    for i in range(len(greyArray)):
        resultArray[i] = round((255 * (greyArray[i]) / count))
    return resultArray

def computeHistogram(pixelArray, count, resultArray):
    newArray = [0] * len(pixelArray)
    for i in range(len(pixelArray)):
        newArray[i] = round(255 * ((resultArray[pixelArray[i]] - resultArray[0]) / (count - resultArray[0])))
    return newArray

#Load the image
im = Image.open('PandaNoise.bmp')

#Load the pixel values into an array, determine the dimensions of the image
pixelArray = im.load()
width, height = im.size

#Setup an array for each grey value, L-1 (0-255)
greyLevels = [0]*256
cdfArray = [0] * (width * height)
pixelCount = width * height

#Next, we must collect the number of occurences of which each level of grey appears.
#for each instance of grey, plus 1
#Load the value of each pixel into an array

counter = 0
for x in range(width):
    for y in range(height):
        greyLevels[pixelArray[x, y]] +=1
        cdfArray[counter] = pixelArray[x, y]
        ++counter

histCDF = calcCDF(pixelCount, greyLevels)
histNew = computeHistogram(cdfArray, pixelCount, histCDF)

print(histNew)




