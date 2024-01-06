from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def get_Highlits(db: Session):
    return db.query(models.Highlits).all()

def get_Highlits_ByID(db:Session,id:int):
    return db.query(models.Highlits).filter(models.Highlits.id==id).first()

def create_Highlits(db:Session,PicUrl:str,Name:str):
    new_Highlits = models.Highlits(PicUrl=PicUrl,Name=Name)
    db.add(new_Highlits)
    db.commit()
    db.refresh(new_Highlits)
    return new_Highlits

def delete_Highlits(db:Session,id=int):
    try:
        delete_Highlits= db.query(models.Highlits).filter(models.Highlits.id==id).first()
        db.delete(delete_Highlits)
        db.commit()
    except:
        return False
    return True

