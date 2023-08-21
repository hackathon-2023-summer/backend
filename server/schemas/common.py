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
    user_id: int
    date: PythonDate
    recipename: str
    category: CategoryEnum
    photo: str
    is_favorite: bool


class RecipeIngredientBase(BaseModel):
    recipe_id: int
    ingredientname: str
    quantity: int


class RecipeSequenceBase(BaseModel):
    recipe_id: int
    step_number: int
    photo: str
    comment: str



User = TypeVar("User")
Recipe = TypeVar("Recipe")
RecipeIngredient = TypeVar("RecipeIngredient")
RecipeSequence = TypeVar("RecipeSequence")
