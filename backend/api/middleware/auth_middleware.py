from fastapi import Request
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from starlette.middleware.base import BaseHTTPMiddleware

from backend.config import settings


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        excluded_paths = [
            "/",
            "/health",
            "/health/",
            "/docs",
            "/openapi.json",
            "/redoc",
            "/auth/login",
        ]

        if request.url.path not in excluded_paths:
            auth_header = request.headers.get("Authorization")

            if not auth_header:
                return JSONResponse(
                    status_code=401,
                    content={"message": "Authorization missing"},
                )

            try:
                parts = auth_header.split(" ")
                if len(parts) != 2 or parts[0].lower() != "bearer":
                    return JSONResponse(
                        status_code=401,
                        content={"message": "Invalid authorization header"},
                    )

                token = parts[1]

                payload = jwt.decode(
                    token,
                    settings.JWT_SECRET,
                    algorithms=["HS256"],
                )

                request.state.user = payload
            except JWTError:
                return JSONResponse(
                    status_code=401,
                    content={"message": "Invalid token"},
                )

        response = await call_next(request)
        return response
