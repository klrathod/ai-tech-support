from datetime import timedelta

from temporalio import workflow

from backend.temporal.activities.notification_activity import send_notification


@workflow.defn
class SupportTicketWorkflow:
    @workflow.run
    async def run(self, email: str):
        result = await workflow.execute_activity(
            send_notification,
            args=[
                email,
                "Support ticket created",
            ],
            start_to_close_timeout=timedelta(seconds=20),
        )

        return result
