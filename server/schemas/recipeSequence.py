from typing import List
from server.schemas.common import RecipeSequenceBase


class RecipeSequenceCreate(RecipeSequenceBase):
    recipe_id: int


class RecipeSequence(RecipeSequenceCreate):
    id: int