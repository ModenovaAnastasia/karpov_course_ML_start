from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":
    db: Session = SessionLocal()
    try:
        posts = (
            db.query(Post.id)
            .filter(Post.topic == "business")
            .order_by(Post.id.desc())
            .limit(10)
            .all()
        )
        result = [post.id for post in posts]
        print(result)
    finally:
        db.close()
