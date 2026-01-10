from src.load_image import load_image, show_image
from src.grayscale import gray
from src.normalize import normalize
from src.brightness_contrast import adjustBrightness

img = load_image("images/sample.jpeg")
print(img.shape)
show_image(img)

grayPic = gray(img)
show_image(grayPic, cmap="gray")  

grayNormalized = normalize(grayPic)
print(grayNormalized.min(), grayNormalized.max())

brightPic = adjustBrightness(grayPic,40)
show_image(brightPic,cmap="gray")