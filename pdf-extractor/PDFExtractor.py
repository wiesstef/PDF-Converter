import os
import PyPDF2
from docx import Document

def convert_pdf_to_word(pdf_directory, output_word_file_path):
    doc = Document()

    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(pdf_directory, filename)

            pdf_file = open(pdf_file_path, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page in pdf_reader.pages:
                text_content = page.extract_text()
                if text_content:
                    doc.add_paragraph(text_content)

            pdf_file.close()

    output_directory = os.path.dirname(output_word_file_path)
    os.makedirs(output_directory, exist_ok=True)
    doc.save(output_word_file_path)

# Usage:
script_directory = os.path.dirname(os.path.abspath(__file__))
pdf_directory = os.path.join(script_directory, 'Input')
word_output_file = os.path.join(script_directory, 'Output', 'Output.docx')

convert_pdf_to_word(pdf_directory, word_output_file)
