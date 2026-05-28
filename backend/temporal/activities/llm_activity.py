from temporalio import activity

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
)


@activity.defn
async def generate_ai_response(query: str):
    response = await llm.ainvoke(query)
    return response.content
