import os
from sqlalchemy import create_engine
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext


from server.models import Base, UserBase, User
from dotenv import load_dotenv

# .env ファイルをロード
load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
server = os.getenv("MYSQL_HOST")
db = os.getenv("MYSQL_DATABASE")
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{server}/{db}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
# app = FastAPI()
app = FastAPI(root_path="/fast")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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


@app.post("/register")
async def register(user: UserBase):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(user_name=user.username,
                   password=hashed_password, email=user.email)

    with Session(engine) as session:
        if session.query(User).filter_by(user_name=db_user.user_name).first():
            raise HTTPException(
                status_code=400,
                detail="Username already exists."
            )
        if session.query(User).filter_by(email=db_user.email).first():
            raise HTTPException(
                status_code=400,
                detail="Email already exists."
            )
        try:
            session.add(db_user)
            session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=500,
                detail="Unexpected error. Please try again later."
            )
    return {"message": "User registered successfully."}
