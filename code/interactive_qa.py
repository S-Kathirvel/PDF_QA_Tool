# interactive_qa.py

from response_testing import ask

def process_prompts(prompt_file, query_engine):
    """
    Process and ask multiple prompts from the provided text file.
    """
    with open(prompt_file, "r") as file:
        for line in file:
            prompt = line.strip()
            print(f"Prompt: {prompt}")
            ask(query_engine, prompt)
