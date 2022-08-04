# compressing images
from distutils import extension
from pickletools import optimize
from PIL import Image  # python -m pip install pillow

import shutil
import os

downloadsFolder = './pantalla/'
images = './pantalla/images/'
text = './pantalla/text/'
music = './pantalla/music/'
word = './pantalla/word/'
excel = './pantalla/excel'

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".xlsx"]:
            shutil.move(filename, 'excel', copy_function=shutil.copy)
