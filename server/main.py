from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routers import routeRecipeIngredients, routeRecipes, routeUsers
from server.services import auth_routes, s3upload
from server.db.session import get_pwd_context

pwd_context = get_pwd_context()

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

app.include_router(routeUsers.router)
app.include_router(auth_routes.router)
app.include_router(s3upload.router)
app.include_router(routeRecipes.router)
app.include_router(routeRecipeIngredients.router)


@app.get("/")
def read_root():
    hashed_password = pwd_context.hash("hahaha")
    return {"hashed_password": hashed_password}
