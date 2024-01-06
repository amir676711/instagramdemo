from sqlalchemy.orm import Session
from database import models
from datetime import datetime
import hashlib
from api.request.account import CreateAccountRequest
from sqlalchemy import and_,or_



def get_account(db: Session):
    return db.query(models.ccount).all()

def get_account_BYID(db: Session,id:int):
    # hashed_password = hashlib.md5(Password.encode('utf-8'))
    # print(hashed_password)
    return db.query(models.ccount).filter(models.ccount.id==id).first()

def create_account(db:Session,user:CreateAccountRequest):
    hashed_password = hashlib.md5(user.Password.encode('utf-8'))
    new_account = models.ccount(UserName=user.UserName,Password=hashed_password.hexdigest())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def login(db:Session,UserName:str,Password:str):
    hashed_password = hashlib.md5(Password.encode('utf-8'))
    print(hashed_password)
    return db.query(models.ccount).filter(and_(models.ccount.id==id,models.ccount.UserName == UserName,models.ccount.Password == hashed_password.hexdigest())).first()

def delete_account(db:Session,id=int):
    try:
        delete_account = db.query(models.ccount).filter(models.ccount.id==id).first()
        db.delete(delete_account)
        db.commit()
    except:
        return False
    return True

