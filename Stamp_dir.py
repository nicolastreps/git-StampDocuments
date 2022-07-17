#!/Users/nicolastreps/opt/anaconda3/bin/python

import subprocess
import re
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from Stamp_lib import *
import glob

WMfile = "TamponSigneLPhysC-2.pdf"


if len(sys.argv) == 1:
	Repertoire = "/Users/nicolastreps/ownCloud/Direction-LicenceDePhysique/scripts/ATamponner/" 
else : 
	if len(sys.argv) == 2:
		Repertoire = sys.argv[1]
	else :
		print('Usage Stamp_dir.py [Repertoire]')
		sys.exit(1)

print(sys.argv[0])

for f in glob.glob(Repertoire+'*.pdf'):
#	cleanfichier = '/opt/homebrew/bin/qpdf --replace-input ' + f
	cleanfichier = ["/opt/homebrew/bin/qpdf", "--replace-input", f] 
	subprocess.run(cleanfichier)
	stamp_pdf(f,f,WMfile)
