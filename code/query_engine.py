from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

# Load the previously defined models (llm and embed_model) from model_loading.py
from .model_loading import llm, embed_model
from .data_processing import documents

def create_query_engine(documents):
  """
  This function creates a query engine using the loaded documents and models.

  Args:
      documents (list): A list of documents loaded from the data source.

  Returns:
      object: The query engine object for processing user queries.
  """
  index = VectorStoreIndex.from_documents(documents, embed_model=embed_model, transformations=Settings.transformations)
  query_engine = index.as_query_engine(llm=llm)
  return query_engine

# Example usage (assuming documents are loaded)
query_engine = create_query_engine(documents)
