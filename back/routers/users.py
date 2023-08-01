from fastapi import HTTPException,Depends, status, APIRouter
import bcrypt
from ..database import get_db
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from typing import List

router = APIRouter()

@router.get("/user/{id}", response_model=schemas.User)
async def read_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if not user:
        # ユーザーが見つからない場合、リダイレクト先のURLとともに302 Foundのステータスコードを返す
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="ユーザーが見つかりません", headers={"Location": "/registration-page"})#registr.htmlに飛ばす
    return user



@router.post("/user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # パスワードをハッシュ化
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    # passwordが8文字以上であるかをチェック
    if len(user.password) < 8:
        raise HTTPException(status_code=400, detail="パスワードは8文字以上である必要があります")
    
    # Emailの重複をチェックする
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="このEmailは既に使用されています")
    # ハッシュ化されたパスワードをデータベースに保存する
    user_data = schemas.UserCreate(username=user.username, password=hashed_password, email=user.email)
    
    return crud.create_user(db=db, user=user_data)

