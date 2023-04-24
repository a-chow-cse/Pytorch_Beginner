# Lime: My Edit
Please see following link for original implementation ([lime](https://github.com/marcotcr/lime/)). Below is the edit of the code that I am working on.

```
python start.py
```
- **input/** folder has the image for input of the program.
    - change in start.py line 15 with the relative path of image you want to try
- **output_original_segmentation/** folder has perturbed images with segmentation used in the original algorithm
- **img_boundary1.jpg** shows the part of the image that corresponds with the selected class label
- **img_boundary2.jpg** shows the part of the image that corresponds with the selected class label with green part, and the parts that negatively contribute to the class label with red color.
- **fudged_img.png** is the image of the same size of input, which will cover the segmented part that perturbed while classification.
## Technical things for me
- The code used pretrained inception model on imagenet
- main change or superpixels are generated in **lime_image.py** file.
    - There is a function **explain_instance()** which generates segments from a algorithm
    ```python
    if segmentation_fn is None:
            segmentation_fn = SegmentationAlgorithm('quickshift', kernel_size=4,
                                                    max_dist=200, ratio=0.2,
                                                    random_seed=random_seed)
    ```
    - you can also pass `segmentation_fn` in this function. Here is the work we have to do. 