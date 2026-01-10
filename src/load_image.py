#load and display the image

import numpy as np
from PIL import Image #PIL image object : wrapper around the image data
import matplotlib.pyplot as plt

def load_image(path):
    img = Image.open(path)
    return np.array(img) 

#np.array converts the PIL image into a numpy array where each pixel is now a number
#each pixel is now a number (0-255)
#shape depends on image type: hw for grayscale, hw3 for rgb and hw4 for rgba
#main.py can manipulate pixels directly using numpy

def show_image(img, cmap=None):
    
    plt.imshow(img, cmap=cmap) #shows image
    plt.axis("off") #hides the axes
    plt.show() #actually renders the plot