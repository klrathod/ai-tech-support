from temporalio import activity


@activity.defn
async def send_notification(email: str, message: str):
    print(f"Sending email to {email}")
    return {
        "status": "sent",
    }
