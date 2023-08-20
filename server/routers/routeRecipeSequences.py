# レシピ食材の一覧
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from server.db.database import get_db
from server.schemas.token import TokenData
from server.services.toRecipesequence import create
from server.services.toAuth import get_current_user
from server.schemas.recipeSequence import (
    RecipeSecuence,
    RecipeSecuenceCreate,
)


router = APIRouter()


# リクエストボディからレシピ順を作成して、データベースに保存する
@router.post("/recipes/{recipe_id}/sequences/", response_model=RecipeSecuence)
async def create_recipesequence(
    recipe_id: int,
    sequence: RecipeSecuenceCreate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create(db=db, recipe_id=recipe_id, sequence=sequence)