import numpy as np
from PIL import Image

'''
Constructs an RGB image whose values are the average of a series of images

@param array an (i x c x h x w) numpy array
       i is the image axis
       c is the color axis
       h is the height axis
       w is the width axis
@return a (c x h x w) array whose values are the average RGB values of the images in array
'''
def averageImage(array):
    #TO BE IMPLEMENTED
    
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

images = np.load('images.npy')
Image.fromarray(np.moveaxis(averageImage(images).astype(np.uint8),0,2)).save('avg.jpg')
grayscales = grayscaleImages(images)
Image.fromarray(grayscales[0].astype(np.uint8), 'L').save('pic1Grayscale.jpg')
Image.fromarray(grayscales[1].astype(np.uint8), 'L').save('pic2Grayscale.jpg')
Image.fromarray(grayscales[2].astype(np.uint8), 'L').save('pic3Grayscale.jpg')