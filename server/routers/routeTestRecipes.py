# レシピの一覧
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from server.db.database import get_db
from server.schemas.token import TokenData
from server.services.toTestRecipe import create
from server.services.toAuth import get_current_user
from server.schemas.testrecipe import TestRecipe, TestRecipeCreate

router = APIRouter()


# リクエストボディからレシピを作成して、データベースに保存する
@router.post("/testrecipe/", response_model=TestRecipe)
async def create_recipe(
    recipe: TestRecipeCreate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    recipe_data = TestRecipeCreate(
        user_id=recipe.user_id,
        date=recipe.date,
        recipename=recipe.recipename,
        category=recipe.category,
        photo=recipe.photo,
        is_favorite=recipe.is_favorite,
    )

    return create(db=db, recipe=recipe_data)
