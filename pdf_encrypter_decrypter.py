# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:48:08 2021

@author: ankit
"""

from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)


decrypt_pdf("C:/Users/ankit/Downloads/ABTSBill_7029103760_Apr2019.pdf", "C:/ankit/AWS_tutorials/ankit_Apr_2019.pdf", "7029103760")