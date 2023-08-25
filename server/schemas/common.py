from typing import TypeVar
from pydantic import BaseModel
from server.models.recipe import CategoryEnum
from datetime import date as PythonDate


# ユーザーを作るためのデータ構造
class UserBase(BaseModel):
    username: str
    password: str
    email: str


# 読み出し専用のデータ構造
class UserRead(BaseModel):
    id: int
    username: str
    email: str


# レシピを保存するためのデータ構造
class RecipeBase(BaseModel):
    date: PythonDate
    recipename: str
    category: CategoryEnum
    imageURL: str
    overview: str
    is_favorite: bool


class RecipeIngredientBase(BaseModel):
    recipe_id: int
    ingredientname: str
    quantity: int


class RecipeSequenceBase(BaseModel):
    step_number: int
    imageURL: str
    comment: str


User = TypeVar("User")
Recipe = TypeVar("Recipe")
RecipeIngredient = TypeVar("RecipeIngredient")
RecipeSequence = TypeVar("RecipeSequence")
