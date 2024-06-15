

# import module
from pdf2image import convert_from_path
import os
 
# Store Pdf with convert_from_path function
source_folder = 'pdf_to_convert'
destination_folder = 'images_to_crop'
liste = os.listdir('./' + source_folder)

for one_pdf in liste :
      if one_pdf == 'README.md':
            print("OK !")
      else :
            print('./' + source_folder + '/' + one_pdf)
            images = convert_from_path('./' + source_folder + '/' + one_pdf)
            for i in range(len(images)):       
                  # Save pages as images in the pdf
                images[i].save('./' + destination_folder + '/' + one_pdf + str(i) +'.jpg', 'JPEG')
