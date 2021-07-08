from PIL import Image

# Data loader class has functions to load image from a path to a PILLOW Image and to save a PILLOW Image to an output path
class DataLoader:

    # image_loader loads and returns the image present at the image_directory into a pillow Image format
    def image_loader(image_directory):
        image = Image.open(image_directory)
        return image

    # image_extractor saves the image to the output_directory
    def image_extractor(image, output_directory):
        image.save(output_directory)
