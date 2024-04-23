import time
from interactive_qa import interactive_qa
prompt_file = "./data/Prompts.txt"  # Replace with your actual filename
start_t = time.time()
#Open the file in read mode
with open(prompt_file, "r") as file:
  #Loop through each line (prompt) in the file
  for line in file:
    # Remove trailing newline character (if any)
    prompt = line.strip()
    # Call the ask function with the current prompt
    print(f"Prompt: {prompt}")
    interactive_qa(prompt)
    # t
    print("-" * 100)

end_t = time.time()
response_t = end_t - start_t
print(response_t)
