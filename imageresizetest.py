import os
import sys

from PIL import Image

def main():
    targetWidth = 1920
    targetHeight = 1080
    targetRatio = float(targetWidth) / targetHeight
    imagePil = Image.open('test.jpg')
    width, height = imagePil.size
    currentRatio = float(width) / height
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
    imageResize(targetSize, imagePil)
    return

def imageResize(targetSize, imagePil):
    imagePil.thumbnail(targetSize, Image.ANTIALIAS)
    imagePil.save('test.jpg')
    return

main()
    
raw_input('Press Enter to Exit')
