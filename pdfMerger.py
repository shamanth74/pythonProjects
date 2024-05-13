import PyPDF2

# List of PDF files to merge
pdf_files = ["document1.pdf", "document2.pdf", "document3.pdf"]

# Create a PdfWriter object
pdf_writer = PyPDF2.PdfWriter()

# Loop through each PDF file
for pdf_file in pdf_files:
    # Open the PDF file in binary mode
    with open(pdf_file, "rb") as file:
        # Create a PdfReader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Loop through each page and add it to the PdfWriter object
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

# Write the merged content to a new PDF file
with open("merged.pdf", "wb") as output_file:
    pdf_writer.write(output_file)
