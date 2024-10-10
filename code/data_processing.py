# data_processing.py

import pdfplumber

def process_pdf(uploaded_file):
    """Process the uploaded PDF file and extract text using pdfplumber."""
    documents = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()  # Extract text from the page
            if text:
                documents.append(text)  # Add text to documents list
    return documents  # Return the list of extracted documents
