import sys
import os
from PIL import Image

#python JPGtoPNGconverter.py pokemon/ new/

#grap first and second index from terminal
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check is new/ exist, if not create
# loop through pokemon
# convert images to png
# save to new folder
def convertImg (image_folder,output_folder):
    if os.path.isdir(output_folder):
        print((f"{output_folder} folder is really exist"))
        return
    else:
        os.mkdir(output_folder)
        for filename in os.listdir(image_folder):
            f = os.path.join(image_folder, filename)

            if os.path.isfile(f):
                clean_name = os.path.splitext(filename)[0]
                new_file = f"{output_folder}{clean_name}.png"
                img = Image.open(f)
                img.save(new_file,"png")



convertImg(image_folder,output_folder)