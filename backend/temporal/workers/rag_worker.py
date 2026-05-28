import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from backend.temporal.activities.llm_activity import generate_ai_response
from backend.temporal.activities.rag_activity import retrieve_context
from backend.temporal.workflows.rag_workflow import RAGWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="rag-queue",
        workflows=[RAGWorkflow],
        activities=[
            retrieve_context,
            generate_ai_response,
        ],
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
