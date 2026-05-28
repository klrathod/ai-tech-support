from backend.rag.ingestion import ingest_document


class UploadController:
    async def upload_document(self, filename: str, content: str):
        result = ingest_document(content)

        return {
            "filename": filename,
            "chunks": result["chunks"],
            "status": "uploaded",
        }


upload_controller = UploadController()
