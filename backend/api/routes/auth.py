from fastapi import APIRouter

from backend.api.controllers.auth_controller import auth_controller
from backend.api.schemas.auth_schema import LoginRequest, LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login")
async def login(payload: LoginRequest) -> LoginResponse:
    return await auth_controller.login(payload)
