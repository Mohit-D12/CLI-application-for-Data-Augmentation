from PIL import Image
import torchvision.transforms as transforms
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by using Brightness as the property.
class BrightnessManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        brightness_value = params[index]
        next_index = index + 1
        updated_image = BrightnessManager.augment_brightness(image, brightness_value)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_brightness(image, brightness_value):
        
        if brightness_value == 'x':
            brightness_value = BrightnessManager.get_brightness_value(image)

        set_brightness = transforms.ColorJitter(brightness = float(brightness_value))
        return set_brightness(image)

    # generates optimum values for params when 'x' is encountered
    def get_brightness_value(image):
        DEFAULT_BRIGHTNESS = random.uniform(0.25, 1)
        return DEFAULT_BRIGHTNESS