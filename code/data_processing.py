from llama_index.readers.smart_pdf_loader import SmartPDFLoader

# Define LLMSherpa API URL (if applicable)
llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"


def load_data(data_path):
  """
  This function loads data from either a PDF file or a directory containing documents.

  Args:
      data_path (str): The path to the PDF file or directory.

  Returns:
      list: A list of documents loaded from the data source.
  """
  if data_path.endswith(".pdf"):
    pdf_loader = SmartPDFLoader(llmsherpa_api_url=llmsherpa_api_url)
    document = pdf_loader.load_data(data_path)
    return [document]
  else:
    # Implement logic for loading documents from a directory using SimpleDirectoryReader (not shown here)
    pass

# Example usage (assuming you have a PDF file named "Twixor.pdf")
pdf_url = "/path/to/your/pdf/file"
documents = load_data(pdf_url)
