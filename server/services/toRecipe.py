from sqlalchemy.orm import Session
from server.schemas.recipe import RecipeBase
from server.models.recipe import Recipe as RecipeModel


def create(db: Session, user_id: int, recipe: RecipeBase):
    db_recipe = RecipeModel(
        user_id=user_id,
        recipename=recipe.recipename,
        category=recipe.category,
        date=recipe.date,
        imageURL=recipe.imageURL,
        overview=recipe.overview,
        is_favorite=recipe.is_favorite,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe
