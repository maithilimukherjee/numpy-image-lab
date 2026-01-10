import numpy as np

def blur_image(img):
    """
    applies a simple 3x3 mean blur on a grayscale image
    """
    kernel = np.ones((3, 3)) / 9

    h, w = img.shape
    blurred = np.zeros_like(img)

    for i in range(1, h-1):
        for j in range(1, w-1):
            region = img[i-1:i+2, j-1:j+2]
            blurred[i, j] = np.sum(region * kernel)

    return blurred.astype(np.uint8)
