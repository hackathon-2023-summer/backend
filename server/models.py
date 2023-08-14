from sqlalchemy import Column,ForeignKey,Integer,String,Enum,Text,Boolean,Date as SQLDate
from server.utils.depends import get_base
from pydantic import BaseModel
from sqlalchemy.orm import relationship
# from datetime import date

Base = get_base()


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100))
    email = Column(String(100), unique=True)

# class Category(Enum):
#     beef = 'beef'
#     pork = 'pork'
#     chicken = 'chicken'
#     fish = 'fish'
#     vegetable ='vegetable'
#     other = 'other'

# class Recipe(Base):
#     __tablename__ = "recipes"
#     recipe_id = Column(Integer, primary_key=True, autoincrement=True)
#     id = Column(Integer, ForeignKey('users.id',ondelete='SET NULL'), nullable=False)
#     date = Column(Date, nullable=False)
#     recipename =Column(String(100),index=True, nullable=False)
#     category =Column(Enum(Category),nullable=False)
#     photo =Column(Text,nullable=False)
#     is_favorite=Column(bool)

class RecipeModel(BaseModel):
    recipe_id: int
    id: int
    date: SQLDate
    recipename: str
    category: str
    photo: str
    is_favorite: bool

    class Config:
        arbitrary_types_allowed = True

class Recipe(Base):
    __tablename__ = "recipes"
    recipe_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, ForeignKey('users.id',ondelete='SET NULL'), nullable=True)
    date = Column(Date, nullable=False)
    recipename =Column(String(100),index=True, nullable=False)
    category =Column(Enum('beef', 'pork', 'chicken', 'fish', 'vegetable', 'other'),nullable=False)
    photo =Column(Text,nullable=False)
    is_favorite=Column(Boolean)
    recipeIngredient = relationship('RecipeIngredient')

class RecipeIngredient(Base):
    __tablename__ = 'recipeingredients'
    recipeingredient_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredientname = Column(String(255),index=True)
    quantity = Column(Integer)
    recipe_id = Column(Integer, ForeignKey('recipes.recipe_id', ondelete='SET NULL'), nullable=True)
    recipe = relationship('Recipe', back_populates='recipeIngredient')