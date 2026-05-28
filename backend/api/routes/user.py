from fastapi import APIRouter

from backend.api.controllers.user_controller import user_controller
from backend.api.schemas.user_schema import UpdateUserRequest

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{user_id}")
async def get_profile(user_id: int):
    return await user_controller.get_profile(user_id)


@router.put("/{user_id}")
async def update_profile(user_id: int, payload: UpdateUserRequest):
    return await user_controller.update_profile(user_id, payload)
