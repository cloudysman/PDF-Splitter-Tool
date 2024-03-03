from PyPDF2 import PdfReader, PdfWriter

def extract_pages_from_pdf(source_pdf_path, output_pdf_path, start_page, end_page):
    reader = PdfReader(source_pdf_path)
    writer = PdfWriter()
    
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
    
    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

# Gọi hàm với đường dẫn tới file nguồn và file đích
extract_pages_from_pdf("LSD.pdf", "LSD_cut.pdf", 48, 83)
