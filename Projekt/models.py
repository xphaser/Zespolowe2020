from sqlalchemy import Column, Integer, String
from database import Base

MAX_STRING_LEN = 64

class User(Base):
    __tablename__ = "users"

    email = Column(
        String(MAX_STRING_LEN),
        unique=True,
        primary_key=True,
        index=True)
    username = Column(
        String(MAX_STRING_LEN),
        unique=True,
        index=True)
    password = Column(String(MAX_STRING_LEN))

class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    email = Column(
        String(MAX_STRING_LEN),
        index=True
    )
    token = Column(
        String(MAX_STRING_LEN),
        index=True
    )