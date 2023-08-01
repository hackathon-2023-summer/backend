from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


#ユーザー取得
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#ユーザー登録
def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#引数として、レシピのIDを受け取り、それに該当するレシピを取得
def get_recipes(db: Session, id: int) -> models.Recipe:
    return db.query(models.Recipe).filter(models.Recipe.id == id).first()

#引数として、ユーザーを受け取り、紐づくレシピを返す
def get_recipes_by_user(db: Session, user_id: int) -> List[models.Recipe]:
    return db.query(models.Recipe).filter(models.Recipe.user_id == user_id).all






#レシピの登録
def create_recipe(db: Session, recipe: schemas.Recipe):
    db_recipe = models.Recipe(recipename=recipe.recipename,
                               category=recipe.category,
                               photo=recipe.photo,
                               date= recipe.date,
                               is_favorite = recipe.is_favorite
                               )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe