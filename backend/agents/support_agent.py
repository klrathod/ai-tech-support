from langchain_openai import ChatOpenAI


class SupportAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")

    async def execute(self, query: str):
        response = await self.llm.ainvoke(query)
        return response.content
