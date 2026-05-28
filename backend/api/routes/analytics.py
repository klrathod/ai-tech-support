from fastapi import APIRouter

from backend.api.controllers.analytics_controller import analytics_controller

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/dashboard")
async def dashboard():
    return await analytics_controller.get_dashboard_metrics()
