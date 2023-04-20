## PIL Image to tensor data
If the image is in png form, the PIL Image would have 4 channels. The 4th channel is transparency channel for pixels that are transparent in png image. 
In neural models, in most cases, we need 3 channel Image, RGB. 
### Convert RGBA img to RGB img
```python
from PIL import Image

_rgba_img=Image.open("path to image")  #(h,w,ch)=(h,w,4)
_rgb_img=_rgba_img.convert("RGB") #(h,w,ch)=(h,w,3)
```

 Below is the way to convert rgb PIL Image to tensor:
 ```python
    from torchvision import transforms

    convert_to_tensor=transforms.ToTensor() #operator for transforming
    data=convert_to_tensor(_rgb_img) # shape=(ch,h,w)
    print(data.size())
```

## Add Dimension to tensor
```python
import torch

data=torch.zeros(5) 
#tensor([ 0.,  0.,  0.,  0.,  0.]) size=([5])

data_1=data[None,:]
#tensor([[ 0.,  0.,  0.,  0.,  0.]]) size=([1,5])

data_2=data[None,None,:]
#tensor([[[ 0.,  0.,  0.,  0.,  0.]]]) size=([1,1,5])

```

### Finetune: Freeze parameters 
```python
from torch import nn, optim

model=resnet18(weights=ResNet18_Weights.DEFAULT)

for param in model.parameters():
    param.requires_grad= False

#change last layer of model
model.fc = nn.linear(512,10)
# a new layer is unfrozen by default
```

## Components of a Neural Network
- Define model class
- Process Input according to model
- Define Loss Function
- Define optimizer
- Initialize model
- Create a loop for training
    - give input x to model to get prediction
    - use the defined loss function to loss
    - do model.zero_grad() to zero the gradient
    - loss.backward() to calculate grad
    - optimizer.step() to update the parameters

## Load Pretrained Model
- create or initialize a model architecture same as pretrained model.
- load the model
```python
state_dict = torch.load(path/to/model)
```
- When you call `torch.load()` on a file which contains GPU tensors, those tensors will be loaded to GPU by default. 
 - You can call `torch.load(.., map_location='cpu')` if you want to use cpu. 
 - You can also specify the gpu you want to use by `torch.load(.., map_location=lambda storage, loc: storage.cuda(1)`