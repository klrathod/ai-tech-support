from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    total_requests: int
    total_tokens: int
    average_latency: float
    active_users: int
