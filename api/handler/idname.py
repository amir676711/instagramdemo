from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import idname
from api.request.idname import CreateIdNameRequest
from api.respones.idname import CreateIdNameRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/idname")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def Getidname(db:Session=Depends(get_db)):
    return idname.get_idName(db)
@router.post("/",status_code=201,response_model=BaseMessage)
def create_IDName(req :CreateIdNameRequest,db: Session = Depends(get_db)):
    if len(req.idName) < 1:
            raise HTTPException(status_code=400,detail=" نام کاربری را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    UserName=idname.create_IdName(db=db,Name=req.idName)
    return BaseMessage(message="نام کاربری باموفقیت ثبت شد")


@router.delete("/{id}",response_model=BaseMessage)
def Delete_idName(id:int,db:Session=Depends(get_db)):
    deleteidname=idname.get_idName_BYID(db,id)
    if deleteidname is None :
        raise HTTPException(status_code=404,detail=" حساب مورد نظر یافت نشد")
    if not idname.delete_IdName(db,id) :
        raise HTTPException(status_code=400,detail="در حذف حساب کاربر خطا رخ داده است")
    return BaseMessage(message="حساب کاربر مورد نظر با موفقیت حذف شد")

