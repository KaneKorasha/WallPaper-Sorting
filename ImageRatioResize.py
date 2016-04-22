# This program will resize based on the dimensional ratio
# For my purposes the program will resize based on 1920x1080
# without making the width or height lower.
#
# This could be edited to fit other resolutions or to be interactive
# I am simply pulling from a directory during an automated cron job
# On a Debian Box.

import os
import sys

# I'm using Pillow, not PIL
from PIL import Image

def main():
    
    # This can be used in any directory as long as the script is called in that directory.
    directory = os.path.dirname(os.path.realpath('__file__'))
    retrieveFile(directory)

def retrieveFile(directory):
    for rawImage in os.listdir(directory):
        
        # Additional Image Extentions can be added here if Pillow supports them.
        if os.path.splitext(rawImage)[1].lower() in ('.jpg', '.jpeg', '.png'):
            rawImageSize = Image.open(rawImage)
            width, height = rawImageSize.size
            imageCalculator(width, height, rawImage, rawImageSize)
    return

def imageCalculator(width, height, rawImage, rawImageSize):
    
    # Have the current size here, but we need to have the end dimensions so we
    # Can resize the image
    targetSize = getNewDimensions(width, height)
    
    # Call the actual resize routine
    imageResize(targetSize, rawImageSize, rawImage)
        
def getNewDimensions(oldWidth, oldHeight, targetWidth=1920, targetHeight=1080):
    currentRatio = float(oldWidth) / oldHeight
    targetRatio = float(targetWidth) / targetHeight
    
    newDimensions = [targetWidth, targetHeight]

    if currentRatio > targetRatio:
        newDimensions[0] = int(targetHeight * currentRatio)
    elif currentRatio < targetRatio:
        newDimensions[1] = int(targetWidth / currentRatio)

    return newDimensions

def imageResize(targetSize, rawImageSize, rawImage):
    rawImageSize.thumbnail(targetSize, Image.ANTIALIAS)
    # Going to overwrite the source image
    rawImageSize.save(rawImage)
    return
    
main()
