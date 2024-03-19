# Object Detection on HSRID dataset using YOLOv8

## Dataset:

Original Link: https://github.com/chaozhong2010/HRSID <br>
Link to my split (70-30): https://drive.google.com/file/d/1O5O8UygEa-bsc9n6MyLFJHonaxhyzn8f/view?usp=sharing

-   The High-Resolution SAR Images Dataset (HRSID) contains 116 co-polarized and 20
    cross-polarized SAR imageries.
-   The original imageries for constructing HRSID are 99 Sentinel-1B imageries, 36
    TerraSAR-X and 1 TanDEM-X images.
-   The above 136 panoramic SAR imageries cropped to 5604 high-resolution SAR images.
-   These 5604 images have dimensions of 800 × 800 pixels, resolution of 96 dpi, and they
    are in .jpeg format.
-   The colour depth of the images is 8 bits (one channel).
-   The extracted 5604 high-resolution SAR images contain 16951 ship instances.
-   The spatial resolutions of SAR images are 0.5, 1 and 3 meters per pixel.
-   The annotations of each instance are the corresponding bounding box and the ship’s
    outline.
-   The annotations of each SAR image constitute a .json file in MS COCO dataset format.

This repository documents and contains my work on an internship qualification task by Suhora (https://suhora.com/).

Problem Statement: Detect ships in the given SAR Data. For the same you can design your own
model or use the current state-of-the-art object detection and/or segmentation model like
YOLOv8 / Segment Anything Model (SAM).

## Methodology:

Note: Here I've used Python 3.10.13.

1. Annotation and dataset inspection and study
2. Converted the MS COCO annotations to YOLO 1.1 format using traintest2017.json (available in the original dataset)
3. Created Train-Test splits and corresponding labelling (code to create it in fileops.ipynb, link shared above)
4. Imported YOLOv8
5. Tested functionality and execution time with 1 epoch runs and different hyperparameters.
6. Trained for 100 epochs, using hyperparameters as shown in main.ipynb.
7. Predicted on a random sample of 5 images from the val set of my train-test split.
8. Predicted on a random sample of 5 images from the pure_background folder of the original dataset.

## Results:

-   Final run data and metrics: runs\detect\train12
-   Model: runs\detect\train12\weights\best.onnx
-   Predictions for five randomly sampled images from the validation set: runs\detect\predict
-   Predictions for five randomly sampled images from the pure background dataset: runs\detect\predict2
