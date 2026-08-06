from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser # only in old versions
from langchain.output_parsers import ResponseSchema
dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)

model = ChatHuggingFace(llm=llm)

