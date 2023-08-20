from typing import TypeVar
from pydantic import BaseModel
from server.models.recipe import CategoryEnum
from datetime import date as PythonDate


# ユーザーを作るためのデータ構造
class UserBase(BaseModel):
    username: str
    password: str
    email: str


# レシピを保存するためのデータ構造
class RecipeBase(BaseModel):
    date: PythonDate
    recipename: str
    category: CategoryEnum
    photo: str
    is_favorite: bool


class RecipeIngredientBase(BaseModel):
    ingredientname: str
    quantity: int


User = TypeVar("User")
Recipe = TypeVar("Recipe")
RecipeIngredient = TypeVar("RecipeIngredient")
