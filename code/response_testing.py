# response_testing.py

import time

def ask_query(query, embed_model, index, llm):
    """
    Query the engine and return the response.
    """
    query_engine = index.as_query_engine(llm=llm)
    start_time = time.time()
    response = query_engine.query(query)
    end_time = time.time()
    response_time = end_time - start_time
    
    # Handle the response (assume it’s a dictionary)
    if isinstance(response, dict):
        answer = response.get('answer')
        if answer:
            return answer, response_time
    else:
        return response, response_time
