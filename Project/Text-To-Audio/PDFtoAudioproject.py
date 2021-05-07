#This program converts any PDF, text pdf to audio
#Import the libraries
import pyttsx3
import pdfplumber
import PyPDF2

#Get the file name and location of the PDF file.
#Create the PDF file object
file = 'Stalingrad ( PDFDrive ).pdf'
pdfFileObj = open(file, 'rb')

#Create PDF File reader object. 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the pages
pages = pdfReader.numPages

#Create pdfplumber objec and it loop through the number of pages
with pdfplumber.open(file) as pdf:
	for i in range(0, pages):
		page = pdf.pages[i]
		text = page.extract_text()
		print(text)
		speaker = pyttsx3.init()
		speaker.say(text)
		speaker.runAndWait()
		speaker.close()