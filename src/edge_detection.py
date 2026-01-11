import numpy as np

def detect_edges(img):
    """
    detects edges using a sobel-x kernel
    """
    kernel_x = np.array([
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ])

    h, w = img.shape
    edges = np.zeros_like(img)

    for i in range(1, h-1):
        for j in range(1, w-1):
            region = img[i-1:i+2, j-1:j+2]
            edges[i, j] = np.sum(region * kernel_x)

    return np.clip(edges, 0, 255).astype(np.uint8)
