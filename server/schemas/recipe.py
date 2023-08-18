from typing import List
from server.schemas.common import RecipeBase


# レシピを保存するためのデータ構造
class RecipeCreate(RecipeBase):
    pass


# レシピ全体のデータ構造
class Recipe(RecipeCreate):
    id: int
