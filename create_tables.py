from app.db.database import Base, engine
from app.models.user import User
from app.models.translation import Translation

print("Creating tables...")
Base.metadata.create_all(bind=engine)
