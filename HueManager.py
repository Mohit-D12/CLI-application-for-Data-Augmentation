from PIL import Image
import torchvision.transforms as transforms
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by using hue as the property.
class HueManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        hue_value = params[index]
        next_index = index + 1
        updated_image = HueManager.augment_hue(image, hue_value)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_hue(image, hue_value):
        
        if hue_value == 'x':
            hue_value = HueManager.get_hue_value(image)

        set_hue = transforms.ColorJitter(hue = float(hue_value))
        return set_hue(image)

    # generates optimum values for params when 'x' is encountered
    def get_hue_value(image):
        DEFAULT_HUE = 0.15       #gets randomly selected between -0.15 to 0.15
        return DEFAULT_HUE