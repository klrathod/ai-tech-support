from backend.api.schemas.analytics_schema import AnalyticsResponse


class AnalyticsController:
    async def get_dashboard_metrics(self) -> AnalyticsResponse:
        return AnalyticsResponse(
            total_requests=1200,
            total_tokens=550000,
            average_latency=1.2,
            active_users=87,
        )


analytics_controller = AnalyticsController()
