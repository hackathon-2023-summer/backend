from typing import List
from server.schemas.common import RecipeIngredientBase


class RecipeIngredientCreate(RecipeIngredientBase):
    pass


class RecipeIngredient(RecipeIngredientCreate):
    id: int
