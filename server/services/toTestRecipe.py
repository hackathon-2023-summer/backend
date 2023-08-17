from sqlalchemy.orm import Session
from server.schemas.testrecipe import TestRecipeBase
from server.models.testrecipe import TestRecipe as TestRecipeModel


def create(db: Session, recipe: TestRecipeBase):
    db_recipe = TestRecipeModel(
        user_id=recipe.user_id,
        recipename=recipe.recipename,
        category=recipe.category,
        date=recipe.date,
        photo=recipe.photo,
        is_favorite=recipe.is_favorite,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe
