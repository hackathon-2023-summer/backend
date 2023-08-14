import datetime import date as PythonDate
from pydantic import BaseModel
# from enum import Enum
# from .models import CategoryEnum

#ユーザーを作るためのデータ構造
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
#ユーザー全体のデータ構造        
class User(UserCreate):
    id: int
    
    class Config:
        orm_mode = True
    

class RecipeCreate(BaseModel):
    recipename: str
    category: str
    photo: str
    date: datetime.date
    is_favorite: bool
    
class Recipe(RecipeCreate):
    id: int
    
    class Config:
        orm_mode = True
        
    
# class RecipeIngredient(BaseModel):
#     id: int
#     ingredientname: str
#     # quantity: str
    
#     class Config:
#         orm_mode = True
        
    
# class RecipeSequence(BaseModel):
#     id: int
#     step_number: int
#     photo: str
#     comment:str
    
#     class Config:
#         orm_mode = True
        
    
# class Stock(BaseModel):
#     id: int
#     stock_level: str
#     checked_day: datetime.date
#     # quantity: str
    
#     class Config:
#         orm_mode = True    
    
    
    