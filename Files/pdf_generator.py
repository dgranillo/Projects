#!/usr/bin/env python2.7
"""PDF Generator
An application which can read in a text file, html file or some other file and 
generates a PDF file out of it. Great for a web based service where the user 
uploads the file and the program returns a PDF of the file.

Optional: Deploy on GAE or Heroku if possible.

Author: Dan Granillo"""

from PyPDF2 import PdfFileWriter, PdfFileReader

input1 = PdfFileReader(file('my_text', 'rb'))
output = PdfFileWriter()

output.addPage(input1)
outputStream = file('document-output.pdf', 'w')
output.write(outputStream)
outputStream.close()