import numpy as np

def blur_image_vectorized(img):
    """
    applies 3x3 mean blur using numpy vectorized operations
    """
    kernel = np.ones((3, 3)) / 9
    h, w = img.shape

    # pad image to handle borders
    padded = np.pad(img, pad_width=1, mode='constant', constant_values=0)

    # create 3x3 shifted slices and sum
    blurred = (
        padded[0:h, 0:w] + padded[0:h, 1:w+1] + padded[0:h, 2:w+2] +
        padded[1:h+1, 0:w] + padded[1:h+1, 1:w+1] + padded[1:h+1, 2:w+2] +
        padded[2:h+2, 0:w] + padded[2:h+2, 1:w+1] + padded[2:h+2, 2:w+2]
    ) / 9

    return blurred.astype(np.uint8)
