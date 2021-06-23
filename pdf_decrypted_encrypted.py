# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:12:46 2021

@author: ankit
"""

import PyPDF2

pdf_in_file = open("C:/ankit/AWS_tutorials/ankit_abc.pdf",'rb')

inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
pages_no = inputpdf.numPages
pages_no
for i in range(pages_no):
	inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
	
	output = PyPDF2.PdfFileWriter()
    
	output.addPage(inputpdf.getPage(i))
	output.encrypt('xyz')

	with open("C:/ankit/AWS_tutorials/ankit_abc_password_protected.pdf", "wb") as outputStream:
		output.write(outputStream)

pdf_in_file.close()