import schemas, models, crud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from server.database import get_db
from server.utils.depends import get_pwd_context

router = APIRouter()

@router.post("/user/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    pwd_context: CryptContext = Depends(get_pwd_context),
):
    # passwordが8文字以上であるかをチェック
    if len(user.password) < 8:
        raise HTTPException(status_code=400, detail="パスワードは8文字以上である必要があります")

    # Emailの重複をチェックする
    existing_user = (
        db.query(models.User).filter(models.User.email == user.email).first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="このEmailは既に使用されています")

    # ハッシュ化されたパスワードをデータベースに保存する
    # パスワードをハッシュ化
    # hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    hashed_password = pwd_context.hash(user.password)
    user_data = schemas.UserCreate(
        username=user.username, password=hashed_password, email=user.email
    )

    return crud.create_user(db=db, user=user_data)
