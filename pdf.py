import PyPDF2

with open("./dummy.pdf", "r") as file:
    reader = PyPDF2.PdfFileReader()
