from PIL import Image
from aquireImage import aquireImage
import time
import requests

def findColor(x1, y1, x2, y2, im):
    boundingBox = (x1,y1,x2,y2)         
    boundingRegion = im.crop(boundingBox)   
    boxX = x2 - x1
    boxY = y2 - y1
    
    #Initializing output
    totalColor = [0,0,0]

    #Iterate through each pixel and find its color
    for y in range(boxY):
        for x in range(boxX):
            pixelColor = boundingRegion.getpixel((x,y))

            #Iterate through R, G, and B value and add to output
            for i in totalColor:
                totalColor[i] = totalColor[i] + pixelColor[i]

    #Find RGB value throughout image
    totalPixels = boxX * boxY
    for i in totalColor:
        totalColor[i] = int(totalColor[i]/totalPixels)

    return (totalColor[0], totalColor[1], totalColor[2])


def calculateTowerColor():

    #Get the image and its path
    imagePath = aquireImage()

    if (imagePath == -1):
        raise Exception('Image path not found')

    im = Image.open(imagePath)

    #Bounding box for the base of the tower



calculateTowerColor()