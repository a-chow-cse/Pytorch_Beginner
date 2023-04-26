import numpy as np
import torch
import os
import cv2
import matplotlib.pyplot as plt
import sys
sys.path.append('./segment_anything')
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor

input_path="./input/dogs.png"
output_path="./output/"

def show_masked_parts(image, anns, output_path):
    show_all_masks(image, anns, output_path)
    if len(anns) == 0:
        return
    output_path=output_path+os.path.splitext(os.path.basename(input_path))[0]+"/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    print(output_path)

    sorted_anns = sorted(anns, key=lambda x: x['area'], reverse=True)
    for maskN in range(len(sorted_anns)):
        m = sorted_anns[maskN]['segmentation']
        # Extract masked region from original image
        masked_img = np.ones_like(image)*255
        masked_img[m] = image[m]
        path = output_path + str(maskN) + ".png"
        plt.imshow(masked_img)
        plt.savefig(path)
def show_all_masks(image, anns, output_path):
    if len(anns) == 0:
        return
    output_path=output_path+os.path.splitext(os.path.basename(input_path))[0]+"/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_path=output_path+"all.png"
    print(output_path)

    plt.imshow(image)

    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
        ax.imshow(np.dstack((img, m*0.35)))
    plt.axis("off")
    plt.savefig(output_path)

def show_masks_as_black(image,anns,output_path): ##for lime
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)

    output_path=output_path+os.path.splitext(os.path.basename(input_path))[0]+"_lime/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    print(output_path)

    for maskN in range(len(sorted_anns)):
        m = sorted_anns[maskN]['segmentation']
        reversed_mask = np.logical_not(m)
        # blacken masked region from original image
        masked_img = np.zeros_like(image)
        masked_img[reversed_mask] = image[reversed_mask]
        path = output_path + str(maskN) + ".png"
        plt.imshow(masked_img)
        plt.axis("off")
        plt.savefig(path)

image=cv2.imread(input_path)
image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

sam_checkpoint="sam_vit_h_4b8939.pth"
model_type="vit_h"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

sam=sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)

masks=mask_generator.generate(image)

print(len(masks))
print(masks[0].keys())


show_masks_as_black(image,masks,output_path)
#show_masked_parts(image,masks,output_path)