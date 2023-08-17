from sqlalchemy.orm import Session
from server.schemas.recipeIngredient import RecipeIngredientCreate
from server.models.recipeIngredient import (
    RecipeIngredient as RecipeIngredientModel,
)


# レシピ材料登録
def create(db: Session, recipe_id: int, ingredient: RecipeIngredientCreate):
    db_recipeingredient = RecipeIngredientModel(
        recipe_id=recipe_id,
        ingredientname=ingredient.ingredientname,
        quantity=ingredient.quantity,
    )
    db.add(db_recipeingredient)
    db.commit()
    db.refresh(db_recipeingredient)
    return db_recipeingredient
