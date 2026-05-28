from fastapi import APIRouter

from backend.api.controllers.chat_controller import chat_controller
from backend.api.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/")
async def chat(payload: ChatRequest) -> ChatResponse:
    return await chat_controller.chat(payload)


@router.post("/rag")
async def rag_chat(payload: ChatRequest) -> ChatResponse:
    return await chat_controller.rag_chat(payload)


@router.post("/temporal")
async def temporal_chat(payload: ChatRequest):
    return await chat_controller.temporal_chat(payload.message)
