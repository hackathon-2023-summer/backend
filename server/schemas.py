from pydantic import BaseModel

# ユーザーを作るためのデータ構造
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    
# ユーザー全体のデータ構造
class User(UserCreate):
    id: int
