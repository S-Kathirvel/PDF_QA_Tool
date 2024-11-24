from llama_index.core.program import LLMTextCompletionProgram
from llama_index.core.bridge.pydantic import BaseModel, Field
from llama_index.llms.huggingface import HuggingFaceLLM
import torch
from transformers import BitsAndBytesConfig



class TableInfo(BaseModel):
	"""Information regarding a structured table."""

	table_name: str = Field(
		..., description="table name (must be underscores and NO spaces)"
	)
	table_summary: str = Field(
		..., description="short, concise summary/caption of the table"
	)


prompt_str = """\
Give me a summary of the table with the following JSON format.

- The table name must be unique to the table and describe it while being concise.
- Do NOT output a generic table name (e.g. table, my_table).

Do NOT make the table name one of the following: {exclude_table_name_list}

Table:
{table_str}

Summary: """

quantization_config = BitsAndBytesConfig(
  load_in_4bit=True,
  bnb_4bit_compute_dtype=torch.float16,
  bnb_4bit_quant_type="nf4",
  bnb_4bit_use_double_quant=True,
)



# quantization_config = BitsAndBytesConfig(
#   load_in_8bit=True,  # Load the model in 8-bit format
#   bnb_8bit_compute_dtype=torch.float16,  # Use float16 for internal computations
#   bnb_8bit_quant_type="tensor_qint8",  # Quantize weights and activations to 8-bit integer
# )


llm = HuggingFaceLLM(
generate_kwargs={"temperature": 0.50, "do_sample": True},
tokenizer_name="mistralai/Mistral-7B-Instruct-v0.2",
model_name="mistralai/Mistral-7B-Instruct-v0.2",
device_map="cuda",
model_kwargs={"torch_dtype": torch.float16 , "quantization_config": quantization_config }
)


program = LLMTextCompletionProgram.from_defaults(
	output_cls=TableInfo,
	llm=llm,
	prompt_template_str=prompt_str,
)