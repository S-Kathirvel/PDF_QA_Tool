# query_engine.py
from llama_cloud import SentenceSplitter
# from llama_index.
from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def create_query_engine(documents):
    """
    Create a query engine using the loaded documents.
    """
    # Use a sentence-transformer embedding model
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    Settings.transformations = [SentenceSplitter(chunk_size=1024, chunk_overlap=20)]
    
    # Index the documents
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model, transformations=Settings.transformations)
    
    return embed_model, index
