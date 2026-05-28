from backend.database import SessionLocal


class DatabaseTool:
    def get_db(self):
        return SessionLocal()
