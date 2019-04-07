from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Move(Base):
    __tablename__ = "moves"

    move_id = Column(Integer, primary_key=True)
    notation = Column(String, nullable=False)
    impact_frames = Column(Integer, nullable=False)
