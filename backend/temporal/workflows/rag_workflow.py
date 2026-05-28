from datetime import timedelta

from temporalio import workflow

from backend.temporal.activities.llm_activity import generate_ai_response
from backend.temporal.activities.rag_activity import retrieve_context


@workflow.defn
class RAGWorkflow:
    @workflow.run
    async def run(self, query: str):
        docs = await workflow.execute_activity(
            retrieve_context,
            query,
            start_to_close_timeout=timedelta(seconds=20),
        )

        context = "\n".join(docs)

        final_prompt = f"""
        Context:
        {context}

        Question:
        {query}
        """

        response = await workflow.execute_activity(
            generate_ai_response,
            final_prompt,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return response
