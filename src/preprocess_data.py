

class Preprocess_Data():
    def adjust_data(img, mask):
        img = img / 255
        mask = mask / 255
        mask[mask > 0.5] = 1
        mask[mask <= 0.5] = 0

        return (img, mask)