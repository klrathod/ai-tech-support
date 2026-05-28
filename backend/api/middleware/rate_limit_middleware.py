from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

RATE_LIMIT = 100

request_counter = {}


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        request_counter[client_ip] = request_counter.get(client_ip, 0) + 1

        if request_counter[client_ip] > RATE_LIMIT:
            return JSONResponse(
                status_code=429,
                content={"message": "Rate limit exceeded"},
            )

        response = await call_next(request)
        return response
