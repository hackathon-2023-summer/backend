from sqlalchemy.orm import Session
from server.schemas.recipe import Recipe
from server.models.recipe import Recipe as RecipeModel


def create(db: Session, recipe: Recipe):
    db_recipe = RecipeModel(
        recipename=recipe.recipename,
        category=recipe.category,
        date=recipe.date,
        photo=recipe.photo,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe
