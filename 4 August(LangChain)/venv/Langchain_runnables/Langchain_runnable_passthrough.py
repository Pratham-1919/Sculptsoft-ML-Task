from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template= "Create a joke on this topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain me this joke: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()


joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke" : RunnablePassthrough(),
        "Explanation" : RunnableSequence(prompt2, model, parser)
    }
)

final = RunnableSequence(joke_chain, parallel_chain)

print(final.invoke({"topic" : "Congress"}))