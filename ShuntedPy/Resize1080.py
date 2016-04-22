import os
import sys

from PIL import Image

def main():
    directory = os.path.dirname(os.path.realpath('__file__'))
    retrieveFile(directory)

def retrieveFile(directory):
    for rawImage in os.listdir(directory):
        if os.path.splitext(rawImage)[1].lower() in ('.jpg', '.jpeg', '.png'):
            imagePil = Image.open(rawImage)
            width, height = imagePil.size
            imageCalculator(width, height, rawImage, imagePil)
    return

def imageCalculator(width, height, rawImage, imagePil):
    targetSize = getNewDimensions(width, height)
    
    imageResize(targetSize, imagePil, rawImage)
        
def getNewDimensions(oldWidth, oldHeight, targetWidth=1920, targetHeight=1080):
    currentRatio = float(oldWidth) / oldHeight
    targetRatio = float(targetWidth) / targetHeight

    newDimensions = [targetWidth, targetHeight]

    if currentRatio > targetRatio:
        newDimensions[0] = int(targetHeight * currentRatio)
    elif currentRatio < targetRatio:
        newDimensions[1] = int(targetWidth / currentRatio)

    return newDimensions

def imageResize(targetSize, imagePil, rawImage):
    imagePil.thumbnail(targetSize, Image.ANTIALIAS)
    imagePil.save(rawImage)
    return
    
main()