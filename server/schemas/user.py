from typing import List
from server.schemas.common import UserBase


class UserCreate(UserBase):
    pass


# ユーザー全体のデータ構造
class User(UserCreate):
    id: int
    # recipes:List[Recipe]=[]
