from backend.api.schemas.auth_schema import LoginRequest, LoginResponse
from backend.security.jwt_handler import create_token


class AuthController:
    async def login(self, payload: LoginRequest) -> LoginResponse:
        if payload.email != "admin@test.com":
            raise Exception("Invalid user")

        token = create_token(
            {
                "email": payload.email,
            }
        )

        return LoginResponse(
            access_token=token,
        )

    async def register(self, payload):
        return {
            "message": "User registered",
        }


auth_controller = AuthController()
