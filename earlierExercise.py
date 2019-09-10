import numpy as np
from PIL import Image
    
'''
Converts a series of RGB images to a series of grayscale images

@param array an (i x c x h x w) numpy array
       i is the image axis
       c is the color axis
       h is the height axis
       w is the width axis
@return an (i x h x w) array of grayscale images
'''
def grayscaleImages(array):
    #TO BE IMPLEMENTED


'''
Converts a series of RGB images to a series of luminosity-map images based on given weights

@param array an (i x c x h x w) numpy array
       i is the image axis
       c is the color axis
       h is the height axis
       w is the width axis
@param r the weight the first channel should have on the luminosity
@param g the weight the second channel should have on the luminosity
@param b the weight the third channel should have on the luminosity
@return a (i x h x w) array whose values are the weighted average of the red, green, and blue channel values
'''
def luminosityImages(array, r, g, b):
    #TO BE IMPLEMENTED

images = np.load('images.npy')
grayscales = grayscaleImages(images)
Image.fromarray(grayscales[0].astype(np.uint8), 'L').save('pic1Grayscale.jpg')
Image.fromarray(grayscales[1].astype(np.uint8), 'L').save('pic2Grayscale.jpg')
Image.fromarray(grayscales[2].astype(np.uint8), 'L').save('pic3Grayscale.jpg')
luminosities = luminosityImages(images,1,1,1)
Image.fromarray(luminosities[0].astype(np.uint8), 'L').save('pic1Luminosity.jpg')
Image.fromarray(luminosities[1].astype(np.uint8), 'L').save('pic2Luminosity.jpg')
Image.fromarray(luminosities[2].astype(np.uint8), 'L').save('pic3Luminosity.jpg')