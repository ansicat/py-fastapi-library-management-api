from sqlalchemy.orm import Session

from book import schemas
from db import models


class Book:
    @staticmethod
    def get_all(db: Session, author_id: int, skip: int = 0, limit: int = 10):
        queryset = db.query(models.Book)

        if author_id:
            queryset = queryset.filter(models.Book.author_id == author_id)

        return queryset.offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, author_id: int, book: schemas.BookCreate):
        db_book = models.Book(
            title=book.title,
            summary=book.summary,
            publication_date=book.publication_date,
            author_id=author_id,
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)

        return db_book
