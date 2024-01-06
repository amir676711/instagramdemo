from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import professionaldash
from api.request.professionaldash import CreatePDRequest,EditPDRequest
from api.respones.professionaldash import CreatePDRespones 
from datetime import datetime



router = APIRouter(prefix="/api/v1/professionaldash")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all")
def GetPD(db:Session=Depends(get_db)):
    return professionaldash.get_PD(db)

@router.post("/",status_code=201,response_model=BaseMessage)
def create_PD(req :CreatePDRequest,db: Session = Depends(get_db)):
    if len(req.Title) < 1:
            raise HTTPException(status_code=400,detail=" موضوع را وارد کنید")
    if len(req.Mini_Text) < 1:
            raise HTTPException(status_code=400,detail=" متن  را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    UserPD=professionaldash.Create_PD(db=db,Title=req.Title,Mini_Text=req.Mini_Text)
    return BaseMessage(message=" داشبورد پرو باموفقیت ثبت شد")

@router.patch("/changepd",status_code=200,response_model=BaseMessage)
def changePD(req:EditPDRequest,db:Session=Depends(get_db)):
    pd=professionaldash.get_PD_BYID(db,req.id)
    if pd is None :
        raise HTTPException(status_code=404 , detail="پروفایل پرو مورد نظر یافت نشد")
    pd.id=req.id,
    pd.Title = req.Title
    pd.Mini_Text = req.Mini_Text
    db.commit()
    return BaseMessage(message=" پروفایل پرو کاربر با موفقیت تغییر کرد")

@router.delete("/{id}",response_model=BaseMessage)
def Delete_PD(id:int,db:Session=Depends(get_db)):
    delete_UserPD=professionaldash.get_PD_BYID(db,id)
    if delete_UserPD is None :
        raise HTTPException(status_code=404,detail=" داشبود پرو مورد نظر یافت نشد")
    if not professionaldash.delete_PD(db,id) :
        raise HTTPException(status_code=400,detail="در حذف  داشبود پرو خطا رخ داده است")
    return BaseMessage(message=" داشبورد پرو مورد نظر با موفقیت حذف شد")

