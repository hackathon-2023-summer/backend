from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    BOOLEAN,
    TEXT,
    Enum,
    Date as SQLDate,
)
from enum import Enum as PyEnum
from server.utils.depends import get_base
from sqlalchemy.orm import relationship

Base = get_base()


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100))
    email = Column(String(100), unique=True)
    recipes = relationship("Recipe", back_populates="user")


class CategoryEnum(PyEnum):
    beef = "beef"
    pork = "pork"
    chicken = "chicken"
    fish = "fish"
    vegetable = "vegetable"
    other = "other"


class Recipe(Base):
    __tablename__ = "recipes"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    date = Column(SQLDate, nullable=False)
    recipename = Column(String(100), index=True, nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    photo = Column(TEXT, nullable=False)
    is_favorite = Column(BOOLEAN)
    user = relationship("User", back_populates="recipes")
    recipeIngredients = relationship("RecipeIngredient", back_populates="recipe")


class RecipeIngredient(Base):
    __tablename__ = "recipeingredients"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(
        Integer, ForeignKey("recipes.id", ondelete="SET NULL"), nullable=True
    )
    ingredientname = Column(String(255), index=True)
    quantity = Column(Integer)
    recipe = relationship("Recipe", back_populates="recipeIngredients")
