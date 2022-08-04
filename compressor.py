# compressing images
from distutils import extension
from pickletools import optimize
from PIL import Image  # python -m pip install pillow

import os

downloadsFolder = './'

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "compressed_" +
                         filename, optimize=True, quality=60)


######
