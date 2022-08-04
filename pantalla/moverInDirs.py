# helped by: https://stackoverflow.com/questions/23556040/moving-specific-file-types-with-python

import os
import shutil


sourcepath = './/'
sourcefiles = os.listdir(sourcepath)
imgs = './imgs2'
excel = '.\excel/'
word = '.\word/'
pdf = '.\pdf'
musica = '.\musica'

for file in sourcefiles:
    if file.endswith('.png'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(imgs, file))

    if file.endswith('.xlsx'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(excel, file))

    if file.endswith('.docs'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(word, file))

    if file.endswith('.pdf'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(pdf, file))

    if file.endswith('.mp3'):
        try:
            shutil.move(os.path.join(sourcepath, file),
                        os.path.join(musica, file))
        except:
            print("No existe el directorio o carpeta, revise por favor")
