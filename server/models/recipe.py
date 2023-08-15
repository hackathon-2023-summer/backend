from sqlalchemy import Column, Integer, String, ForeignKey, Date as SQLDate, Enum, BOOLEAN, TEXT
from sqlalchemy.orm import relationship
from .base import Base
from enum import Enum as PyEnum

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