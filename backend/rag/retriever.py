from backend.rag.vector_store import vector_store


def retrieve_documents(query: str):
    docs = vector_store.similarity_search(query)
    return [d.page_content for d in docs]
