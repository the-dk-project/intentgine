import os.path
from datetime import datetime
from PyPDF2 import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def file_to_dict(input_file, delimiter=" "):
    try:
        sc_dict = dict()
        file = open(input_file, encoding="utf8")
        lines = file.readlines()

        for line in lines:
            line = line.rstrip()
            line_array = line.split(delimiter)
            key = line_array[1]
            value = line_array[0]
            if int(value) != 1:
                sc_dict[key] = value

        file.close()

    except Exception as e:
        print(datetime.now(), "ERROR: {0}".format(e))
        exit(1)

    else:
        return sc_dict

def pdf_reader(input_file):
    pdf_file = open(input_file, 'rb')
    read_pdf = PdfFileReader(pdf_file, strict=False)
    if read_pdf.isEncrypted:
        read_pdf.decrypt('')
    count = read_pdf.numPages(password='')
    content = ""
    for i in range(count):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        content += page_content

    pdf_file.close()
    return content

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def pdf_info(pdf_file):
    pdf_file = open(pdf_file, 'rb')
    read_pdf = PdfFileReader(pdf_file, strict=False)
    info = read_pdf.getDocumentInfo()

    pdf_file.close()
    return info