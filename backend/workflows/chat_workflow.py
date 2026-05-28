from backend.agents.support_agent import SupportAgent

agent = SupportAgent()


async def run_chat_workflow(query: str):
    result = await agent.execute(query)
    return result
