# app.py

import streamlit as st
import pdfplumber  # Import pdfplumber for reading PDF files
from data_processing import process_pdf
from model_loading import load_llm
from query_engine import create_query_engine
from response_testing import ask_query

# Title and description of the app
st.title("PDF/Document Question Answering Tool")
st.write("This tool allows you to ask questions from uploaded documents using RAG and LlamaIndex.")

# File uploader for multiple PDF documents
uploaded_files = st.file_uploader("Upload PDF Documents", accept_multiple_files=True, type=["pdf"])

if uploaded_files:
    documents = []
    
    # Process each uploaded PDF file
    for uploaded_file in uploaded_files:
        with st.spinner(f"Processing {uploaded_file.name}..."):
            doc = process_pdf(uploaded_file)  # Process the PDF to extract text
            documents.extend(doc)  # Assuming process_pdf returns a list of documents

    st.success("Documents processed successfully!")
    
    # Load the language model
    with st.spinner("Loading the model..."):
        llm = load_llm()  # Function to load your LLM

    st.success("Model loaded successfully!")
    
    # Create Query Engine using the documents
    embed_model, index = create_query_engine(documents)
    
    # User input for questions
    query = st.text_input("Ask a question about the document:")
    
    # Button to submit the question
    if st.button("Get Answer"):
        if query:
            with st.spinner("Getting answer..."):
                # Call the query function to get the answer
                answer, response_time = ask_query(query, embed_model, index, llm)
                st.write(f"**Answer:** {answer}")
                st.write(f"**Response Time:** {response_time:.4f} seconds")
        else:
            st.error("Please enter a question.")
