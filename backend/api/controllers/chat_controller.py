from backend.api.schemas.chat_schema import ChatRequest, ChatResponse
from backend.workflows.chat_workflow import run_chat_workflow
from backend.workflows.rag_workflow import rag_pipeline
from temporalio.client import Client


class ChatController:
    async def chat(self, payload: ChatRequest) -> ChatResponse:
        response = await run_chat_workflow(payload.message)
        return ChatResponse(
            response=response,
        )

    async def rag_chat(self, payload: ChatRequest) -> ChatResponse:
        response = await rag_pipeline(payload.message)
        return ChatResponse(
            response=response,
        )

    async def temporal_chat(self, query: str):
        client = await Client.connect("localhost:7233")

        handle = await client.start_workflow(
            "ChatWorkflow.run",
            query,
            id="chat-workflow-id",
            task_queue="chat-queue",
        )

        result = await handle.result()

        return {
            "response": result,
        }


chat_controller = ChatController()
