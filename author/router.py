from typing import List

from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from author import schemas, crud
from db.utils import get_db

router = APIRouter()


@router.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = crud.Author.get_by_name(db=db, author_name=author.name)

    if db_author:
        raise HTTPException(
            status_code=400,
            detail="Author with same name already exists",
        )

    return crud.Author.create(db=db, author=author)


@router.get("/authors/", response_model=List[schemas.Author])
def list_authors(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return crud.Author.get_all(db=db, skip=skip, limit=limit)


@router.get("/authors/{author_id}/", response_model=schemas.Author)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.Author.get_by_id(db=db, author_id=author_id)

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    return db_author
