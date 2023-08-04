import os
import schemas, bcrypt, models, crud
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pymysql import IntegrityError
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

from server.database import get_db, engine
from server.models import Base, UserBase, User
from dotenv import load_dotenv

# .env ファイルをロード
load_dotenv()

Base.metadata.create_all(bind=engine)
# app = FastAPI()
app = FastAPI(root_path="/fast")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

# AWSなどにデプロイしURLのドメインが確定したら指定する。
# ブラウザからのリクエストはdockerコンテナのサービス名に基づくURLを
# 名前解決できない。
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # パスワードをハッシュ化
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
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
    user_data = schemas.UserCreate(
        username=user.username, password=hashed_password, email=user.email
    )

    return crud.create_user(db=db, user=user_data)


app.include_router(router)
