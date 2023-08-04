from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field

Base = declarative_base()


class UserBase(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: str = Field(...)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100))
    email = Column(String(100), unique=True)
