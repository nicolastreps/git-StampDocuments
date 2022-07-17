#!/Users/nicolastreps/opt/anaconda3/bin/python

import os
import re
import sys
import random
from PyPDF2 import PdfFileReader, PdfFileWriter
#import pikepdf



#if len(sys.argv) != 3:
#	print('Usage Split_Pdf.py Fichier_Pdf_Source Dossier_Resultat Wattermark')
#	sys.exit(1)

Repertoire = "/Users/nicolas/ownCloud/Direction-LicenceDePhysique/scripts/ParaphPV/" 
fichiersource = "[SPRINT]3SLPYII0-session1_à_signer_11 07 2022"
#cleanfichier = '/opt/homebrew/bin/qpdf ' + Repertoire + fichiersource + '.pdf ' + Repertoire + fichiersource + '-fix.pdf'
#os.system(cleanfichier)
PdfFile = Repertoire + fichiersource + '-fix.pdf' #  Clean file first with qpdf 
OutputFile = Repertoire + fichiersource + '-NT.pdf'

Paraphfile = "Paraph-10-flat.pdf"
Paraphpdf = PdfFileReader(Paraphfile)
Paraphs = [Paraphpdf.getPage(Page) for Page in range(0, Paraphpdf.getNumPages())]

Stampfile = "StampPV-flat.pdf"
StampfilePdf = PdfFileReader(Stampfile)
StampPV = StampfilePdf.getPage(0)

Stampfile2 = "StampAlone.pdf"
Stampfile2pdf = PdfFileReader(Stampfile2)
StampPV2 = Stampfile2pdf.getPage(0)

pdf = PdfFileReader(PdfFile)
pdf_writer = PdfFileWriter()
pdf_writer.addPage(pdf.getPage(0))
for Page in range(1, pdf.getNumPages()-1):
	PdfPage = pdf.getPage(Page)
	PdfPage.mergePage(Paraphs[random.randint(0, 9)])
	pdf_writer.addPage(PdfPage)
	
PdfPage = pdf.getPage(Page+1)

#xp=PdfPage.mediaBox.getUpperRight_x()
#yp=PdfPage.mediaBox.getUpperLeft_y()
#PdfPage.mediaBox.upperLeft=(0,xp)
#PdfPage.mediaBox.lowerRight=(yp,0)
#PdfPage.rotateCounterClockwise(90)
#StampPV.rotateCounterClockwise(90)

#PdfPage.mergePage(StampPV)
PdfPage.mergeRotatedTranslatedPage(StampPV, 180, StampPV.mediaBox.getWidth()/2, StampPV.mediaBox.getWidth()/2)
pdf_writer.addPage(PdfPage)

with open(OutputFile, 'wb') as out:
	pdf_writer.write(out)
