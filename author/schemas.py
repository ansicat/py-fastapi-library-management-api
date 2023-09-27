from typing import Optional, List

from pydantic import BaseModel

from book.schemas import Book


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str]


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List[Book] = []

    class Config:
        orm_mode = True
