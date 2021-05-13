# pip install PyPDF2
# pip install pyttsx3

import pyttsx3
import PyPDF2

user = input('Enter the name of the PDF file:\n')
book = open(user, 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

play = pyttsx3.init()
print('Playing audio book')

for num in range(0, num_pages):
    page = pdf_reader.getPage(num)

    data = page.extractText()

    play.say(data)

    play.runAndWait()
