from backend.agents.support_agent import SupportAgent
from backend.rag.retriever import retrieve_documents

agent = SupportAgent()


async def rag_pipeline(query: str):
    docs = retrieve_documents(query)

    context = "\n".join(docs)

    prompt = f"""
    Context:
    {context}

    Question:
    {query}
    """

    return await agent.execute(prompt)
