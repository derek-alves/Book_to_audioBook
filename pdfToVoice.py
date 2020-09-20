import PyPDF2

bookName = 'threejs.pdf'


class main(namebook):
    book = open(namebook, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    
    def getAllPages():
      pages = pdfReader.numPages
      return pages
    
    def getContentPage(numberPage):
      page = pdfReader.getPage(numberPage)
      return page

    def textOfPage(page):
      text = page.extractText()
      return text


# pages = pdfReader.numPages
# page = pdfReader.getPage(7)
# text = page.extractText()

print(pdfReader)