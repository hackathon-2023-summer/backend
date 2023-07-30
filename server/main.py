import os
from sqlalchemy import create_engine
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from server.models import Base, TestUser
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
app = FastAPI(root_path="/api")

# AWSなどにデプロイしURLのドメインが確定したら指定する。
# ブラウザからのリクエストはdockerコンテナのサービス名に基づくURLを
# 名前解決できない。
# origins = [
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/{user_name}")
def create_user(user_name: str):
    with Session(engine) as session:
        session.add(TestUser(user_name=user_name))
        session.commit()
