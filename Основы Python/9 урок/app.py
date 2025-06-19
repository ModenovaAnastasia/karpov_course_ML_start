from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Generator

app = FastAPI()

DB_PARAMS = {
    "host": "postgres.lab.karpov.courses",
    "user": "robot-startml-ro",
    "password": "pheiph0hahj1Vaif",
    "dbname": "startml",
    "port": 6432
}

def get_db() -> Generator[psycopg2.extensions.connection, None, None]:
    conn = psycopg2.connect(**DB_PARAMS)
    try:
        yield conn
    finally:
        conn.close()

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

@app.get("/post/{id}", response_model=PostResponse)
def get_post(id: int, db: psycopg2.extensions.connection = Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute('SELECT id, text, topic FROM post WHERE id = %s', (id,))
        post = cursor.fetchone()

    if post is None:
        raise HTTPException(status_code=404, detail="post not found")

    return PostResponse(**post)