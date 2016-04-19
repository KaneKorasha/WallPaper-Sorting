import os.path, shutil
import get_image_size

def main():
    # Set directory to the picture source. This will eventually be 
    # /home/aito/MainStorage/BTBox/Photos/PaperDump as it
    # will be running on an Debian Server
    # Rewrote to be pulled directly.
    directory = os.path.dirname(os.path.realpath(__file__))
    retrieveFile(directory)

def retrieveFile(directory):
    for rawImage in os.listdir(directory):
        if os.path.splitext(rawImage)[1].lower() in ('.jpg', '.jpeg', '.png'):
            # REMEMBER TO ASSIGN A CALL TO A VARIABLE YOU IDIOT
            width, height = imageFetchDimension(rawImage)
            imageSort(rawImage, width, height)
    return

# This module calls get_image_size to pull dimensions
def imageFetchDimension(rawImage):
    try:
        width, height = get_image_size.get_image_size(rawImage)
    except get_image_size.UnknownImageFormat:
        width, height = -1, -1
    return width, height

def imageSort(rawImage, width, height):
    #move files or remove files I really don't have to play with
    if width == 1920 and height == 1080:
        #print rawImage, 'does not need to be resized, moving to 1920x1080'
        dest = '1920x1080'
        imageMove(rawImage, dest)
    elif width == 1366 and height == 768:
        #print rawImage, 'does not need to be resized, moving to 1366x768'
        dest = '1366x768'
        imageMove(rawImage, dest)
    elif width < 1366 or height < 768:
        #print rawImage, 'is too small, deleting.'
        os.remove(rawImage)
    # sort remaining files based on size
    elif width >= 1920 and height >= 1080:
        #print rawImage, 'is larger than 1920x1080, moving to 1920x1080Resize'
        dest = '1920x1080Resize'
        imageMove(rawImage, dest)
    elif width >= 1366 and height >= 768:
        #print rawImage, 'is larger than 1366x768, moving to 1366x768Resize'
        dest = '1366x768Resize'
        imageMove(rawImage, dest)
    else:
        print rawImage, 'has a problem'
    return

def imageMove(rawImage, dest):
    shutil.move(rawImage, dest)
    return
    
main()

raw_input('Press Enter to Exit')
