from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv


load_dotenv()

prompt = PromptTemplate(
    template= "Write a joke on this topic {topic}",
    input_variables=["topic"]
)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="can you please explain me this joke {response}",
    input_variables=["response"]
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

print(chain.invoke({"topic" : "Rahul Gandhi"}))

