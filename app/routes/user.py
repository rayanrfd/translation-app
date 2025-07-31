from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import User, UserCreate, UserInDB
from app.db.database import SessionLocal, get_db
from app.models.user import User as UserDB
from app.auth.auth import pwd_context, verify_password, authenticate_user
from sqlalchemy.orm import Session
from app.crud.user import get_user, create_user, get_users

user_router = APIRouter(prefix="/user")

@user_router.post("/register", response_model=User)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    user = get_user(db, user_create.user_name)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db, user_create)

@user_router.post("/login", response_model=User)
def login(user_create: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_create.user_name, user_create.password)
    if not user:
        return HTTPException(status_code=401, detail="Authentification error")
    return user
