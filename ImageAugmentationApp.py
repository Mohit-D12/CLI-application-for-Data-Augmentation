from ImageAugmentor import ImageAugmentor
from DataLoader import DataLoader
from InputReader import InputReader
import torchvision.transforms as transforms #pytorch
import argparse
import os

class ImageAugmentation:
    def init():
        args = []

        parser = argparse.ArgumentParser()
        parser.add_argument('-input', action='store', type=str)
        parser.add_argument('-o', action='store', type=str)
        parser.add_argument('-n', action='store', type=int)
        parser.add_argument('-p', nargs="+", action="append", type=str)
        parser.add_argument('-l', nargs="+", action="append", type=str)
        args = parser.parse_args()
        return args

    if __name__ == "__main__":
        #read terminal input
        args = init()
        #print(InputReader.readInput(args))
        image_path, extension, output_path, number_of_outputs, properties, parameters = InputReader.readInput(args)

        #load image to pillow object
        image =  DataLoader.image_loader(image_path)

        for i in range(1, number_of_outputs+1):
            
            #augment image
            updated_image = ImageAugmentor.augment(image, properties, parameters)

            #save image to output path
            if output_path == None:
                output_path = image_path

            output_path = output_path.split('.')[0]
            current_output_path = output_path + str(i) + "." + extension
            DataLoader.image_extractor(updated_image,current_output_path)

#format: python ImageAugmentationApp.py -input image_path -o output_path -n number_of_output -p properties(space seperated) -l parameters(space seperated)
# only compulsory till image_path
# & C:/Users/dharm/AppData/Local/Programs/Python/Python39/python.exe c:/Users/dharm/OneDrive/Documents/Workspace/PS1/OOP_Augmentor/ImageAugmentationApp.py -input "C:\Users\dharm\OneDrive\Documents\Workspace\PS1\OOP_Augmentor\dog.jpg" -n 1 -p crop hue -l 500 0.5

#number of input works fine
#params and properties works fine

# & C:/Users/dharm/AppData/Local/Programs/Python/Python39/python.exe c:/Users/dharm/OneDrive/Documents/Workspace/PS1/OOP_Augmentor/ImageAugmentationApp.py -input "C:\Users\dharm\OneDrive\Documents\Workspace\PS1\OOP_Augmentor\Images\dog.jpg" -n 1 -p brightness crop -l 1 600