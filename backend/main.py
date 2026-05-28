from fastapi import FastAPI

from backend.api.middleware.auth_middleware import AuthMiddleware
from backend.api.middleware.cors_middleware import setup_cors
from backend.api.middleware.error_handler import global_exception_handler
from backend.api.middleware.logging_middleware import LoggingMiddleware
from backend.api.middleware.rate_limit_middleware import RateLimitMiddleware
from backend.api.middleware.request_id_middleware import RequestIDMiddleware
from backend.api.middleware.security_headers import SecurityHeadersMiddleware
from backend.api.routes.analytics import router as analytics_router
from backend.api.routes.auth import router as auth_router
from backend.api.routes.chat import router as chat_router
from backend.api.routes.health import router as health_router
from backend.api.routes.upload import router as upload_router
from backend.api.routes.user import router as user_router

app = FastAPI(title="Enterprise GenAI Platform")

app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(AuthMiddleware)

setup_cors(app)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(analytics_router)
app.include_router(user_router)
app.include_router(health_router)


@app.get("/")
def health_check():
    return {"status": "running"}
