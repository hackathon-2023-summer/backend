from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date as SQLDate,
    Enum,
    BOOLEAN,
    TEXT,
)
from server.models.base import Base
from . import user,recipeIngredient,recipeSequence
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship


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
    ingredients = relationship("RecipeIngredient", back_populates="recipes")
    sequences = relationship("RecipeSequence", back_populates="recipes")