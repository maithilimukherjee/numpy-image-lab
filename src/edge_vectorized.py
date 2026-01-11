import numpy as np

def detect_edges_vectorized(img):
    """
    detects edges using sobel-x kernel (vectorized)
    """
    h, w = img.shape
    padded = np.pad(img, pad_width=1, mode='constant', constant_values=0).astype(np.int16)

    edges = (
        -1*padded[0:h, 0:w] + 0*padded[0:h, 1:w+1] + 1*padded[0:h, 2:w+2] +
        -2*padded[1:h+1, 0:w] + 0*padded[1:h+1, 1:w+1] + 2*padded[1:h+1, 2:w+2] +
        -1*padded[2:h+2, 0:w] + 0*padded[2:h+2, 1:w+1] + 1*padded[2:h+2, 2:w+2]
    )

    return np.clip(edges, 0, 255).astype(np.uint8)
