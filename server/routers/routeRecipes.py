from datetime import date as PythonDate
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from server.db.database import get_db
from server.schemas.token import TokenData
from server.services.toRecipe import create
from server.services.toAuth import get_current_user
from server.schemas.recipe import Recipe, RecipeCreate
from server.models.recipe import Recipe as RecipeModel
from server.models.recipe import CategoryEnum
import shutil
from pathlib import Path

router = APIRouter()


# リクエストボディからレシピを作成して、データベースに保存する
@router.post("/recipes", response_model=Recipe)
async def create_recipe(
    recipe: RecipeCreate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_id = current_user.id
    recipe_data = RecipeCreate(
        date=recipe.date,
        recipename=recipe.recipename,
        category=recipe.category,
        imageURL=recipe.imageURL,
        overview=recipe.overview,
        is_favorite=recipe.is_favorite,
    )
    return create(db=db, user_id=user_id, recipe=recipe_data)


def get_user_recipes(
    start_date: PythonDate,
    end_date: PythonDate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
) -> List[Recipe]:
    user_id = current_user.id
    # データベースから指定ユーザーと日付範囲のレシピを取得
    recipes = (
        db.query(RecipeModel)
        .filter(
            RecipeModel.user_id == user_id,
            RecipeModel.date >= start_date,
            RecipeModel.date <= end_date,
        )
        .all()
    )
    return recipes


@router.get("/recipes/")
def get_recipes_for_date_range(
    recipes: List[Recipe] = Depends(get_user_recipes),
) -> List[Recipe]:
    return recipes


@router.get("/categories")
def get_categories(current_user: TokenData = Depends(get_current_user)):
    return [e.value for e in CategoryEnum]


@router.get("/recipe/")
def get_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
) -> Recipe:
    user_id = current_user.id
    # データベースから指定ユーザーと指定IDのレシピを取得
    recipe = (
        db.query(RecipeModel)
        .filter(
            RecipeModel.user_id == user_id,
            RecipeModel.id == recipe_id,  # == で比較することで指定IDのレシピだけを取得
        )
        .first()  # first を使用して一番最初の一致するレシピを取得
    )

    # レシピが存在しない場合のエラーハンドリング
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found"
        )

    return recipe


@router.post("/uploadsql/")
async def upload_sql_file(
    file: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # ファイルの一時保存
    temp_file = Path("tempfile.sql")
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # SQLファイルを読み込み
    with open(temp_file, "r") as file:
        sql = file.read()

    # SQLクエリの実行
    db.execute(text(sql))
    db.commit()

    return {"message": "SQLファイルからレシピが一括挿入されました"}
