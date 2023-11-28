"""
2023

@author: pchaillo

"""
import os
from pathlib import Path
import utils.crop_image as ci
import cv2 as cv2

source_folder = 'images_to_crop'
destination_folder = 'processed_images'
liste = os.listdir('./' + source_folder)
# print(liste)

for i in liste : 
        u = source_folder + '/' + i
        crop_image = ci.crop_image(u)
        record_path = destination_folder + '/' + i
        cv2.imwrite(record_path, crop_image)
