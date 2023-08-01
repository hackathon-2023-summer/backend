#レシピの一覧

from fastapi import Depends, APIRouter, HTTPException, status
from ..database import get_db
from sqlalchemy.orm import Session
from .. import crud, schemas
from typing import List
from fastapi.security import OAuth2PasswordBearer
from . import jwt_token


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return jwt_token.verify_token(token, credentials_exception)

# @router.post("/recipes/", response_model=schemas.Recipe)
# async def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
#     # リクエストボディから新しいレシピを作成する
#     return crud.create_recipe(db=db, recipe=recipe)

#ユーザーが持つレシピを紐付けて返す
@router.get("/recipes/{id}", response_model=schemas.Recipe)
async def read_recipes(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    recipe = crud.get_recipes_by_user(db, id, current_user.id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("/recipes/", response_model=schemas.Recipe)
async def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    # リクエストボディから新しいレシピを作成する
    return crud.create_recipe(db=db, recipe=recipe, user_id=current_user.id)







