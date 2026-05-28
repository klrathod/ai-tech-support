class CodingAgent:
    async def generate_code(self, prompt: str):
        return {
            "code": f"Generated code for {prompt}",
        }
