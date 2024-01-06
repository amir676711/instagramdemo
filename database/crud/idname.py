from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def get_idName(db: Session):
    return db.query(models.IdName).all()

def get_idName_BYID(db: Session,id:int):
    return db.query(models.IdName).filter(models.IdName.id==id).first()

def create_IdName(db:Session,Name:str):
    new_IdName = models.IdName(Name=Name)
    db.add(new_IdName)
    db.commit()
    db.refresh(new_IdName)
    return new_IdName

def delete_IdName(db:Session,id=int):
    try:
        delete_idName = db.query(models.IdName).filter(models.IdName.id==id).first()
        db.delete(delete_idName)
        db.commit()
    except:
        return False
    return True

