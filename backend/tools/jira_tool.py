import httpx


class JiraTool:
    async def create_ticket(self, title, description):
        return {
            "ticket": "JIRA-1001",
            "title": title,
        }
