from backend.rag.chunking import chunk_document


def ingest_document(text: str):
    chunks = chunk_document(text)
    return {
        "chunks": len(chunks),
    }
