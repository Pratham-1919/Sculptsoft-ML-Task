from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature = 1.5
)

result = llm.invoke("write a peom for me on a king")

print(result.content[0]["text"].replace("**",""))