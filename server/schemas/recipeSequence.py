from typing import List
from server.schemas.common import RecipeSequenceBase


class RecipeSequenceCreate(RecipeSequenceBase):
    pass


class RecipeSequence(RecipeSequenceCreate):
    id: int