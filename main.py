from PyPDF2 import PdfReader

# Open the PDF file
pdf_file = open("Operations Management.pdf", "rb")

# Create a PDF reader object
pdf_reader = PdfReader(pdf_file)

# Read the content from the PDF
pdf_content = ""
for page in pdf_reader.pages:
    pdf_content += page.extract_text()

# Close the PDF file
pdf_file.close()
