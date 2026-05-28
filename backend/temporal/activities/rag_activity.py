from temporalio import activity

from backend.rag.retriever import retrieve_documents


@activity.defn
async def retrieve_context(query: str):
    docs = retrieve_documents(query)
    return docs
