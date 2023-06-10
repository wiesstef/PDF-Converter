# PDF to Word Converter

This project is a Python script that converts PDF files to Word documents. It uses the PyPDF2 library to extract text content from PDF files and the python-docx library to create Word documents.

## Requirements

To run the script, you need to have the following dependencies installed:

- Python 3
- PyPDF2
- python-docx

You can install the required packages using pip:

pip install PyPDF2 python-docx

markdown
Copy code

## Usage

1. Create two subdirectories in the project directory:
   - `Input`: Place the PDF files you want to convert in this directory.
   - `Output`: The converted Word documents will be saved in this directory.

2. Open the `PDFExtractor.py` script and modify the following variables:
   - `pdf_directory`: Set it to the path of the `Input` subdirectory.
   - `word_output_file`: Set it to the desired path and filename of the Word document in the `Output` subdirectory.

3. Run the script:
python PDFExtractor.py


The script will convert the PDF files in the `Input` directory to Word documents and save them in the `Output` directory.

## Notes

- The script extracts only the text content from the PDF files. If you need to include images or preserve the formatting, you may need to use additional libraries or tools.

- Make sure the PDF files are in a format that can be properly parsed by PyPDF2. Complex layouts or scanned PDFs may not extract text accurately.

- The script assumes that the PDF files have the `.pdf` extension. Only files with this extension will be processed.

- If you encounter any issues or errors, please check the dependencies, file paths, and the format of the PDF files.

## License

This project is licensed under the [MIT License](LICENSE).
