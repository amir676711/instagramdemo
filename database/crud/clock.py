from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def getClock(db: Session):
    return db.query(models.Clock).all()
def getClock_BYID(db: Session,id:int):
    return db.query(models.Clock).filter(models.Clock.id==id).first()

def CreateClock(db:Session,Time:str):
    new_Time = models.Clock(Time=Time)
    db.add(new_Time)
    db.commit()
    db.refresh(new_Time)
    return new_Time

def delete_Time(db:Session,id=int):
    try:
        delete_Clock = db.query(models.Clock).filter(models.Clock.id==id).first()
        db.delete(delete_Clock)
        db.commit()
    except:
        return False
    return True

