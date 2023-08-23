from sqlalchemy.orm import Session
from server.schemas.recipeSequence import RecipeSequenceCreate
from server.models.recipeSequence import (
    RecipeSequence as RecipeSequenceModel,
)


# レシピ順登録
def create(db: Session, recipe_id: int, sequence: RecipeSequenceCreate):
    db_recipesequence = RecipeSequenceModel(
        recipe_id=recipe_id,
        step_number=sequence.step_number,
        photo=sequence.photo,
        comment=sequence.comment,
        # timestamp=sequence.timestamp,
    )
    db.add(db_recipesequence)
    db.commit()
    db.refresh(db_recipesequence)
    return db_recipesequence