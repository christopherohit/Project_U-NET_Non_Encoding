import cv2
import numpy as np


def diff_mask(ref_image, mask_image):
    mask_image_gray = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)

    mask = cv2.bitwise_and(mask_image, mask_image, mask = mask_image_gray)

    mask_coord = np.where(mask != [0,0,0])

    mask[mask_coord[0],mask_coord[1], :] = [255,0,0]

    ret = cv2.addWeighted(ref_image, 0.7, mask, 0.3, 0)
    return ret