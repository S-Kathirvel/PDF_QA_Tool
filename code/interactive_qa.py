from .query_engine import query_engine, res

import time


def interactive_qa(prompt):
  """
  This function allows users to interactively ask questions and receive answers
  from the query engine in a loop, printing the response time for each query.
  """
  while True:
    user_question = input("Ask a question (or type 'quit' to exit): ")

    if user_question.lower() == "quit":
      print("Exiting...")
      break

    start_time = time.time()  # Start time measurement

    # Ask the question using the query engine
    response = query_engine.query(user_question)

    end_time = time.time()  # End time measurement
    response_time = end_time - start_time  # Calculate response time

    # Check if response is a dictionary and extract answer using 'answer' key
    if isinstance(answer, dict):
      answer = response.get("answer")
      if answer:
        print(f"Answer: {answer}")
        print(f"\nResponse Time: {response_time:.4f} seconds")
    else:
      print(response)  # Handle non-dictionary responses (e.g., errors)
      print(f"Response Time: {response_time:.4f} seconds (Non-standard format)")


# Example usage (assuming query_engine is created elsewhere)
# interactive_qa()
