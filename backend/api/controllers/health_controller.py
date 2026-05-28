class HealthController:
    async def health_check(self):
        return {
            "status": "healthy",
            "service": "enterprise-genai-platform",
        }


health_controller = HealthController()
