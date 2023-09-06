import os
import glob
from PIL import Image

def resize_keeped_aspect_ratio(path: str, size: tuple):
    image = Image.open(path).convert('RGBA')
    width, height = size
    x_ratio = width / image.width
    y_ratio = height / image.height
    if x_ratio < y_ratio:
        resize_size = (width, round(image.height * x_ratio))
    else:
        resize_size = (round(image.width * y_ratio), height)
    return image.resize(resize_size, Image.LANCZOS)

image_files = glob.glob('illust/*.png')

for image in image_files:
    resezed_image = resize_keeped_aspect_ratio(image, (320,240))
    resezed_image.save(os.path.splitext(image)[0] + ".webp", "webp")
