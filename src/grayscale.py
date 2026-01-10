# gray = 0.299*R + 0.587*G + 0.114*B


import numpy as np

def gray(img):
    
    g = (
        0.299*img[:,:,0] + #red channel
        0.587*img[:,:,1] + #green channel
        0.114*img[:,:,2] #blue channel
    )
    
    return g.astype(np.uint8)

'''
key numpy concepts here:

img[:, :, 0] → all red pixels
slicing + broadcasting → apply math to the whole image at once
no loops needed
.astype(np.uint8) → keep pixel values in 0–255
'''