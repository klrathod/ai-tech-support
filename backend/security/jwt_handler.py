from jose import jwt

from backend.config import settings


def create_token(data: dict):
    return jwt.encode(data, settings.JWT_SECRET, algorithm="HS256")
