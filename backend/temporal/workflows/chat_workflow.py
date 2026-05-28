from datetime import timedelta

from temporalio import workflow

from backend.temporal.activities.llm_activity import generate_ai_response


@workflow.defn
class ChatWorkflow:
    @workflow.run
    async def run(self, query: str):
        response = await workflow.execute_activity(
            generate_ai_response,
            query,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return response
