import numpy as np
def adjustBrightness(img, value):
    """
    img: numpy array (grayscale 0-255)
    value: positive to brighten, negative to darken
    """
    result = img + value
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

#contrast adjustment concept
#idea: stretch pixel differences from the mean brightness
#new_pixel = mean + factor * (pixel - mean)
#factor > 1 → stronger contrast
#factor < 1 → weaker contrast

def adjustContrast(img,factor):
    
    mean = np.mean(img)
    result = mean + factor*(img-mean)
    result = np.clip(result,0,255) #keep pixel values safe
    return result.astype(np.uint8)