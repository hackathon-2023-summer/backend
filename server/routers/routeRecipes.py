# レシピの一覧
import crud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from server.db.database import get_db
from server.schemas.recipe import Recipe, RecipeCreate

router = APIRouter()


# リクエストボディからレシピを作成して、データベースに保存する
@router.post("/recipe/", response_model=Recipe)
async def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    recipe_data = RecipeCreate(
        recipename=recipe.recipename, category=recipe.category, date=recipe.date
    )

    return crud.create_recipe(db=db, recipe=recipe_data)
