from pydantic import BaseModel
from datetime import date as PythonDate



# ユーザーを作るためのデータ構造
class UserCreate(BaseModel):
    username: str
    password: str
    email: str


# ユーザー全体のデータ構造
class User(UserCreate):
    id: int



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None

# レシピを保存するためのデータ構造
class RecipeCreate(BaseModel):
    date: PythonDate
    recipename: str
    category: str
    photo: str
    is_favorite: bool


# レシピ全体のデータ構造
class Recipe(RecipeCreate):
    id: int
