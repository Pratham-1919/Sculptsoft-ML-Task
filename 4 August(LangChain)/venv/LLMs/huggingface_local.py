from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100
)

llm = HuggingFacePipeline(pipeline=pipe)

prompt = """<|system|>
You are a helpful assistant.
<|user|>
what is the capital of gujarat and provide its location?
<|assistant|>
"""

result = llm.invoke(prompt)

print(result)