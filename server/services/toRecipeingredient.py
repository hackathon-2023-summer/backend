from sqlalchemy.orm import Session
from server.schemas.recipeIngredient import RecipeIngredient
from server.models.recipeIngredient import RecipeIngredient as RecipeIngredientModel


# レシピ材料登録
def create(db: Session, ingredient: RecipeIngredient):
    db_recipeingredient = RecipeIngredientModel(
        ingredientname=ingredient.ingredientname, quantity=ingredient.quantity
    )
    db.add(db_recipeingredient)
    db.commit()
    db.refresh(db_recipeingredient)
    return db_recipeingredient
