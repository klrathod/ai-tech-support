from fastapi import APIRouter

from backend.api.controllers.health_controller import health_controller

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check():
    return await health_controller.health_check()
