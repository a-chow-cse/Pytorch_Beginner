import os
import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image

def change_image(folder_name,desired_size):
    for f in os.scandir(folder_name):
        if f.is_file():
            im_pth = f.path

            im = Image.open(im_pth)
            print("previous= ",im.size)

            
            resz=transforms.Resize(((int((im.size[1]/im.size[0])*desired_size)),desired_size))

            im=resz(im)
            print("after resize= ",im.size)

            if (desired_size-im.size[0]) %2==1:
                left= int((desired_size-im.size[0]-1) /2)
                right= int((desired_size-im.size[0]+1) /2 )
            else:
                left=int((desired_size-im.size[0]) /2)
                right= int((desired_size-im.size[0]) /2)

            if (desired_size-im.size[1]) %2==1:
                up= int((desired_size-im.size[1]-1) /2)
                down= int((desired_size-im.size[1]+1) /2 )
            else:
                up=int((desired_size-im.size[1]) /2)
                down= int((desired_size-im.size[1]) /2)

            transform=transforms.Pad((left,up,right,down),255)


            im=transform(im)
            

            print(im.size)
            im.save(folder_name+f.name)
        else:
            change_image(f.path,desired_size)

folder_name="../../ddpm/ddpm_datasets/ThreeFromBoth/"

desired_size = 128

change_image(folder_name,desired_size)


