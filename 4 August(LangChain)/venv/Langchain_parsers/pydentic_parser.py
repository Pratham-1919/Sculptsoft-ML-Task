from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)

model = ChatHuggingFace(llm = llm)


class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt= 18, description="Age of the person")
    city: str = Field(description="Name of the city")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = """
Generate the details of ONE fictional person from {place}.

{format_instruction}

IMPORTANT:
- Return ONLY JSON.
- Do NOT explain.
- Do NOT include markdown.
- Do NOT include Python code.
- Do NOT write any text before or after the JSON.
""",
    input_variables=["place"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({"place" : "Australia"})

print(result)