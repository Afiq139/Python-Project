
#install:
#pip install pdfminer.six
#pip install PyMuPDF --> import fitz
#pip install pillow  --> PIL.Image
#pip install tabula-py --> table
#pip install pandas

import re  #regular expression
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("test.pdf"):
#     for element in page_layout:
#         print(element)

# text = extract_text("test.pdf")
# print(text)

# pattern = re.compiler(r"[a-zA-Z]+ , {1}\s{1}")
# matches = pattern.findall(text)
# names = [n[:2] for n in matches]
# print(names)
