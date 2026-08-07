from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template= "Create a tweet on this topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Create a linkedin post for this topic: {topic}",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel(
    {
        "tweet" : RunnableSequence(prompt1, model, parser),
        "linkedin" : RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({"topic" : "my new position"})

print(result)