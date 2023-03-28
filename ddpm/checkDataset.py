# dataset classes
import math
import copy
from pathlib import Path
from random import random
from functools import partial
from collections import namedtuple
from multiprocessing import cpu_count

import torch
from torch import nn, einsum
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

from torch.optim import Adam

from torchvision import transforms as T, utils

from einops import rearrange, reduce, repeat
from einops.layers.torch import Rearrange

from PIL import Image
from tqdm.auto import tqdm
from ema_pytorch import EMA

from accelerate import Accelerator

from pytorch_fid.inception import InceptionV3
from pytorch_fid.fid_score import calculate_frechet_distance

from version import __version__

def exists(x):
    return x is not None
class SquarePad:
    def __call__(self, image):
        #print(image.size)
        max_wh = max(image.size)
        p_left, p_top = [(max_wh - s) // 2 for s in image.size]
        p_right, p_bottom = [max_wh - (s+pad) for s, pad in zip(image.size, [p_left, p_top])]
        padding = (p_left, p_top, p_right, p_bottom)
        convert_tensor = T.ToTensor()

        
        return F.pad(convert_tensor(image), padding,'constant')

class Dataset(Dataset):
    def __init__(
        self,
        folder,
        image_size,
        exts = ['jpg', 'jpeg', 'png', 'tiff'],
        augment_horizontal_flip = False,
        convert_image_to = None
    ):
        super().__init__()
        self.folder = folder
        self.image_size = image_size
        self.paths = [p for ext in exts for p in Path(f'{folder}').glob(f'**/*.{ext}')]

        maybe_convert_fn = partial(convert_image_to_fn, convert_image_to) if exists(convert_image_to) else nn.Identity()

        self.transform = T.Compose([
            SquarePad(),
            T.Lambda(maybe_convert_fn),
            T.Resize(image_size),
            #T.RandomHorizontalFlip() if augment_horizontal_flip else nn.Identity(),
            #T.ToTensor()
            #T.CenterCrop(image_size),
        ])

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, index):
        path = self.paths[index]
        img = Image.open(path)
        return self.transform(img)

ds = Dataset("./ddpm_datasets/ThreeFromBoth/", 128, augment_horizontal_flip = True, convert_image_to = None)
dl = DataLoader(ds, batch_size = 4, shuffle = True, pin_memory = True, num_workers = cpu_count())
for i in range(5):
    print(ds.__getitem__(i).shape)
    utils.save_image(ds.__getitem__(i), str('./samples/sample'+str(i)+'.png'))