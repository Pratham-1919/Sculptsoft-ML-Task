from langchain_huggingface import HuggingFaceEmbeddings 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    
)

document = [
    "ML includes the combination of supervised and unsupervised learning algorithms",
    "We use fastApi for routing through API",
    "play cricket for fun",
    "do Gym to stay healty"
]

query = "what do we use in ML"

doc_embedding = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

print(cosine_similarity([query_embedding], doc_embedding))