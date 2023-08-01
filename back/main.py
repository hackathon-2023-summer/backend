from fastapi import FastAPI# Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import users, recipes# recipeIngredient, recipesequence, stocks

# # テーブルをデータベースに作成
# from sqlalchemy.exc import OperationalError
models.Base.metadata.create_all(bind=engine)

# try:
#     models.Base.metadata.create_all(bind=engine)
#     print("テーブルが正常に作成されました。")
# except OperationalError as e:
#     print(f"テーブルの作成中にエラーが発生しました：{e}")


app = FastAPI(root_path="/api", debug=True)

app.include_router(users.router)
app.include_router(recipes.router)
# app.include_router(recipeIngredient.router)
# app.include_router(recipesequence.router)
# app.include_router(stocks.router)

#Read

#レシピの一覧を返す
# @app.get("/recipes", response_model=List[schemas.Recipe])
# async def read_recipes(db: Session = Depends(get_db)):
#     recipes = crud.get_recipes(db)
#     return recipes

# @app.post("/recipes")
# async def create_user(recipes: Recipe):
#     return {"recipes":recipes}


# @app.post("/recipe_ingredients")
# async def create_user(recipe_ingredients: RecipeIngredient):
#     return {"recipe_ingredients":recipe_ingredients}


# @app.post("/recipe_sequences")
# async def create_user(recipe_sequences: RecipeSequence):
#     return {"recipe_sequences":recipe_sequences}


# @app.post("/stocks")
# async def stock_memo(stocks: Stock):
#     return {"stocks": stocks}


# AWSなどにデプロイしURLのドメインが確定したら指定する。
# ブラウザからのリクエストはdockerコンテナのサービス名に基づくURLを
# 名前解決できない。
# origins = [
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    # allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






