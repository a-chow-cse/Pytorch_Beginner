## **Virtual Environment**
- Needed for project isolation
- Install specific libary versions for project without globally changing those
- I prefer conda over pip
    - Most ML github projects use this, so it's easier to run
    - Easier to create environment

---
### **Environment.yml given**
Run the following commands:
```
conda env create -f environment.yml
```
To activate virtual environment:
``` 
source activate (environment->name)
```
In terminal,(environment name) will change if activated.
To deactivate:
```
conda deactivate
 ```
 ---

### **Create a new environment**
Go to the folder,
```
touch environment.yml
```
Write name of the virtual environment, and dependencies in the following manner,
```
name : project_name
dependencies:
    - numpy
    - scipy
    - ...
```
Now, do the [things as if environment.yml is given](#environmentyml-given)

### **Update Libraries in environment.yml**
deactivate current environment, then
```
conda env create -f environment.yml --force
```

### **Update Conda**
```
conda update -n base -c defaults conda
```
