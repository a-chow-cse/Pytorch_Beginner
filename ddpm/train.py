#ddpm from https://github.com/lucidrains/denoising-diffusion-pytorch
import torch

from denoising_diffusion_pytorch import Unet, GaussianDiffusion,Trainer

model=Unet(
    dim=64,
    dim_mults= (1,2,4,8)
)

diffusion = GaussianDiffusion (
    model,
    image_size = 128,
    timesteps = 1000,
    sampling_timesteps = 250,
    loss_type = 'l1'
)

trainer = Trainer(
    diffusion,
    './ddpm_datasets/ThreeFromBoth/',
    train_batch_size= 3,
    train_lr = 1e-4,
    train_num_steps = 10000,
    gradient_accumulate_every = 2,
    save_and_sample_every=100,
    ema_decay = 0.995,
    amp = False,
    fp16=True,
    calculate_fid = True
)
#trainer.load(44)

trainer.train()


        