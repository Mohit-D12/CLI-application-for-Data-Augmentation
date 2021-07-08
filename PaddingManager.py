from PIL import Image
import torchvision.transforms as transforms
import random

# This class contains tools for
# a. Extracting the required number of parameters from the list of parameters passed.
# b. Generating the optimum value in case above parameter is 'x'.
# c. Augmenting the image by adding padding to the image.
class PaddingManager:

    # main function which gets the pillow image, list of parameters and index of first parameter for current property.
    # it returns a tuple of the updated image and index of first parameter of the next property.
    def augment(image, params, index):
        padding_left = params[index]
        padding_top = params[index+1]
        padding_right = params[index+2]
        padding_bottom = params[index+3]
        next_index = index + 4
        updated_image = PaddingManager.augment_padding(image, padding_left, padding_top, padding_right, padding_bottom)
        return (updated_image, next_index)

    #augments image and returns the updated image
    def augment_padding(image, padding_left, padding_top, padding_right, padding_bottom):
        
        if padding_left == 'x':
            padding_left = PaddingManager.get_padding_left(image)
        if padding_top == 'x':
            padding_top = PaddingManager.get_padding_top(image)
        if padding_right == 'x':
            padding_right = PaddingManager.get_padding_right(image)
        if padding_bottom == 'x':
            padding_bottom = PaddingManager.get_padding_bottom(image)
            
        set_padding = transforms.Pad((int(padding_left), int(padding_top), int(padding_right), int(padding_bottom)))
        return set_padding(image)

    # generates optimum values for params when 'x' is encountered
    def get_padding_left(image):
        DEFAULT_PADDING_LEFT = random.randint(0, 10)
        return DEFAULT_PADDING_LEFT
    
    def get_padding_top(image):
        DEFAULT_PADDING_TOP = random.randint(0, 10)
        return DEFAULT_PADDING_TOP
    
    def get_padding_right(image):
        DEFAULT_PADDING_RIGHT = random.randint(0, 10)
        return DEFAULT_PADDING_RIGHT
    
    def get_padding_bottom(image):
        DEFAULT_PADDING_BOTTOM = random.randint(0, 10)
        return DEFAULT_PADDING_BOTTOM
    