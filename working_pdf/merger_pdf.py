import PyPDF2
import sys

# (test sample) python pdf.py dummy.pdf  twopage.pdf tilt.pdf
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)