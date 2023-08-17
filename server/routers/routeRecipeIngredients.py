# レシピ食材の一覧
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from server.db.database import get_db
from server.schemas.token import TokenData
from server.services.toRecipeingredient import create
from server.services.toAuth import get_current_user
from server.schemas.recipeIngredient import (
    RecipeIngredient,
    RecipeIngredientCreate,
)


router = APIRouter()


# リクエストボディからレシピ材料を作成して、データベースに保存する
@router.post("/recipes/{recipe_id}/ingredients/", response_model=RecipeIngredient)
async def create_recipeingridient(
    recipe_id: int,
    ingredient: RecipeIngredientCreate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create(db=db, recipe_id=recipe_id, ingredient=ingredient)
