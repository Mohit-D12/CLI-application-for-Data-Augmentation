from PIL import Image
import torchvision.transforms as transforms
import random

# For uniformity, each Manager receives the image, list of params, and starting index from which it has to extract the parameters itself, and also return index for next property.
# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by using Translation as the property.
class TransalteManager:

    # This is prime function which gets called and it receives the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter for the next property.
    def augment(image, params, index):
        x_value = params[index]
        y_value = params[index + 1]
        next_index = index + 2      #example if crop is to be used next, the parameters of crop can be fetched starting at params[next_index], and therfore the code will be similar.
        updated_image = TransalteManager.augment_translate(image, x_value, y_value)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_translate(image, x_value, y_value):
        if x_value == 'x':
            x_value = TransalteManager.get_translate_x(image)
        if y_value == 'x':
            y_value = TransalteManager.get_translate_y(image)
            
        set_translation = transforms.RandomAffine(0, translate=(float(x_value), float(y_value)))
        return set_translation(image)

    # generates optimum values for params when 'x' is encountered (isn't final, currently it returns a demo value)
    def get_translate_x(image):
        DEFAULT_TRANSLATE_X = random.uniform(0.13, 0.25)
        return DEFAULT_TRANSLATE_X
    
    def get_translate_y(image):
        DEFAULT_TRANSLATE_Y = random.uniform(0.13, 0.25)
        return DEFAULT_TRANSLATE_Y
