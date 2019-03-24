from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import os
import sys, getopt
 
#converts pdf, returns its text content as a string
def convert(case,fname, pages=None):
    if not pages: pagenums = set();
    else:         pagenums = set(pages);      
    manager = PDFResourceManager() 
    codec = 'utf-8'
    caching = True
 
    if case == 'text' :
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())     
    if case == 'HTML' :
        output = io.BytesIO()
        converter = HTMLConverter(manager, output, codec=codec, laparams=LAParams())
 
    interpreter = PDFPageInterpreter(manager, converter)   
    infile = open(fname, 'rb')
 
    for page in PDFPage.get_pages(infile, pagenums,caching=caching, check_extractable=True):
        interpreter.process_page(page)
 
    convertedPDF = output.getvalue()  
 
    infile.close(); converter.close(); output.close()
    return convertedPDF
 
def convert_pdf_to_txt(path_to_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path_to_file, 'rb')
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
 
input("This is a quick PDF to TXT and HTML converter. It extracts plain text from PDF files and save as *.txt or *.html documents.")
print("-------------------------")
filePDF = input("input directory; your pdf file:   ")
fileHTML = input("output directory for HTML:    ")
fileTXT= input("output directory for TXT:      ")
print("-------------------------")
fileNAME=str(input("the pdf file name:     "))
case=str(input("for creating TEXT output, type T and for HTML output, type H:"    ))
fileHTML =fileHTML+"/"+fileNAME+".html"
fileTXT =fileTXT+"/"+fileNAME+".txt"
filePDF=filePDF+"/"+fileNAME+".pdf"
if case == "H" :
    convertedPDF = convert('HTML', filePDF, pages=None)
    fileConverted = open(fileHTML, "wb")
if case == "T" :
    convertedPDF = convert('text', filePDF, pages=None)
    fileConverted = open(fileTXT, 'w', encoding="utf-8")
######## EITHER
fileConverted.write(convertedPDF)
fileConverted.close()
#print(convertedPDF) 
 
######## OR
#convertedPDF=convert_pdf_to_txt(filePDF)
#fileConverted = open(fileTXT, "w", encoding="utf-8")
#fileConverted.write(convertedPDF)
#fileConverted.close()
print("-------------------------")
print("-------------------------")
input("It's done, press any key to terminate the program")   
Now that we have a way to get the text content of a PDF, all we have to do is
Iterate through all of our PDFs.
For each pdf, get the text content,
open/create a .txt file,
write the text content to the .txt file.
You can do this using the following function and calling it like so:
#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
 
pdfDir = "C:/pdftotxt/pdfs/"
txtDir = "C:/pdftotxt/txt/"
convertMultiple(pdfDir, txtDir)
