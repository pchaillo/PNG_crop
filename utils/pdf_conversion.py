# from fpdf import FPDF # librairie nulle ?

def get_extension(string):
    length = len(string)
    string_out = string[length-4:length]
    return string_out

def set_extension(string,extension):
    length = len(string)
    current_extension = string[length-4:length]
    raw_string = string[0:length-4]
    string_out = raw_string + extension
    return string_out

def record_pdf(image,pdf_path):
    pdf = FPDF() 
    pdf.add_page()
    pdf.image(image,0,0,100,200)
    pdf.output("pdf_path", "F")




# pdf = FPDF() # Library exemple
# # imagelist is the list with all image filenames
# for image in imagelist:
#     pdf.add_page()
#     pdf.image(image,x,y,w,h)
# pdf.output("yourfile.pdf", "F")