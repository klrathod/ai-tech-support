from datetime import timedelta

from temporalio import workflow

from backend.temporal.activities.approval_activity import wait_for_approval


@workflow.defn
class HumanApprovalWorkflow:
    @workflow.run
    async def run(self, ticket_id: str):
        approval = await workflow.execute_activity(
            wait_for_approval,
            ticket_id,
            start_to_close_timeout=timedelta(hours=24),
        )

        return approval
