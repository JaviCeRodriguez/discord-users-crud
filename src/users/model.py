from enum import Enum
from sqlalchemy import Column, Integer, String

from src.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    discriminant = Column(Integer, index=True)
    username = Column(String, index=True)
    image = Column(String)
    status = Column(Integer, default=1) # 1 = Disponible, 2 = Ausente, 3 = Ocupado y 4 = Invisible
