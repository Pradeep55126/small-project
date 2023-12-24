import pyttsx3
import PyPDF2
book = open('python2.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(6,7):
    page = pdfReader.getPage(6)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


