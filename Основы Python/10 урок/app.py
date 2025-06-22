from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from schema import UserGet, PostGet, FeedGet
import table_user
import table_post
import table_feed
from typing import List
from sqlalchemy import func

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(table_user.User).filter(table_user.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(table_post.Post).filter(table_post.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    feed = db.query(table_feed.Feed).filter(table_feed.Feed.user_id == id).order_by(table_feed.Feed.time.desc()).limit(limit).all()
    return feed

@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    feed = (db.query(table_feed.Feed).filter(table_feed.Feed.post_id == id).order_by(table_feed.Feed.time.desc()).limit(limit).all()
    )
    return feed

@app.get("/post/recommendations/", response_model=List[PostGet])
def get_recommended_posts(id: int = Query(...), limit: int = 10, db: Session = Depends(get_db)):
    posts = (
        db.query(table_post.Post)
        .select_from(table_feed.Feed)
        .join(table_post.Post, table_feed.Feed.post_id == table_post.Post.id)
        .filter(table_feed.Feed.action == "like")
        .group_by(table_post.Post.id)
        .order_by(func.count(table_post.Post.id).desc())
        .limit(limit)
        .all()
    )
    return posts