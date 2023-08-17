from typing import List
from server.models.testrecipe import CategoryEnum
from server.schemas.common import TestRecipeBase
from datetime import date as PythonDate


# レシピを保存するためのデータ構造
class TestRecipeCreate(TestRecipeBase):
    user_id: int
    date: PythonDate
    recipename: str
    category: CategoryEnum
    photo: str
    is_favorite: bool


# レシピ全体のデータ構造
class TestRecipe(TestRecipeCreate):
    id: int
