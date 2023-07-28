from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestUser(Base):
    __tablename__ = 'test_users'
    id = Column(Integer, Sequence('test_user_id_seq'), primary_key=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
