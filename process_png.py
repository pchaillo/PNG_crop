"""
2023

@author: pchaillo

"""
import os
from pathlib import Path
import utils.crop_image as ci
import utils.pdf_conversion as p_c
import cv2 as cv2
from PIL import Image

RECORD_PNG = True
RECORD_PDF = True

source_folder = 'images_to_crop'
destination_folder = 'processed_images'
liste = os.listdir('./' + source_folder)
# print(liste)

for i in liste : 
        u = source_folder + '/' + i
        crop_image = ci.crop_image(u)
        if RECORD_PNG :
                record_path = destination_folder + '/' + i
                cv2.imwrite(record_path, crop_image)
        if RECORD_PDF :
                record_path = destination_folder + '/' + p_c.set_extension(string = i, extension = ".pdf")
                # p_c.record_pdf(image = crop_image,pdf_path = record_path)

images = [
    Image.open(source_folder+'/' + f)
    for f in liste ]


images[0].save(
    record_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)