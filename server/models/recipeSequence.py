from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    # TIMESTAMP,
    TEXT,
    # Date as SQLDate
)
from server.models.base import Base
from . import recipe
from sqlalchemy.orm import relationship


class RecipeSequence(Base):
    __tablename__ = "recipesequences"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(
        Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=True
    )
    step_number = Column(Integer, nullable=False)
    imageURL = Column(TEXT, nullable=True)
    comment = Column(TEXT, nullable=False)
    recipe = relationship("Recipe", back_populates="sequences")
