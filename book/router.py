from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import author
from book import schemas, crud
from db.utils import get_db

router = APIRouter()


@router.post("/authors/{author_id}/books/", response_model=schemas.Book)
def create_book(
    author_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    db_author = author.crud.Author.get_by_id(db=db, author_id=author_id)

    if db_author is None:
        raise HTTPException(
            status_code=400,
            detail="Author not found",
        )

    return crud.Book.create(db=db, author_id=author_id, book=book)


@router.get("/books/", response_model=List[schemas.Book])
def list_books(
    author_id: int | None = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.Book.get_all(
        db=db, author_id=author_id, skip=skip, limit=limit
    )
