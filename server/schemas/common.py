from typing import TypeVar
from pydantic import BaseModel
from datetime import date as PythonDate


# ユーザーを作るためのデータ構造
class UserBase(BaseModel):
    username: str
    password: str
    email: str

# レシピを保存するためのデータ構造
class RecipeBase(BaseModel):
    user_id: int
    date: PythonDate
    recipename: str
    category: str
    photo: str
    is_favorite: bool

class RecipeIngredientBase(BaseModel):
    recipe_id: int
    ingredientname: str
    quantity: int

User = TypeVar("User")
Recipe = TypeVar("Recipe")
RecipeIngredient = TypeVar("RecipeIngredient")

class TestRecipeBase(BaseModel):
    user_id: int
    date: PythonDate
    recipename: str
    category: str
    photo: str
    is_favorite: bool