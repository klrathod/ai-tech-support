from temporalio import activity


@activity.defn
async def wait_for_approval(ticket_id: str):
    return {
        "ticket": ticket_id,
        "approved": True,
    }
