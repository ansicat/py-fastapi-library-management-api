import uvicorn
from fastapi import FastAPI

from author import router as author_router
from book import router as book_router
from db import models
from db.database import engine

app = FastAPI(title="Library Management API")

app.include_router(author_router.router)
app.include_router(book_router.router)

models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
