from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.token import Token
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.auth import authenticate_user, create_access_token
from sqlalchemy.orm import Session
from app.db.database import get_db
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN_EXPIRES_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

token_router = APIRouter()

@token_router.post('/', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect user name or password"
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
