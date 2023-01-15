import pyttsx3
import PyPDF2

book = open('OS.pdf', 'rb') # pdf_file = OS.pdf
reader = PyPDF2.PdfReader(book)
mark = reader.pages
print(mark)
audio = pyttsx3.init()
page = reader.pages[2]
text = page.extract_text()
audio.say(text)
audio.runAndWait()
