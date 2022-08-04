# How to Move Files in Python: Single and Multiple File Examples
# A quick way of moving a file from one place to another is using shutil.move() as shown:

import pandas as pd
import pathlib
import os
import shutil

shutil.move('old_directory/test_file.txt', 'new_directory/test_file.txt')
# We'll look at some of the various options you've got for moving files around using Python. There's also a quick example of how you could use the shutil and os libraries to tidy up your downloads folder in the first section. So if you're someone that needs something like that in your life, then keep reading!

# Option 1: shutil.move()
# The example shown in the introduction uses the move() function from the shutil library. This function does what you'd expect and moves files from one location to the other, as follows:


shutil.move(old_path, new_path)
shutil.move()  # works by first creating a copy of the file with the path defined by old_path and storing the copy in the new location, new_path. Finally, after the successful creation of the copy, Python deletes the original file located at old_path.

In cases where the original file is protected, shutil.move() will create a copy of the file in the new location, but Python will be unable to delete the original.

Most people have got quite messy download folders. So let's look at a practical example of how we could use shutil.move() to store all the images in a download folder in a new folder called downloaded images:


images = [f for f in os.listdir() if '.jpg' in f.lower()]

os.mkdir('downloaded_images')

for image in images:
    new_path = 'downloaded_images/' + image
    shutil.move(image, new_path)
# Running this script inside a downloads folder will move any files with the extension .jpg or .JPG in the folder to the downloaded_images folder. Using os.listdir() returns a list of all the files in the folder. By then using os.mkdir('downloaded_images') the downloaded_images folder is created. Using shutil.move(), Python can then move all the files in our images list to the new folder. This process is shown in the diagram below:


# There's a lot of room for improvement here. For example, we could upgrade our list comprehension to include more image types. We should also code in an if-else branch to see if the downloaded_images folder exists before running os.mkdir(). There's also no reason we couldn't expand this script to create separate folders for PDFs, executable files and anything else sitting in your downloads folder gathering dust!

# Option 2: os.rename()
# The os library also has a couple of options for moving files, one of these is os.rename(). os.rename() functions a little differently to shutil.move().

# Instead of copying the file in question, rename() alters the path of a file, which automatically changes the file location. See below for an example of how we could apply the function:


os.rename('old_directory/test_file.txt', 'new_directory/test_file.txt')
# os.replace()# works too. Despite the function being called replace(), it also moves files by renaming them. os.replace() can be implemented with an identical template to shutil.move() and os.rename():


os.replace('old_directory/test_file.txt', 'new_directory/test_file.txt')
# os.replace()# and os.rename() can both be used to change a file or directory name. os.rename() reports errors differently depending on what operating system you're running.

# Whereas os.replace() will report errors uniformly across different systems, which may be the better choice when working on a program that needs compatibility with different operating systems.

# Option 3: pathlib.Path().rename()
# For a more object-oriented approach to moving files, pathlib is also an option.

# By using the Path() function, Python creates a Path object. The rename() method then changes the path of the object, similarly to how os.rename() works:


pathlib.Path(
    'old_directory/test_file.txt').rename('new_directory/test_file.txt')
# We could also apply pathlib.Path().rename() to our script created earlier for moving images out of our downloads folder. See below for an example of this:


images = [f for f in os.listdir() if '.jpg' in f.lower()]

os.mkdir('downloaded_images')

for image in images:
    new_path = 'downloaded_images/' + image
    pathlib.Path(image).rename(new_path)

# Below is a table that compares the speed difference of the three approaches:


# Create anonymous functions - need to regenerate files after each move

def gen_file(file_name):
    with open(f'old_directory/{file_name}', 'w') as f:
        f.write('')


def shutil_move():
    gen_file('shutil.txt')
    shutil.move('old_directory/shutil.txt', 'new_directory/shutil.txt')


def os_move():
    gen_file('os.txt')
    os.rename('old_directory/os.txt', 'new_directory/os.txt')


def pathlib_move():
    gen_file('pathlib.txt')
    pathlib.Path(
        'old_directory/pathlib.txt').rename('new_directory/pathlib.txt')


# Calculate timings
shutil_time = %timeit - o - q shutil_move()
os_time = %timeit - o - q os_move()
pathlib_time = %timeit - o - q pathlib_move()

# Create data table
data = [['shutil.move()', shutil_time.best], ['os.rename()', os_time.best],
        ['Pathlib.Path()', pathlib_time.best]]
df = pd.DataFrame(data, columns=['type', 'microseconds'])
df.microseconds = round(df.microseconds * 1e6, 2)
df.sort_values('microseconds', inplace=True)

df

# OUT:
#    type	microseconds
# 1	os.rename()	50.55
# 0	shutil.move()	54.58
# 2	Pathlib.Path()	63.74
# Summary

# You've got a few options when it comes to moving files around. shutil.move(), os.rename() and os.replace() are all great approaches, with all three of them using the arguments (old_path, new_path). For a more object-oriented approach, you could also use pathlib.Path().rename(), providing Path() with old_path and rename() with new_path.
