from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)

model = ChatHuggingFace(llm=llm)

perser = JsonOutputParser()

template1 = PromptTemplate(
    template = """
Generate details of one person.

{format_instruction}

Do NOT explain anything.
Do NOT write markdown.
Do NOT write Python code.
Return ONLY valid JSON.
""",
    input_variables=[],
    partial_variables={"format_instruction" : perser.get_format_instructions()}
)

chain = template1 | model | perser

result = chain.invoke({})

print(result)



