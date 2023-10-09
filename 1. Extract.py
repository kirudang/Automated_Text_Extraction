# Import library
from PyPDF2 import PdfReader

# Open the PDF file
pdf_file = PdfReader(open("data/sample.pdf", "rb"))

# Read all the pages in the PDF
pages = [pdf_file.pages[i] for i in range(len(pdf_file.pages))]

# Join all the pages into a single string
text = '\n'.join([page.extract_text() for page in pages])
