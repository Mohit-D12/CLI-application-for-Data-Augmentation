from PIL import Image
import torchvision.transforms as transforms
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by using Contrast as the property.
class ContrastManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        contrast_value = params[index]
        next_index = index + 1
        updated_image = ContrastManager.augment_contrast(image, contrast_value)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_contrast(image, contrast_value):
        
        if contrast_value == 'x':
            contrast_value = ContrastManager.get_contrast_value(image)

        set_contrast = transforms.ColorJitter(contrast = float(contrast_value))
        return set_contrast(image)

    # generates optimum values for params when 'x' is encountered
    def get_contrast_value(image):
        DEFAULT_CONTRAST = random.uniform(0.25, 1)
        return DEFAULT_CONTRAST