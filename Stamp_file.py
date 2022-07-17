#!/Users/nicolas/opt/anaconda3/bin/python


import os
import re
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from Stamp_lib import *


Repertoire = "/Users/nicolas/ownCloud/Direction-LicenceDePhysique/scripts/Essai-Separe/" 
fichiersource = "3705264_MAHJOUBI-Farah_L3PY01_20-21_session2"
cleanfichier = '/opt/homebrew/bin/qpdf ' + Repertoire + fichiersource + '.pdf ' + Repertoire + fichiersource + '-fix.pdf'
os.system(cleanfichier)
PdfFileIn = Repertoire +fichiersource + '-fix.pdf' #  Clean file first with qpdf 
PdfFileOut = Repertoire +fichiersource + '-signe.pdf' 
WMfile = "TamponSigneLPhysC.pdf"
stamp_pdf(PdfFileIn,PdfFileOut,WMfile)
