from src.load_image import load_image, show_image
from src.grayscale import gray
from src.normalize import normalize
from src.brightness_contrast import adjustBrightness, adjustContrast
from src.flip import flip_horizontal, flip_vertical
from src.blur import blur_image

img = load_image("images/sample.jpeg")
print(img.shape)
show_image(img)

grayPic = gray(img)
show_image(grayPic, cmap="gray")  

grayNormalized = normalize(grayPic)
print(grayNormalized.min(), grayNormalized.max())

brightPic = adjustBrightness(grayPic,40)
show_image(brightPic,cmap="gray")

contrastPic = adjustContrast(grayPic, 1.5)  # stronger contrast
show_image(contrastPic, cmap="gray")

hFlip = flip_horizontal(grayPic)
show_image(hFlip,cmap="gray")

vFlip = flip_vertical(grayPic)
show_image(vFlip,cmap="gray")

blurPic = blur_image(grayPic)
show_image(blurPic, cmap="gray")
