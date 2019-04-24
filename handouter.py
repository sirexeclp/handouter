#%%
import sys
import re
input_file = sys.argv[1]

#%%
from PyPDF2 import PdfFileReader
pdf = PdfFileReader(open(input_file, 'rb'))

#%%
from PyPDF2 import PdfFileWriter, PdfFileReader
last_page = 0
output = PdfFileWriter()
pages2keep =[]
for i in reversed(range(pdf.getNumPages())):
    page = pdf.getPage(i)
    last_line = page.extractText().strip().split("\n")[-1]
    m = re.search("^[0-9]+", last_line)
    if m:
        m = m.group(0)
    else:
        pages2keep.append(page)
        continue
    if last_page != int(m):
        pages2keep.append(page)
        last_page = int(m)

[output.addPage(page) for page in reversed(pages2keep)]

with open(f"{input_file}.short.pdf", 'wb') as f:
    output.write(f)