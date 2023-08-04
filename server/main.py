import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.database import engine
from server.models import Base
from server.routers import users

from dotenv import load_dotenv

# .env ファイルをロード
load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/fast", debug=True)
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

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
