import os
import sys

from PIL import Image

targetWidth = 1920
targetHeight = 1080
targetRatio = float(targetWidth) / targetHeight
print targetRatio

imagePil = Image.open('test.png')
width, height = imagePil.size
currentRatio = float(width) / height
print width, height, currentRatio

if currentRatio == targetRatio:
    targetSize = 1920, 1080
    imagePil.thumbnail(targetSize, Image.ANTIALIAS)
    imagePil.save('test2.png')
else:
    print 'well shit.'

raw_input('Press Enter to Exit')
