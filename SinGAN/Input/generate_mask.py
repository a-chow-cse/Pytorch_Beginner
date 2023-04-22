#This will remove background and generate a mask of the object in the image
#Remove background from here: https://www.remove.bg/ and remember to background white, not transparent
#Author : Arpita

import cv2
import numpy as np
from PIL import Image
import os


def convert_to_jpg(path):
    png_image = Image.open(path)

    # Convert to RGB if necessary
    if png_image.mode != 'RGB':
        png_image = png_image.convert('RGB')

    # Save as JPG with high quality
    path=os.path.dirname(path)+"/"+os.path.splitext(os.path.basename(path))[0]+".jpg"
    png_image.save(path, quality=100)
    create_mask(path)

def create_mask(path):
    img = cv2.imread(path)
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Create a binary mask where white pixels in the original image are black and all other pixels are white
    mask = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)[1]
    mask = np.stack((mask,) * 3, axis=-1)
    newName= os.path.dirname(path)+"/"+os.path.splitext(os.path.basename(path))[0]+"_mask.jpg"
    cv2.imwrite(newName,mask)

def check_channels_in_mask():
    img=cv2.imread(os.path.dirname(path)+"/"+os.path.splitext(os.path.basename(path))[0]+"_mask.jpg")
    print(img.shape)
    channels = cv2.split(img)
    cv2.imwrite("r.png",channels[0])
    cv2.imwrite("g.png",channels[1])
    cv2.imwrite("b.png",channels[2])

# Open the PNG image
n_path='./Harmonization/another_butterfly.png'
convert_to_jpg(n_path)
