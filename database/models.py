from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    uid = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Game(Base):
    __tablename__ = "game"

    game_id = Column(Integer, primary_key=True, nullable=False)


class ActiveGames(Base):
    __tablename__ = "active_games"

    uid = Column(Integer, ForeignKey('users.uid', ondelete='CASCADE'), nullable=False, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), nullable=False)
    
