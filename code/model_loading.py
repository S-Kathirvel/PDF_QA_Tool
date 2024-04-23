# For importing models from local storage
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, AutoModel

# For System and query prompt
from llama_index.core.prompts.prompts import SimpleInputPrompt

# For quantization of the model (if needed)
from transformers import BitsAndBytesConfig
import bitsandbytes
import torch

# For embedding and model loading
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter



"""# **STEP 2: LOADING THE LLM AND EMBEDDING MODELS FROM LOCAL STORAGE** #

system_prompt='''You are a Q&A assistant. Try your best to answer the user's questions based on the information in the documents.'''

query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")
"""

system_prompt="""You are a Q&A assistant designed to answer user questions in a concise and informative way. Use the information from the documents and your knowledge to provide short answers that directly address the user's intent. Avoid generating irrelevant text before the answer
    Make sure to answer it correctly and precisely and do not generate any incomplete sentences
    Don't add more queries to the existing responses, just answer the prompt and terminate the generation of response and the response should be only relevant to the context extracted from the documents and also the contents of the document feeded into the model
    GIVE SHORT ANSWERS FOR ALL QUESTIONS MINIMUM 2 SENTENCES MAXIMUM 5 OR 6 SENTENCES ONLY
    *Generate only from the given context and not from your knowledge baase, the prompts are always about the documents feeded to you and the responses are needed relevant to the context from the documents*
    "Explain" and other open ended questions (e.g., explain the campaign modules):**
    Provide a clear and concise explanation that addresses the user's intent. The responses must be within 5-6 lines only, no larger explanations needed , only needed when explaining a workflow or providing instructions to do a task
    Use the information from the documents to support your explanation
    but avoid overly verbose or repetitive language. Summarize key points
    and avoid going into unnecessary detail. Must reply in clear, completed sentences and try using precise language
    For example
    Prompt: How can I host Twixor EnCaps back end?
    Answer: Based on the information retrieved from the document, Twixor EnCaps back end can be hosted either on-premise or on the Cloud
    **If the answer cannot be found in the knowledge base, inform the user.**
    """

query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")


# (Optional) Load the quantization configuration if needed
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

llm = HuggingFaceLLM(
context_window=2000,
max_new_tokens=200,
generate_kwargs={"temperature": 0.50, "do_sample": True},
system_prompt=system_prompt,
query_wrapper_prompt=query_wrapper_prompt,
tokenizer_name="MODEL_NAME",
model_name="MODEL_NAME",
device_map="cuda",
model_kwargs={"torch_dtype": torch.float16 ,"quantization_config": quantization_config }
)
# Load the embedding model from local storage
embed_model = AutoModel.from_pretrained("EMBED_MODEL_NAME")

Settings.transformations = [SentenceSplitter(chunk_size=1024, chunk_overlap=20)]
