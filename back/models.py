from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, Boolean
from .database import Base
from sqlalchemy.orm import relationship
import datetime
# from sqlalchemy import Enum 


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100))
    email = Column(String(100), unique=True)
    

# class CategoryEnum(Enum):
#     揚げ物 = '揚げ物'
#     焼き物 = '焼き物'
#     煮物 = '煮物'


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recipename = Column(String(100), index=True)
    # category = Column(Enum(CategoryEnum))
    category = Column(String(100))
    photo = Column(String(100))
    date = Column(DateTime)
    is_favorite = Column(Boolean)
    
    # user_id = Column(Integer,  ForeignKey('users.id', ondelete='SET NULL'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'))

    user = relationship('User', back_populates='recipes')

    
# class RecipeIngredient(Base):
#     __tablename__ = 'recipeingredients'
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     ingredientname = Column(String)
#     quantity = Column(Integer)
    
#     recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='SET NULL'), nullable=False)
#     recipe = relationship('Recipe', back_populates='ingredients')

    
# class RecipeSequence(Base):
#     __tablename__ ='recipeSequences '
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     step_number = Column(Integer)
#     photo = Column(String(100))
#     comment = Column(String(255))
    
#     recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='SET NULL'), nullable=False)
#     recipe = relationship('Recipe', back_populates='sequences')
    
# class Stock(Base):
#     __tablename__ ='stocks'
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     stock_level = Column(String(255))
#     checked_day = Column(DateTime, default=datetime.now)
    
#     user_id = Column(Integer,  ForeignKey('users.id', ondelete='SET NULL'), nullable=False)
#     user = relationship('User', back_populates='stocks')
    

# UserとRecipeの関連付け
User.recipes = relationship('Recipe', back_populates='user')

# RecipeとRecipeIngredientの関連付け
# Recipe.ingredients = relationship('RecipeIngredient', back_populates='recipe')

# # RecipeとRecipeSequenceの関連付け
# Recipe.sequences = relationship('RecipeSequence', back_populates='recipe')

# # USERとStockの関連付け
# User.stocks = relationship('Stock', back_populates='user')




    
