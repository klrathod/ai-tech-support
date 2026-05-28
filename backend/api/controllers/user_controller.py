from backend.api.schemas.user_schema import UpdateUserRequest, UserProfile


class UserController:
    async def get_profile(self, user_id: int):
        return UserProfile(
            id=user_id,
            name="Lokesh",
            email="lokesh@test.com",
            role="admin",
        )

    async def update_profile(self, user_id: int, payload: UpdateUserRequest):
        return {
            "message": "Profile updated",
        }


user_controller = UserController()
