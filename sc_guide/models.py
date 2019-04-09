from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"
    character_id = Column(Integer, primary_key=True, autoincrement=True)

    moves = relationship("Move", back_populates="character")

class Move(Base):
    __tablename__ = "moves"

    move_id = Column(Integer, primary_key=True, autoincrement=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    command = Column(String, nullable=False)
    impact_frames = Column(Integer, nullable=False)
    block_frames = Column(Integer, nullable=False)
    hit_frames = Column(Integer, nullable=False)
    counter_frames = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)

    character = relationship("Character", back_populates="moves")
