from typing import List
from server.schemas.common import RecipeIngredientBase,Recipe
class RecipeIngredientCreate(RecipeIngredientBase):
    recipe_id: int
    ingredientname: str
    quantity: int


class RecipeIngredient(RecipeIngredientCreate):
    id: int
    recipe:Recipe=None
    