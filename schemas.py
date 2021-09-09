from typing import List
from datetime import date

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    price: int
    date: date


class User(BaseModel):
    name: str
    email: str
    password: str
    number: int
    books: List[Book]
