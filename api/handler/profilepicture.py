from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import profilepicture
from api.request.profilepicture import CreateProfilePictureRequest
from api.respones.profilepicture import CreateProfilePictureRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/profilepicture")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all")
def GetProfilePicture(db:Session=Depends(get_db)):
    return profilepicture.get_Profilepicture(db)

@router.post("/",status_code=201,response_model=BaseMessage)
def create_profilePic(req :CreateProfilePictureRequest,db: Session = Depends(get_db)):
    if len(req.PictureUrl) < 1:
            raise HTTPException(status_code=400,detail="عکس پروفایل را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    Picture=profilepicture.create_profilePicture(db=db,PictureUrl=req.PictureUrl)
    return BaseMessage(message="عکس پروفایل باموفقیت ثبت شد")


@router.delete("/{id}",response_model=BaseMessage)
def DeleteProfilepic(id:int,db:Session=Depends(get_db)):
    delete_Picture=profilepicture.get_Profilepicture_BYID(db,id)
    if delete_Picture is None :
        raise HTTPException(status_code=404,detail="عکس مورد نظر یافت نشد")
    if not profilepicture.delete_ProPicture(db,id) :
        raise HTTPException(status_code=400,detail="در حذف عکس پروفایل خطا رخ داده است")
    return BaseMessage(message="عکس پروفایل مورد نظر با موفقیت حذف شد")

