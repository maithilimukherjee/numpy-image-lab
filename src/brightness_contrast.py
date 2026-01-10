import numpy as np
def adjustBrightness(img, value):
    """
    img: numpy array (grayscale 0-255)
    value: positive to brighten, negative to darken
    """
    result = img + value
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)
