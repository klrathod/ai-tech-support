import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from backend.temporal.activities.notification_activity import send_notification
from backend.temporal.workflows.support_ticket_workflow import SupportTicketWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="notification-queue",
        workflows=[
            SupportTicketWorkflow,
        ],
        activities=[
            send_notification,
        ],
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
