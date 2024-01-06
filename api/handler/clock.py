from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import clock
from api.request.clock import CreateClockRequest,EditClockRequest
from api.respones.clock import CreateClockRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/clock")
access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def GetClock(db:Session=Depends(get_db)):
    return clock.getClock(db)
@router.post("/",status_code=201,response_model=BaseMessage)
def create_Time(req :CreateClockRequest,db: Session = Depends(get_db)):
    if len(req.Time) < 1:
            raise HTTPException(status_code=400,detail="  ساعت را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    UserTime=clock.CreateClock(db=db,Time=req.Time)
    return BaseMessage(message=" ساعت باموفقیت ثبت شد")

@router.patch("/changetime",status_code=200,response_model=BaseMessage)
def changepass(req:EditClockRequest,db:Session=Depends(get_db)):
    time=clock.getClock_BYID(db,req.id)
    if time is None :
        raise HTTPException(status_code=404 , detail="ساعت مورد نظر یافت نشد")
    time.id=req.id,
    time.Time = req.Time
    db.commit()
    return BaseMessage(message=" ساعت کاربر با موفقیت تغییر کرد")


@router.delete("/{id}",response_model=BaseMessage)
def Delete_account(id:int,db:Session=Depends(get_db)):
    deletetime=clock.getClock_BYID(db,id)
    if deletetime is None :
        raise HTTPException(status_code=404,detail=" ساعت مورد نظر یافت نشد")
    if not clock.delete_Time(db,id) :
        raise HTTPException(status_code=400,detail="در حذف ساعت کاربر خطا رخ داده است")
    return BaseMessage(message="ساعت کاربر مورد نظر با موفقیت حذف شد")
