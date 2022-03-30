import cv2
import numpy as np

class Add_color():
    def add_colored_dilate(image, mask_image, dilate_image):
        mask_image_gray = cv2.cvtColor(mask_image,cv2.COLOR_BGR2GRAY)
        dilate_image_gray = cv2.cvtColor(dilate_image, cv2.COLOR_BGR2GRAY)

        mask = cv2.bitwise_and(mask_image, mask_image, mask = mask_image_gray)
        dilate = cv2.bitwise_and(dilate_image, dilate_image, mask = dilate_image_gray)

        mask_coord = np.where(mask != [0,0,0])
        dilate_coord = np.where(dilate != [0,0,0])

        mask[mask_coord[0], mask_coord[1], :] = [255,0,0]

        dilate[dilate_coord[0], dilate_coord[1], :] = [0,0,255]

        ret = cv2.addWeighted(image,0.7,dilate,0.3,0)
        ret = cv2.addWeighted(ret,0.7,mask,0.3,0)

        return ret

    def add_colored_mask(image, mask_image):
        mask_image_gray = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)

        mask = cv2.bitwise_and(mask_image, mask_image, mask = mask_image_gray)

        mask_coord = np.where(mask != [0,0,0])
        mask[mask_coord[0], mask_coord[1], :] = [255,0,0]

        ret = cv2.addWeighted(image, 0.7, mask, 0.3, 0)
        return ret