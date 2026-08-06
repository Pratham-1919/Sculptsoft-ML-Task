from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.4,
)
model1 = ChatHuggingFace(llm=llm)
model2 = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.4
)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the given text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template = "Generate any 5 short question answers from the following text \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="merge the provided notes and into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes","quiz"]
)



parallel_chain = {
    "notes" : prompt1 | model1 | parser,
    "quiz" : prompt2 | model2 | parser
}


merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """

    Transformer is a deep learning based on multi-head attention that process sequential data in parallel, eliminating the need to recurence and convolutions which we used earlier in RNN's. This helps the model to capture the long range dependencies. 

The architecture consists of encoder and decoder in it. The encoder process the full input BIDIRECTIONALY using self-attention to create contextual representation. While decoder generates the output sequence autoregressively using masked self-attention. 

"""

result = chain.invoke({"text" : text})

print(result)

chain.get_graph().print_ascii()
