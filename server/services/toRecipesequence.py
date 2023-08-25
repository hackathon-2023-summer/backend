from sqlalchemy.orm import Session
from server.schemas.recipeSequence import RecipeSequenceBase
from server.models.recipeSequence import (
    RecipeSequence as RecipeSequenceModel,
)


# レシピ順登録
def create(db: Session, recipe_id: int, sequence: RecipeSequenceBase):
    db_recipesequence = RecipeSequenceModel(
        recipe_id=recipe_id,
        step_number=sequence.step_number,
        imageURL=sequence.imageURL,
        comment=sequence.comment,
    )
    db.add(db_recipesequence)
    db.commit()
    db.refresh(db_recipesequence)
    return db_recipesequence