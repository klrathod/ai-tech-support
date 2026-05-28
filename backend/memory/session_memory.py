class SessionMemory:
    def create_session(self, user_id):
        return {
            "session": user_id,
        }
