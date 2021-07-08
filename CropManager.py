from PIL import Image
import torchvision.transforms as transforms
from torchvision.transforms.functional import crop
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by Centre Cropping.
class CropManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        crop_value = params[index]
        next_index = index + 1
        updated_image = CropManager.augment_centre_crop(image, crop_value)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_centre_crop(image, crop_value):
        if crop_value == 'x':
            crop_value = CropManager.get_crop_value(image)
        set_centre_crop = transforms.CenterCrop(float(crop_value))
        return set_centre_crop(image)

    # generates optimum values for params when 'x' is encountered
    def get_crop_value(image):
        CROP_VALUE_LOW, CROP_VALUE_HIGH = 550, 1000
        CROP_VALUE = random.randint(CROP_VALUE_LOW, CROP_VALUE_HIGH)
        return CROP_VALUE
