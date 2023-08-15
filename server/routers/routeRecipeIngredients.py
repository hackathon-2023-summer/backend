# レシピ食材の一覧

import crud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from server.db.database import get_db
from server.schemas.recipeIngredient import RecipeIngredient, RecipeIngredientCreate

router = APIRouter()


# リクエストボディからレシピ材料を作成して、データベースに保存する
@router.post("/recipeingredient/", response_model=RecipeIngredient)
async def create_recipeingridient(
    ingredient: RecipeIngredientCreate, db: Session = Depends(get_db)
):
    recipeingredient_data = RecipeIngredientCreate(
        ingredientname=ingredient.ingredientname, quantity=ingredient.quantity
    )

    return crud.create_recipeingredient(db=db, ingredient=recipeingredient_data)
