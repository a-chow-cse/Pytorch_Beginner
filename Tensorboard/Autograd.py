import torch
import torchvision
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
import os
import numpy as np

os.environ['TORCH_HOME'] = './'
if os.path.exists("./hub/checkpoints/resnet18-f37072fd.pth")== False:
    model =resnet18(weights=ResNet18_Weights.DEFAULT)
else:
    model= resnet18()
    model.load_state_dict(torch.load("./hub/checkpoints/resnet18-f37072fd.pth"))


from PIL import Image
img=Image.open("a.png")
img_crop=img.crop((100,100,164,164))
three_channel_img=img_crop.convert("RGB")

convert_to_tensor=transforms.ToTensor()
data=convert_to_tensor(three_channel_img)
data=data[None,:]

label= torch.rand(1,1000)

optimizer= torch.optim.SGD(model.parameters(),lr=0.02,momentum=0.9)

for i in range(100):
    prediction= model(data)
    loss=abs(prediction-label).sum()
    print(loss)
    model.zero_grad()
    loss.backward()
    optimizer.step()