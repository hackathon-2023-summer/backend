from server import schemas, models
from sqlalchemy.orm import Session


# ユーザー登録
def create_user(db: Session, user: schemas.User):
    db_user = models.User(
        username=user.username, password=user.password, email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# レシピ登録
def create_recipe(db: Session, recipe: schemas.Recipe):
    db_recipe = models.Recipe(
        recipename=recipe.recipename,
        category=recipe.category,
        date=recipe.date,
        photo=recipe.photo,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


# レシピ材料登録
def create_recipeingredient(db: Session, ingredient: schemas.RecipeIngredient):
    db_recipeingredient = models.RecipeIngredient(
        ingredientname=ingredient.ingredientname, quantity=ingredient.quantity
    )
    db.add(db_recipeingredient)
    db.commit()
    db.refresh(db_recipeingredient)
    return db_recipeingredient
