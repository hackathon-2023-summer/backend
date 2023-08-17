from typing import List
from server.schemas.common import RecipeIngredientBase


class RecipeIngredientCreate(RecipeIngredientBase):
    ingredientname: str
    quantity: int


class RecipeIngredient(RecipeIngredientCreate):
    id: int
