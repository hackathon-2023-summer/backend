from pydantic import BaseModel
import Date 

# ユーザーを作るためのデータ構造
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    
# ユーザー全体のデータ構造
class User(UserCreate):
    id: int

# レシピを保存するためのデータ構造
class RecipeCreate(BaseModel):
    date: Date
    recipename: str
    category: str
    photo: str
    is_favorite:bool

# レシピ全体のデータ構造
class Recipe(RecipeCreate):
    recipe_id: int