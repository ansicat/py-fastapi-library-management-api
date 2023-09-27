from sqlalchemy.orm import Session

from author import schemas
from db import models


class Author:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Author).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, author_id: int):
        return (
            db.query(models.Author)
            .filter(models.Author.id == author_id)
            .first()
        )

    @staticmethod
    def get_by_name(db: Session, author_name: str):
        return (
            db.query(models.Author)
            .filter(models.Author.name == author_name)
            .first()
        )

    @staticmethod
    def create(db: Session, author: schemas.AuthorCreate):
        db_author = models.Author(
            name=author.name,
            bio=author.bio,
        )
        db.add(db_author)
        db.commit()
        db.refresh(db_author)

        return db_author
