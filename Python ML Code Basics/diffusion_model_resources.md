### Pretrained Diffusion Models

- https://github.com/VSehwag/minimal-diffusion 
    - contains 10 pre-trained model with classifier, accuracy, images and scripts
    - probably not ddpm?
    - Datasets: MNIST, MNIST-M, CIFAR-10, Skin Cancer, AFHQ, CelebA, Standford Cars, Oxford Flowers, Traffic signs

### Official DDPM Paper pretrained models
- https://github.com/hojonathanho/diffusion 
    - Cifar-10, lsun, CelebHQ
    - https://www.dropbox.com/sh/pm6tn31da21yrx4/AABWKZnBzIROmDjGxpB6vn6Ja?dl=0 

### All The resources for Diffusion:
- Good Blog : https://aman.ai/primers/ai/diffusion-models/

### For ButterFly Training:
- I used code from here
- Must do the following for not generating black photos:
    - in Terminal `set COMMANDLINE_ARGS=--lowvram --precision full --no-half`
    - make `fp16= True` in Trainer class
    - turn off mixed precision by `amp=False`



