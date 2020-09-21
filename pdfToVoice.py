import PyPDF2
from gtts import gTTS
from translate import Translator

bookName = 'threejs.pdf'


class main:

    def __init__(self,namebook):
        self.book = namebook
        self.instaciate = open(self.book, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(self.instaciate)
      
    def getAllPages(self):
      pages = self.pdfReader.numPages
      return pages
    
    def getContentPage(self,numberPage):
      page = self.pdfReader.getPage(numberPage)
      return page

    def textOfPage(self,page):
      text = page.extractText()
      return text


book = main(bookName)
page = book.getContentPage(7)
result = book.textOfPage(page)
info = (result[:250] + '..') if len(result) > 500 else result

translator = Translator(to_lang="Portuguese")
translation = translator.translate(info)

print(translation)
