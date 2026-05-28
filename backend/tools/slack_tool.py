class SlackTool:
    async def send_message(self, channel, message):
        return {
            "status": "sent",
            "channel": channel,
        }
