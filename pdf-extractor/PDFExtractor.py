import os
import PyPDF2
from docx import Document

def convert_pdf_to_word(pdf_directory, output_word_file_path):
    doc = Document()  # Create a new Word document object

    for filename in os.listdir(pdf_directory):  # Iterate over files in the specified PDF directory
        if filename.endswith('.pdf'):  # Check if the file has a PDF extension
            pdf_file_path = os.path.join(pdf_directory, filename)  # Get the full path of the PDF file

            pdf_file = open(pdf_file_path, 'rb')  # Open the PDF file in binary mode
            pdf_reader = PyPDF2.PdfReader(pdf_file)  # Create a PDF reader object

            for page in pdf_reader.pages:  # Iterate over each page in the PDF
                text_content = page.extract_text()  # Extract the text content from the current page
                if text_content:  # Check if there is any text content
                    doc.add_paragraph(text_content)  # Add the text content to the Word document

            pdf_file.close()  # Close the PDF file

    output_directory = os.path.dirname(output_word_file_path)  # Get the directory path of the output Word file
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    doc.save(output_word_file_path)  # Save the Word document to the specified output file path

# Usage:
script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory path of the current script
pdf_directory = os.path.join(script_directory, 'Input')  # Define the input PDF directory path
word_output_file = os.path.join(script_directory, 'Output', 'Output.docx')  # Define the output Word file path

convert_pdf_to_word(pdf_directory, word_output_file)  # Call the function to convert PDF to Word