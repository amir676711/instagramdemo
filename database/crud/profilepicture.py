from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def get_Profilepicture(db: Session):
    return db.query(models.ProfilePicture).all()

def get_Profilepicture_BYID(db: Session,id:int):
    return db.query(models.ProfilePicture).filter(models.ProfilePicture.id).first()

def create_profilePicture(db:Session,PictureUrl:str):
    new_Picture = models.ProfilePicture(PictureUrl=PictureUrl)
    db.add(new_Picture)
    db.commit()
    db.refresh(new_Picture)
    return new_Picture

def delete_ProPicture(db:Session,id=int):
    try:
        delete_profilePicture= db.query(models.ProfilePicture).filter(models.ProfilePicture.id==id).first()
        db.delete(delete_profilePicture)
        db.commit()
    except:
        return False
    return True

