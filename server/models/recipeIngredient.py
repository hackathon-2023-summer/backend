from sqlalchemy import Column, Integer, String, ForeignKey
from server.models.base import Base
from . import recipe
from sqlalchemy.orm import relationship


class RecipeIngredient(Base):
    __tablename__ = "recipeingredients"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(
        Integer, ForeignKey("recipes.id", ondelete="SET NULL"), nullable=True
    )
    ingredientname = Column(String(255), index=True)
    quantity = Column(Integer)
    recipes = relationship("Recipe", back_populates="ingredients")
