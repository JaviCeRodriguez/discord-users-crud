from enum import Enum
from pydantic import BaseModel


class Status(int, Enum):
    DISPONIBLE = 1
    AUSENTE = 2
    OCUPADO = 3
    INVISIBLE = 4


class UserBase(BaseModel):
    username: str
    image: str = ''
    status: Status
    discriminant: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True