from temporalio import activity

from backend.rag.ingestion import ingest_document


@activity.defn
async def process_document(content: str):
    result = ingest_document(content)
    return result
