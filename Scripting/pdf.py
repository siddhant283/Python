import os
import PyPDF2


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
pdf1_path = script_dir + '/pdfs/sid.pdf'
blank_path = script_dir + '/pdfs/blank.pdf'

with open(pdf1_path, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(blank_path, 'wb') as new_file:
        writer.write(new_file) 
