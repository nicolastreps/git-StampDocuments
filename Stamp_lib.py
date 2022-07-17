#!/usr/bin/python3
# pdf_splitter.py

import os
import re
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
#import pikepdf


def stamp_pdf(fichierin, fichierout, WM):
	pdf = PdfFileReader(fichierin)
	WMpdf = PdfFileReader(WM)
	WMpdf0=WMpdf.getPage(0)	
	pdf0_writer = PdfFileWriter()
	for Page in range(0, pdf.getNumPages()):
		pdf0 = pdf.getPage(Page)	
		pdf0.mergePage(WMpdf0)
		pdf0_writer.addPage(pdf0)
	with open(fichierout, 'wb') as out:
		pdf0_writer.write(out)
