from typing import List
from server.schemas.common import RecipeSequenceBase


class RecipeSecuenceCreate(RecipeSequenceBase):
    pass


class RecipeSecuence(RecipeSecuenceCreate):
    id: int