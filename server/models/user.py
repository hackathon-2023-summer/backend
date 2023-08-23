from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from server.models.base import Base
from . import recipe


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100))
    email = Column(String(100), unique=True)
    recipes = relationship("Recipe", back_populates="user")
