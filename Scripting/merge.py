import os
import sys
import PyPDF2

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        clean_name = pdf.split('/')[2]
        print(clean_name)
        merger.append(clean_name)
    merger.write('super.pdf')    

pdf_combiner(inputs)        