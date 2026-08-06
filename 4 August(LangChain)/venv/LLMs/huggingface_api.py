from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="Text generation"
)

model = ChatHuggingFace(llm = llm)
result = model.invoke("what is the capital of India in 2 lines")
print(result)
print(type(result))