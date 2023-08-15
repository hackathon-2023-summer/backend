from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from server.db.database import get_db

from server.schemas.token import Token
from server.schemas.user import UserCreate
from server.services.authentication import authenticate_user, get_current_user
from server.services.token import create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserCreate)
async def read_users_me(current_user: UserCreate = Depends(get_current_user)):
    return current_user


@router.get("/users/me/items")
async def read_own_items(current_user: UserCreate = Depends(get_current_user)):
    return [{"item_id": 1, "owner": current_user}]
