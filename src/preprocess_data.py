from logging import NullHandler
import os
from tkinter import filedialog
from tkinter import *




class Preprocess_Data():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    def create_dir(folder_selected):
        
        try:
            isExist = os.path.exists(folder_selected)
            if not isExist:
                os.makedirs(folder_selected)
                print("The new directory is created!")
            else:
                print("It's Exist")
        except(Exception):
            return 'Error'
            
    def adjust_data(img, mask):
        img = img / 255
        mask = mask / 255
        mask[mask > 0.5] = 1
        mask[mask <= 0.5] = 0

        return (img, mask)
    
    def Join_path(folder_selected):
        INPUT_DIR = os.path.join('/content/gdrive/MyDrive/Dataset/CT Lung','src')
        IMAGE_DIR = os.path.join('/content/gdrive/MyDrive/Dataset','CT Lung')
        SEGMENTATION_DIR = os.path.join(INPUT_DIR, 'segmentation')
        SEGMENTATION_TEST_DIR = os.path.join(SEGMENTATION_DIR, 'test')
        SEGMENTATION_TRAIN_DIR = os.path.join(SEGMENTATION_DIR, 'train')
        SEGMENTATION_AUG_DIR = os.path.join(SEGMENTATION_TRAIN_DIR, 'augmentation')
        SEGMENTATION_IMAGE_DIR = os.path.join(SEGMENTATION_TRAIN_DIR, 'image')
        SEGMENTATION_MASK_DIR = os.path.join(SEGMENTATION_TRAIN_DIR, 'mask')
        SEGMENTATION_DILATE_DIR = os.path.join(SEGMENTATION_TRAIN_DIR, 'dilate')

        SHENZEN_TRAIN_DIR = os.path.join(IMAGE_DIR, 'ChinaSet_AllFiles')


        SHENZHEN_IMAGE_DIR = os.path.join(SHENZEN_TRAIN_DIR, "CXR_png")
        SHENZHEN_MASK_DIR = os.path.join(IMAGE_DIR,"mask", "mask")

        MONTGOMERY_TRAIN_DIR = os.path.join(IMAGE_DIR, "Montgomery", "MontgomerySet")
        MONTGOMERY_IMAGE_DIR = os.path.join(MONTGOMERY_TRAIN_DIR, "CXR_png")
        MONTGOMERY_LEFT_MASK_DIR = os.path.join(MONTGOMERY_TRAIN_DIR, "ManualMask", "leftMask")
        MONTGOMERY_RIGHT_MASK_DIR = os.path.join(MONTGOMERY_TRAIN_DIR,"ManualMask", "rightMask")

        DILATE_KERNEL = np.ones((15, 15), np.uint8)