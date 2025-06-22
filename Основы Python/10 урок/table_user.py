from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func
from sqlalchemy.orm import Session

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":
    db: Session = SessionLocal()
    try:
        result = (
            db.query(User.country, User.os, func.count().label("cnt"))
            .filter(User.exp_group == 3)
            .group_by(User.country, User.os)
            .having(func.count() > 100)
            .order_by(func.count().desc())
            .all()
        )
        print(result)
    finally:
        db.close()