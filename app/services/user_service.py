from sqlalchemy.orm import Session

from app import models, schemas


def list_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user_in: schemas.UserCreate):
    # NOTE: Password handling is omitted for brevity; add hashing in real apps.
    user = models.User(email=user_in.email, full_name=user_in.full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user