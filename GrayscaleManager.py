from PIL import Image
import torchvision.transforms as transforms
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by Grayscaling the image.
class GrayscaleManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        probability = params[index]
        next_index = index + 1
        updated_image = image

        if probability == 'x':
            probability = GrayscaleManager.get_probability()
        
        if random.uniform(0, 1) < float(probability):
            updated_image = GrayscaleManager.augment_grayscale(image)

        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_grayscale(image):
        set_grayscale = transforms.Grayscale()
        return set_grayscale(image)

    # generates optimum values for params when 'x' is encountered
    def get_probability():
        DEFAULT_PROBABILITY = 0.16
        return DEFAULT_PROBABILITY