# To put all the images of the folder in the same pdf files


import os
from PIL import Image
import utils.pdf_conversion as p_c

source_folder = 'images_to_crop'
destination_folder = 'processed_images'
liste = os.listdir('./' + source_folder)

record_path = destination_folder + '/' + p_c.set_extension(string = liste[0], extension = ".pdf")

images = [
    Image.open(source_folder+'/' + f)
    for f in liste ]

images[0].save(
    record_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])