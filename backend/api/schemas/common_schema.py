from typing import Optional

from pydantic import BaseModel


class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None


class Pagination(BaseModel):
    page: int
    limit: int
    total: int
