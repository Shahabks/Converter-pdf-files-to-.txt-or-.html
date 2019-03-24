# Converter-pdf-files-to-.txt-or-.html
PDFs are notoriously difficult to scrape. This program converts them to *.txt or *.html formats. The program has tested for Latin alphabets and Japanese. 


## Introduction
I built this package on the work of Gorkovenko (Stanford University) and Greenfield (Harvard University) to make **pdfminer.six** available for **Python versions 3.x**.
 
 […] PDFs are notoriously difficult to scrape. Converting them to text files can make extracting their data significantly easier. There are several tools out there to help you do this, but I will focus on the one that I think is the best and easiest to use: pdfminer.six
Converting *.pdf   to   *.txt or *.html
I made a standalone executable version of the package ready **testpdf2txt.exe**. You could download and use it even if you do not have python 3 installed on your machine. 

### please download **---testpdf2txt.exe---** from the ***releases*** branch above. 

You can save the program anywhere in your computer and run it by double-clicking on it directly from your machine. 

<UL>
<li>Put your PDF file in a folder.
<li>Double-click the program and follow the instruction on the screen.
<li>You may save *.txt and *.html in a different directory, please enter the path to those directory if you wish.
<li>Enter the filename of your PDF. 
</ul>

## Converting Multiple PDFs to .txt
If you have multiple PDFs that you need to convert, you just have to iterate through them and call the same commands as above. Do the following steps.
<ul>
<li>Create a new folder, and put all of your PDFs in there. In this example, my folder is titled “pdfs.”
<li>Create a new folder to store your .txt files. My folder is titled “txt.”
<li>Create a *.bat file, type the cd command to change directories to your PDF folder.
<li>Use the command line for-loop syntax in the following example to loop through your PDFs and convert them all to .txt. 

     @rem change to your new folder
     cd "C:\pdfToText" 
     @rem make txt file, name it example.txt
     cmd /k testpdf2txt.exe -o example.txt example.pdf
     cd "c:\pdftotext\pdfs"
     cmd /k for %%i in (*) do "c:\users\testpdf2txt.exe" -o c:\pdftotext\txt\%%~ni.txt %%i
     “%%i” stands for the current PDF file.  .
                         

I put “%%” in front of every “i” because in batch files you have to preface every variable reference with a “%%”.
“(*)” stands for the current directory.
"c:\pdftotext\pdf2txt.py" tells the computer to run “testpdf2txt.exe” from the “c:\users” directory.
The modifier “~n” returns the filename only of the current file -- not the directory or extension. I used this modifier to make the filenames of my .txt files be the same as those of their corresponding PDFs. See here for more information about modifiers.
Your PDFs should now be converted to .txt.

## Converting PDFs to .txt in Python
Using pdfminer as a module to convert PDFs can be done with the following steps.
Copy and paste the following code, found on this website, into your Python script. The convert() function returns the text content of a PDF as a string.

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

 

 

