from typing import List
from server.schemas.common import RecipeBase,RecipeIngredient
from datetime import date as PythonDate

# レシピを保存するためのデータ構造
class RecipeCreate(RecipeBase):
    pass
    # user_id: int
    # date: PythonDate
    # recipename: str
    # category: str
    # photo: str
    # is_favorite: bool


# レシピ全体のデータ構造
class Recipe(RecipeCreate):
    id: int
    recipeIngredients:List[RecipeIngredient]=[]