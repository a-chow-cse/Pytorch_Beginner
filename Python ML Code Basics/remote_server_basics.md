### Copy file to Remote Server
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