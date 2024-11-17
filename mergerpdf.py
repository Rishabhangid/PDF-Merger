# Importing the PdfWriter class from pypdf library
from pypdf import PdfWriter

# List of PDF files to be merged
pdfs = ["pdf1.pdf", "pdf2.pdf"]

# Initialize the PdfWriter object which will be used to merge the PDFs
merger = PdfWriter()

# Loop through each PDF file in the pdfs list and append them to the merger
for pdf in pdfs:
    merger.append(pdf)  # Append each PDF to the merger

# Write the merged PDF to a new file named 'result.pdf'
# Open the result.pdf in write-binary mode to save the merged content
with open("result.pdf", "wb") as output_pdf:
    merger.write(output_pdf)

# Close the PdfWriter object to free up any resources
merger.close()
    