import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from backend.temporal.activities.llm_activity import generate_ai_response
from backend.temporal.workflows.chat_workflow import ChatWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="chat-queue",
        workflows=[ChatWorkflow],
        activities=[generate_ai_response],
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
