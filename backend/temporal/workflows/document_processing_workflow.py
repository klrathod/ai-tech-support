from datetime import timedelta

from temporalio import workflow

from backend.temporal.activities.document_activity import process_document


@workflow.defn
class DocumentWorkflow:
    @workflow.run
    async def run(self, content: str):
        result = await workflow.execute_activity(
            process_document,
            content,
            start_to_close_timeout=timedelta(minutes=5),
        )

        return result
