import torch

from denoising_diffusion_pytorch import Unet, GaussianDiffusion,Trainer

model=Unet(
    dim=64,
    dim_mults= (1,2,4,8)
)

model= torch.load('./mnist_checkpoints/model-1.pt')

diffusion = GaussianDiffusion (
    model,
    image_size = 64,
    timesteps = 1000,
    sampling_timesteps = 250,
    loss_type = 'l1'
)

sampled_images = diffusion.sample(batch_size = 4)
sampled_images.shape