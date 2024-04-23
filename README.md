---
## **A PDF Question Answering model using RAG Architecture using [LlamaIndex🦙](https://docs.llamaindex.ai/en/stable/)**
---

# **RAG Architecture**  
The model incorporates Retrieval Augumented Generation Arrchitecture which allows the LLM to respond the to the prompt from the provided context. Generally speaking the LLMs respond to the queries from the training data it was trained with, using RAG architecture we make use of the ability of the llm that generates text with the content Retrived from the documents we provide to the model

![image](https://blogs.nvidia.com/wp-content/uploads/2023/11/LangChain-2-LLM-with-a-retriveal-process.jpg)

---
# How to run the code:

### Step 1: Setup a virtual environment
Just execute the code from the shell file in bash or just execute the statements in it separately in command prompt.

### Step 2: Huggingface Login (Optional)
If you are gonna use a model from Huggingface you may need to login or authorized to use some gated models
For that do the following in cmd on your virtual environment

```
huggingface-cli login
```

then login using your Huggingface token from your account and you can load any models from huggingface.

> If you are not using HuggingFace LLMs you can modify the '`model_loading.py`' file with the model path to yout local 

### Step 3: Data Loading:

The data loading is not automated yet, so you have to manually put path of the document in `data_processing.py` file

Soon this will be automated


### Testing the Model:
After setting up everything just run the '`prompt_testing.py`' and if you get a response with 10 answers then the model is functioning well and good.



---
> Currently working on making this a interactive tool ,to have conversations with the document content
#### Note : The Code is still under development