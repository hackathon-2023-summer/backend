from sqlalchemy.orm import Session
from server.schemas.recipe import RecipeBase
from server.models.recipe import Recipe as RecipeModel


def create(db: Session, recipe: RecipeBase):
    db_recipe = RecipeModel(
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
