# レシピの一覧
import schemas, models, crud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from server.database import get_db
from server.utils.depends import get_pwd_context

router = APIRouter()

# リクエストボディからレシピを作成して、データベースに保存する
@router.post("/recipe/",response_model=schemas.Recipe)
async def create_recipe(recipe : schemas.RecipeCreate, db: Session = Depends(get_db)):
    recipe_data = schemas.RecipeCreate(
        recipename=recipe.recipename,category=recipe.category,date=recipe.date
    )

    return crud.create_recipe(db=db,recipe=recipe_data)
