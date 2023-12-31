from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from server.db.database import get_db
from server.db.session import get_pwd_context
from server.schemas.user import User, UserCreate
from server.models.user import User as UserModel
from server.schemas.common import UserRead
from server.services.toUser import create
from server.schemas.token import TokenData
from server.services.toAuth import get_current_user

router = APIRouter()
pwd_context = get_pwd_context()


@router.post("/register", response_model=User)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    pwd_context: CryptContext = Depends(get_pwd_context),
):
    # passwordが8文字以上であるかをチェック
    if len(user.password) < 8:
        raise HTTPException(status_code=400, detail="パスワードは8文字以上である必要があります")

    # Emailの重複をチェックする
    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="このEmailは既に使用されています")

    # ハッシュ化されたパスワードをデータベースに保存する
    # パスワードをハッシュ化
    # hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    hashed_password = pwd_context.hash(user.password)
    user_data = UserCreate(
        username=user.username, password=hashed_password, email=user.email
    )

    return create(db=db, user=user_data)


@router.get("/user/", response_model=UserRead)
def get_user(
    db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)
):
    user = db.query(UserModel).filter(UserModel.id == current_user.id).first()
    return user  # UserRead型に自動変換されます
