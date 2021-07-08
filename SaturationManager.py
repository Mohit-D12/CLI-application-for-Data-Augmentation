from PIL import Image
import torchvision.transforms as transforms
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by using Saturation as the property.
class SaturationManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        saturation_value = params[index]
        next_index = index + 1
        updated_image = SaturationManager.augment_saturation(image, saturation_value)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_saturation(image, saturation_value):
        
        if saturation_value == 'x':
            saturation_value = SaturationManager.get_saturation_value(image)

        set_saturation = transforms.ColorJitter(saturation = float(saturation_value))
        return set_saturation(image)

    # generates optimum values for params when 'x' is encountered
    def get_saturation_value(image):
        DEFAULT_SATURATION = random.uniform(0.25, 1)
        return DEFAULT_SATURATION