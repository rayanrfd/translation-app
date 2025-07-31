from app.auth.auth import hash_password, verify_password, get_password_hash
from app.schemas.user import UserCreate
from app.db.database import SessionLocal
from app.models.user import User as UserDB
from sqlalchemy.orm import Session

def create_user(db: Session, user_create: UserCreate):
    hashed_password = hash_password(user_create.password)
    user_db = UserDB(
        user_name=user_create.user_name, 
        hashed_password=hashed_password
        )
    
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

def get_user(db: Session, user_name: str):
    return db.query(UserDB).filter(user_name == UserDB.user_name).first()

def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(UserDB).offset(skip).limit(limit).all()
