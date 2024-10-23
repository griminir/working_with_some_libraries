import PyPDF2

# rb stands for read binary
# with open('first.pdf', 'rb') as file1:
#     reader = PyPDF2.PdfReader(file1)
#     print(len(reader.pages))
#     page = reader._get_page(0)
#     page.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('rotated.pdf', 'wb') as output:
#         writer.write(output)

merger = PyPDF2.PdfMerger()
file_names = ['first.pdf', 'second.pdf']
for file_name in file_names:
    merger.append(file_name)
merger.write('combined.pdf')