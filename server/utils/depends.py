import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
server = os.getenv("MYSQL_HOST")
db = os.getenv("MYSQL_DATABASE")
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{server}/{db}"

Base = declarative_base()

def get_pwd_context():
    return CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_engine():
    return create_engine(DATABASE_URL, echo=True)

def get_base():
    return Base