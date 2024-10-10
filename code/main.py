# main.py

from data_processing import load_documents
from model_loading import load_llm, load_embedding_model
from query_engine import create_query_engine
from interactive_qa import process_prompts

def main():
    # Step 1: Load Documents
    documents = load_documents("../data/")  # Adjust the path as needed

    # Step 2: Load the LLM and Embedding Models
    llm = load_llm()
    embed_model = load_embedding_model()

    # Step 3: Create the Query Engine
    query_engine = create_query_engine(documents, llm, embed_model)

    # Step 4: Run Interactive QA
    prompt_file = "../data/Prompts.txt"  # Adjust the path as needed
    process_prompts(prompt_file, query_engine)

if __name__ == "__main__":
    main()
