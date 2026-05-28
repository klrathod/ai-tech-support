from typing import Optional

from pydantic import BaseModel


class UserProfile(BaseModel):
    id: int
    name: str
    email: str
    role: str


class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None
