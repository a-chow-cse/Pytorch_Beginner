## Multiple GPU
Use the following command to train the diffusion model on four gpus.\
```
CUDA_VISIBLE_DEVICES=0,1,2,3 python <file>
```

## In case of **torch.cuda.OutOfMemoryError: CUDA out of memory.**
Diffusion model training takes a lot of GPU compute. By default it may only want to use one GPU and it'll look at the first one (GPU 0). Does the code allow you to specify the GPU to use? Does it allow for multiple GPUs? \
You could also decrease the batch_size of the training, that would reduce the amount of GPU memory needed.\
It looks like the first two GPU are already at 80%-100%, so try using the other two GPUs. You could do this either in code or with the following command:
```
CUDA_VISIBLE_DEVICES=2,3 python [name of train script]
```
## Copy file to Remote Server
```
scp -r source destination
```
-r is for recursively copying all the files and folders from the source folder\
Source/destination can be local/remote
If you put '/' sign after folder name, it will copy all things within folder, not the folder itself.\
So if write `scp -r a_1 destination/`, you will have,
- a_1
    - b_1
        - c_1
        - c_2
    - b_2\

But, if you write, ` scp -r a_1/ destination/` , you will have,
- b_1
    - c_1
    - c_2
- b_2

## In case of binding error
```
RuntimeError: The server socket has failed to listen on any local network address. The server socket has failed to bind to [::]:29500 (errno: 98 - Address already in use). The server socket has failed to bind to 0.0.0.0:29500 (errno: 98 - Address already in use).
```
Run the following commands:
- `ps -fA | grep python`
- `kill -9 pid` (pid from the list generated above)
