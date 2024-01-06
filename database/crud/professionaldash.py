from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def get_PD(db: Session):
    return db.query(models.ProfessionalDash).all()

def get_PD_BYID(db: Session,id:int):
    return db.query(models.ProfessionalDash).filter(models.ProfessionalDash.id==id).first()

def Create_PD(db:Session,Title:str,Mini_Text:str):
    new_PD = models.ProfessionalDash(Title=Title,Mini_Text=Mini_Text)
    db.add(new_PD)
    db.commit()
    db.refresh(new_PD)
    return new_PD

def delete_PD(db:Session,id=int):
    try:
        deletePD = db.query(models.ProfessionalDash).filter(models.ProfessionalDash.id==id).first()
        db.delete(deletePD)
        db.commit()
    except:
        return False
    return True

