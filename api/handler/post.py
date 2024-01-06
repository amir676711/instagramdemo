from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import post
from api.request.post import CreatePostRequest,EditPostRequest
from api.respones.post import CreatePostRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/post")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def GetPosts(db:Session=Depends(get_db)):
    return post.get_posts(db)

@router.post("/",status_code=201,response_model=BaseMessage)
def create_Post(req :CreatePostRequest,db: Session = Depends(get_db)):
    if len(req.PostPicUrl) < 1:
            raise HTTPException(status_code=400,detail=" عکس پست را وارد کنید")
    if req.TypePost is None:
            raise HTTPException(status_code=400,detail=" نوع پست را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    UserPost=post.create_post(db=db,PostPicUrl=req.PostPicUrl,TypePost=req.TypePost)
    return BaseMessage(message=" پست باموفقیت ثبت شد")

@router.patch("/changepsot",status_code=200,response_model=BaseMessage)
def changepass(req:EditPostRequest,db:Session=Depends(get_db)):
    pst=post.get_post_ByID(db,req.id)
    if pst is None :
        raise HTTPException(status_code=404 , detail="پست مورد نظر یافت نشد")
    pst.id=req.id,
    pst.TypePost = req.TypePost,
    pst.PostPicUrl= req.PostPicUrl
    db.commit()
    return BaseMessage(message=" پست کاربر با موفقیت تغییر کرد")

@router.delete("/{id}",response_model=BaseMessage)
def Delete_Post(id:int,db:Session=Depends(get_db)):
    delete_UserPost=post.delete_post(db,id)
    if delete_UserPost is None :
        raise HTTPException(status_code=404,detail=" پست مورد نظر یافت نشد")
    if not post.delete_post(db,id) :
        raise HTTPException(status_code=400,detail="در حذف  پست خطا رخ داده است")
    return BaseMessage(message=" پست مورد نظر با موفقیت حذف شد")

