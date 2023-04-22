#This will remove background and generate a mask of the object in the image
#Author : Arpita

import cv2
import numpy as np
from PIL import Image
import os

# Open the PNG image
path='./Harmonization/mimic_butterfly.jpg'

def convert_to_jpg():
    png_image = Image.open(path)

    # Convert to RGB if necessary
    if png_image.mode != 'RGB':
        png_image = png_image.convert('RGB')

    # Save as JPG with high quality
    png_image.save(path, quality=100)

def create_mask():
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

#check_channels_in_mask()
img = cv2.imread('./Harmonization/mimic_butterfly.jpg')
print(img.shape)
