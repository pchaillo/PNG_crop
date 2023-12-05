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

RECORD_JPG = True # to record one by one all the cropped images => this inetrmediary format is finally used for pdf conversion
RECORD_PDF = True # to record one by one all the cropped images in pdf format

source_folder = 'images_to_crop'
destination_folder = 'processed_images'
liste = os.listdir('./' + source_folder)
# print(liste)

for i in liste : 
        u = source_folder + '/' + i
        crop_image = ci.crop_image(u)
        if RECORD_JPG :
                record_path = destination_folder + '/jpg/' + i
                cv2.imwrite(record_path, crop_image)
        if RECORD_PDF :
                record_path_pdf = destination_folder + '/pdf/' + p_c.set_extension(string = i, extension = ".pdf")
                p_c.record_pdf(image_path = record_path,pdf_path = record_path_pdf)


