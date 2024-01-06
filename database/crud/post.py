from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def get_posts(db: Session):
    return db.query(models.Post).all()

def get_post_ByID(db:Session,id:int):
    return db.query(models.Post).filter(models.Post.id==id).first()

def create_post(db:Session,PostPicUrl:str,TypePost:int):
    new_post = models.Post(PostPicUrl=PostPicUrl,TypePost=TypePost)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def delete_post(db:Session,id=int):
    try:
        delete_post= db.query(models.Post).filter(models.Post.id==id).first()
        db.delete(delete_post)
        db.commit()
    except:
        return False
    return True

