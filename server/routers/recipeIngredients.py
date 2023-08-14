# レシピ食材の一覧
import schemas, models, crud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from server.database import get_db
from server.utils.depends import get_pwd_context

router = APIRouter()


# リクエストボディからレシピ材料を作成して、データベースに保存する
@router.post("/recipeingredient/", response_model=schemas.RecipeIngredient)
async def create_recipeingridient(
    ingredient: schemas.RecipeIngredientCreate, db: Session = Depends(get_db)
):
    recipeingredient_data = schemas.RecipeIngredientCreate(
        ingredientname=ingredient.ingredientname, quantity=ingredient.quantity
    )

    return crud.create_recipeingredient(db=db, ingredient=recipeingredient_data)
