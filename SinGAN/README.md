

# SinGAN
Source : https://tamarott.github.io/SinGAN.htm \
Some error has been fixed.

# Purpose of this work
I am exploring the original sinGAN repository to see if it specially the harmonization feature of sinGan can be used for classification purpose.

## Code

### **Install dependencies**

```
conda env create -f environment.yml
source activate singan
```

the code currently only supports torch 1.4 or earlier because of the optimization scheme.

### **Train**
To train SinGAN model on your own image, put the desired training image under Input/Images, and run

```
python main_train.py --input_name <input_file_name>
```
This will also use the resulting trained model to generate random samples starting from the coarsest scale (n=0).

To run this code on a cpu machine, specify `--not_cuda` when calling `main_train.py`

###  **Random samples**
To generate random samples from any starting generation scale, please first train SinGAN model on the desired image (as described above), then run 

```
python random_samples.py --input_name <training_image_file_name> --mode random_samples --gen_start_scale <generation start scale number>
```
`python random_samples.py --input_name butterfly.png --mode random_samples --gen_start_scale 4`
The outputs are in `Output/RandomeSamples/<image_name>` folder.

**pay attention:** for using the full model, specify the generation start scale to be 0, to start the generation from the second scale, specify it to be 1, and so on. As n is increased, the details of the image increases as well. You can see the highest value of n in `TrainedModels/` folder.


###  **Harmonization**

To harmonize a pasted object into an image , Go to this website,: https://www.remove.bg/  and remove background from the object and replace it with white (not transparent).

Then save the naively pasted reference image and it's binary mask under **"Input/Harmonization"** (see saved images for an example). To generate mask, go to Inputs/ folder, run `python3 generate_mask.py` (change the path to the current image in the code and run it without being in the virtual environment).

Now,Run the command,

```
python harmonization.py --input_name <training_image_file_name> --ref_name <naively_pasted_reference_image_file_name> --harmonization_start_scale <scale to inject>

```
Example: `python harmonization.py --input_name butterfly.png --ref_name mimic_butterfly.jpg --harmonization_start_scale 5`

Please note that different injection scale will produce different harmonization effects. The coarsest injection scale equals 1. as this increases you will have finer details of the reference image.

---
###  Animation from a single image

It can also generate short animation from a single image, Please see original link for this.

###  Editing

It can also edit image, Please see original link for this.

###  Paint to Image

It can also transfer a paint into a realistic image, Please see original link for this.


### Super Resolution
It can also transfer a image into a super resolution image, Please see original link for this.
