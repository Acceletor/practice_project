import PyPDF2

# write wtr.pdf to watermark all the page in super.pdf

def watermark_pdf(file):
    reader = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    watermark = reader.pages[0]

    reader = PyPDF2.PdfFileReader(open(file, 'rb'))
    writer = PyPDF2.PdfFileWriter()
    num_page = reader.getNumPages()
    for index in range(num_page):
        content_page = reader.getPage(index)
        mediabox = content_page.mediaBox
        content_page.mergePage(watermark)
        content_page.mediaBox = mediabox   # To ensure that the page retains its original size and layout.
        writer.addPage(content_page)

    with open('result.pdf', "wb") as fb:
        writer.write(fb)

    

watermark_pdf("super.pdf")