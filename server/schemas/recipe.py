from typing import List
from server.models.recipe import CategoryEnum
from server.schemas.common import RecipeBase
from datetime import date as PythonDate


# レシピを保存するためのデータ構造
class RecipeCreate(RecipeBase):
    user_id: int
    date: PythonDate
    recipename: str
    category: CategoryEnum
    photo: str
    is_favorite: bool


# レシピ全体のデータ構造
class Recipe(RecipeCreate):
    id: int
