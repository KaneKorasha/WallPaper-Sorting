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
    targetWidth = 1920
    targetHeight = 1080
    currentRatio = float(width) / height
    targetRatio = float(targetWidth) / targetHeight
    if currentRatio == targetRatio:
        targetSize = targetWidth, targetHeight
    elif currentRatio > targetRatio:
        newWidth = int(targetHeight * currentRatio)
        targetSize = newWidth, targetHeight
    elif currentRatio < targetRatio:
        newHeight = int(targetWidth / currentRatio)
        targetSize = targetWidth, newHeight
    else:
        print 'well shit.'
    
    imageResize(targetSize, imagePil, rawImage)
    
    return
        
def imageResize(targetSize, imagePil, rawImage):
    imagePil.thumbnail(targetSize, Image.ANTIALIAS)
    imagePil.save(rawImage)
    return
    
main()

raw_input('Press Enter to Exit')
