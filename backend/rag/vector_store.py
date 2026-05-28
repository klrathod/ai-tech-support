from langchain_community.vectorstores import FAISS

from backend.rag.embeddings import embeddings

vector_store = FAISS.from_texts(
    ["hello world"],
    embedding=embeddings,
)
