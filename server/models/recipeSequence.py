from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    TIMESTAMP,
    TEXT,
    Date as SQLDate
)
from server.models.base import Base
from . import recipe
from sqlalchemy.orm import relationship 

class RecipeSequence(Base):
    __tablename__ = "recipesequences"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer,primary_key=True, autoincrement=True)
    recipe_id = Column(Integer,ForeignKey("recipes.id"),nullable=False)
    step_number = Column(Integer,nullable=True)
    photo = Column(TEXT,nullable=True)
    comment = Column(TEXT,nullable=False)
    timestamp = Column(TIMESTAMP)
    recipe = relationship("Recipe", back_populates="redipesequences")