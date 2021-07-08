from PaddingManager import PaddingManager
from GrayscaleManager import GrayscaleManager
from CropManager import CropManager
from SaturationManager import SaturationManager
from HueManager import HueManager
from ContrastManager import ContrastManager
from BrightnessManager import BrightnessManager
from TraslateManager import TransalteManager
from PIL import Image
import torchvision.transforms as transforms #pytorch
from sys import argv
import os
import random

class ImageAugmentor:
        global ALL_PROPERTIES, ALL_PARAMS, map_to_function
        
        ALL_PROPERTIES = ['brightness', 'contrast', 'hue', 'grayscale', 'saturation',  'crop', 'padding', 'translate']
        ALL_PARAMS = ['x'] * 30
        map_to_function = {
                'brightness':   BrightnessManager.augment, 
                'contrast':     ContrastManager.augment, 
                'hue':          HueManager.augment, 
                'grayscale':    GrayscaleManager.augment, 
                'saturation':   SaturationManager.augment, 
                'crop':         CropManager.augment, 
                'padding':      PaddingManager.augment, 
                'translate':    TransalteManager.augment
        }

        def augment(image, properties = ALL_PROPERTIES, params = ALL_PARAMS):
                index = 0
                updated_image = image

                if properties == None:
                        properties = ALL_PROPERTIES
                else:
                        properties = properties[0]
                        
                if params == None:
                        params = ALL_PARAMS
                else:
                        params = params[0]
                
                #print(properties, params)
                #print(properties)
                for i in properties:
                        #print("tag", i)
                        updated_image, index = map_to_function[i](updated_image, params, index)
                
                return updated_image




        
