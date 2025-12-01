from sqlalchemy.orm import Session

from app import models, schemas


def list_items(db: Session):
    return db.query(models.Item).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item_in: schemas.ItemCreate):
    item = models.Item(title=item_in.title, description=item_in.description, owner_id=item_in.owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item